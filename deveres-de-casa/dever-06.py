from functools import lru_cache
import ipywidgets as widgets
from IPython.display import display, clear_output

X = "X"
O = "O"
EMPTY = None


def initial_state():
    return (
        (EMPTY, EMPTY, EMPTY),
        (EMPTY, EMPTY, EMPTY),
        (EMPTY, EMPTY, EMPTY),
    )


def player(board):
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return O if x_count > o_count else X


def actions(board):
    return tuple(
        (i, j)
        for i in range(3)
        for j in range(3)
        if board[i][j] is EMPTY
    )


def result(board, action):
    i, j = action

    if board[i][j] is not EMPTY:
        raise ValueError("Movimento inválido.")

    new_board = [list(row) for row in board]
    new_board[i][j] = player(board)

    return tuple(tuple(row) for row in new_board)


def winner(board):
    lines = [
        board[0],
        board[1],
        board[2],
        (board[0][0], board[1][0], board[2][0]),
        (board[0][1], board[1][1], board[2][1]),
        (board[0][2], board[1][2], board[2][2]),
        (board[0][0], board[1][1], board[2][2]),
        (board[0][2], board[1][1], board[2][0]),
    ]

    for line in lines:
        if line[0] is not EMPTY and line[0] == line[1] == line[2]:
            return line[0]

    return None


def terminal(board):
    return winner(board) is not None or len(actions(board)) == 0


def utility(board):
    win = winner(board)

    if win == X:
        return 1
    if win == O:
        return -1

    return 0


@lru_cache(maxsize=None)
def minimax_value(board):
    if terminal(board):
        return utility(board)

    turn = player(board)

    if turn == X:
        best = -999
        for action in actions(board):
            best = max(best, minimax_value(result(board, action)))
        return best

    best = 999
    for action in actions(board):
        best = min(best, minimax_value(result(board, action)))
    return best


def minimax(board):
    if terminal(board):
        return None

    turn = player(board)
    possible_actions = actions(board)

    if turn == X:
        return max(
            possible_actions,
            key=lambda action: minimax_value(result(board, action))
        )

    return min(
        possible_actions,
        key=lambda action: minimax_value(result(board, action))
    )


def play_colab():
    state = {
        "board": initial_state(),
        "user": None,
        "buttons": [],
    }

    title = widgets.HTML("<h2>Jogo da Velha</h2>")
    status = widgets.HTML()

    choose_x = widgets.Button(
        description="Jogar como X",
        button_style="primary",
        layout=widgets.Layout(width="130px", height="40px")
    )

    choose_o = widgets.Button(
        description="Jogar como O",
        button_style="info",
        layout=widgets.Layout(width="130px", height="40px")
    )

    again = widgets.Button(
        description="Jogar novamente",
        button_style="warning",
        layout=widgets.Layout(width="180px", height="40px")
    )

    controls = widgets.HBox([choose_x, choose_o])

    grid = widgets.GridBox(
        layout=widgets.Layout(
            width="225px",
            grid_template_columns="70px 70px 70px",
            grid_template_rows="70px 70px 70px",
            grid_gap="5px",
        )
    )

    def game_message():
        board = state["board"]

        if terminal(board):
            win = winner(board)

            if win is None:
                return "<h3>Empate!</h3>"

            if win == state["user"]:
                return f"<h3>Você venceu! ({win})</h3>"

            return f"<h3>A IA venceu! ({win})</h3>"

        if state["user"] is None:
            return "<h3>Escolha X ou O para começar.</h3>"

        if player(board) == state["user"]:
            return "<h3>Sua vez.</h3>"

        return "<h3>IA pensando...</h3>"

    def refresh():
        board = state["board"]

        for i in range(3):
            for j in range(3):
                button = state["buttons"][i][j]
                value = board[i][j]

                button.description = "" if value is EMPTY else value

                button.disabled = (
                    state["user"] is None
                    or value is not EMPTY
                    or terminal(board)
                    or player(board) != state["user"]
                )

                if value == X:
                    button.button_style = "success"
                elif value == O:
                    button.button_style = "danger"
                else:
                    button.button_style = ""

        status.value = game_message()

        if state["user"] is None:
            controls.layout.display = ""
        else:
            controls.layout.display = "none"

        if terminal(board):
            again.layout.display = ""
        else:
            again.layout.display = "none"

    def ai_move():
        board = state["board"]

        if state["user"] is None:
            return

        if terminal(board):
            return

        if player(board) == state["user"]:
            return

        move = minimax(board)

        if move is not None:
            state["board"] = result(board, move)

    def choose_player(symbol):
        state["user"] = symbol
        ai_move()
        refresh()

    def make_move(i, j):
        def click(_):
            board = state["board"]

            if state["user"] is None:
                return

            if terminal(board):
                return

            if player(board) != state["user"]:
                return

            if board[i][j] is not EMPTY:
                return

            state["board"] = result(board, (i, j))
            ai_move()
            refresh()

        return click

    def reset_game(_=None):
        state["board"] = initial_state()
        state["user"] = None
        refresh()

    buttons = []

    for i in range(3):
        row = []

        for j in range(3):
            button = widgets.Button(
                description="",
                layout=widgets.Layout(width="70px", height="70px"),
                style={"font_weight": "bold"}
            )

            button.on_click(make_move(i, j))
            row.append(button)

        buttons.append(row)

    state["buttons"] = buttons
    grid.children = [button for row in buttons for button in row]

    choose_x.on_click(lambda _: choose_player(X))
    choose_o.on_click(lambda _: choose_player(O))
    again.on_click(reset_game)

    clear_output()
    display(widgets.VBox([title, status, controls, grid, again]))

    refresh()


play_colab()
