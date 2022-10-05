# Imports
from tkinter import *
import ctypes

# Compatibility Settings
ctypes.windll.shcore.SetProcessDpiAwareness(1)

# Tkinter Meta Data
root = Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root.title("Tic Tac Toe")
root.iconbitmap("logo.ico")

# Variables
turn = "x"
click_btn = []
clicked = False
win = False
buttons = []
tie = False
winner = ""
x_score_number = 0
o_score_number = 0
default_status_text = """
Status:
Waiting To Start
"""

# Main Code
def app():
    # Functions
    def higher_score_calc():
        if x_score_number > o_score_number:
            x_score_label["foreground"] = "green"
            o_score_label["foreground"] = "red"
        elif x_score_number < o_score_number:
            x_score_label["foreground"] = "red"
            o_score_label["foreground"] = "green"
        elif x_score_number == o_score_number:
            x_score_label["foreground"] = "black"
            o_score_label["foreground"] = "black"

    def win_function(player):
        def win_execution():
            global draw_type, win_btn, x_score_number, o_score_number
            if draw_type == "horizontal":
                type_character = "-"
            elif draw_type == "vertical":
                type_character = "|"
            elif draw_type == "slant-left":
                type_character = "\\"
            elif draw_type == "slant-right":
                type_character = "/"
            for i in win_btn:
                i["font"] = ("Arial", 100)
                i["text"] = type_character
            status["foreground"] = "green"
            status[
                "text"
            ] = f"""
Status:
{winner} Won the Game!!
            """

            if winner == "X":
                x_score_number += 1
                x_score_label["text"] = f"X Score: {x_score_number}"
                higher_score_calc()
            if winner == "O":
                o_score_number += 1
                o_score_label["text"] = f"O Score: {o_score_number}"
                higher_score_calc()

        def check_win_x():
            global draw_type, win_btn, win, winner
            if (
                button_1["text"] == "X"
                and button_2["text"] == "X"
                and button_3["text"] == "X"
            ):
                win = True
                winner = "X"
                win_btn = [button_1, button_2, button_3]
                draw_type = "horizontal"
                win_execution()
            elif (
                button_1["text"] == "X"
                and button_4["text"] == "X"
                and button_7["text"] == "X"
            ):
                win = True
                winner = "X"
                win_btn = [button_1, button_4, button_7]
                draw_type = "vertical"
                win_execution()

            elif (
                button_1["text"] == "X"
                and button_5["text"] == "X"
                and button_9["text"] == "X"
            ):
                win = True
                winner = "X"
                win_btn = [button_1, button_5, button_9]
                draw_type = "slant-left"
                win_execution()

            elif (
                button_2["text"] == "X"
                and button_5["text"] == "X"
                and button_8["text"] == "X"
            ):
                win = True
                winner = "X"
                win_btn = [button_2, button_5, button_8]
                draw_type = "vertical"
                win_execution()

            elif (
                button_3["text"] == "X"
                and button_6["text"] == "X"
                and button_9["text"] == "X"
            ):
                win = True
                winner = "X"
                win_btn = [button_3, button_6, button_9]
                draw_type = "vertical"
                win_execution()

            elif (
                button_3["text"] == "X"
                and button_5["text"] == "X"
                and button_7["text"] == "X"
            ):
                win = True
                winner = "X"
                win_btn = [button_3, button_5, button_7]
                draw_type = "slant-right"
                win_execution()

            elif (
                button_4["text"] == "X"
                and button_5["text"] == "X"
                and button_6["text"] == "X"
            ):
                win = True
                winner = "X"
                win_btn = [button_4, button_5, button_6]
                draw_type = "horizontal"
                win_execution()

            elif (
                button_7["text"] == "X"
                and button_8["text"] == "X"
                and button_9["text"] == "X"
            ):
                win = True
                winner = "X"
                win_btn = [button_7, button_8, button_9]
                draw_type = "horizontal"
                win_execution()

        def check_win_o():
            global draw_type, win_btn, win, winner
            if (
                button_1["text"] == "O"
                and button_2["text"] == "O"
                and button_3["text"] == "O"
            ):
                win = True
                winner = "O"
                win_btn = [button_1, button_2, button_3]
                draw_type = "horizontal"
                win_execution()

            elif (
                button_1["text"] == "O"
                and button_4["text"] == "O"
                and button_7["text"] == "O"
            ):
                win = True
                winner = "O"
                win_btn = [button_1, button_4, button_7]
                draw_type = "vertical"
                win_execution()

            elif (
                button_1["text"] == "O"
                and button_5["text"] == "O"
                and button_9["text"] == "O"
            ):
                win = True
                winner = "O"
                win_btn = [button_1, button_5, button_9]
                draw_type = "slant-left"
                win_execution()

            elif (
                button_2["text"] == "O"
                and button_5["text"] == "O"
                and button_8["text"] == "O"
            ):
                win = True
                winner = "O"
                win_btn = [button_2, button_5, button_8]
                draw_type = "vertical"
                win_execution()

            elif (
                button_3["text"] == "O"
                and button_6["text"] == "O"
                and button_9["text"] == "O"
            ):
                win = True
                winner = "O"
                win_btn = [button_3, button_6, button_9]
                draw_type = "vertical"
                win_execution()

            elif (
                button_3["text"] == "O"
                and button_5["text"] == "O"
                and button_7["text"] == "O"
            ):
                win = True
                winner = "O"
                win_btn = [button_3, button_5, button_7]
                draw_type = "slant-right"
                win_execution()

            elif (
                button_4["text"] == "O"
                and button_5["text"] == "O"
                and button_6["text"] == "O"
            ):
                win = True
                winner = "O"
                win_btn = [button_4, button_5, button_6]
                draw_type = "horizontal"
                win_execution()

            elif (
                button_7["text"] == "O"
                and button_8["text"] == "O"
                and button_9["text"] == "O"
            ):
                win = True
                winner = "O"
                win_btn = [button_7, button_8, button_9]
                draw_type = "horizontal"
                win_execution()

        if player == "x":
            check_win_x()
        elif player == "o":
            check_win_o()

    def tie_check():
        global tie
        required_clicks = [
            "button_1",
            "button_2",
            "button_3",
            "button_4",
            "button_5",
            "button_6",
            "button_7",
            "button_8",
            "button_9",
        ]
        click_btn.sort()
        if required_clicks == click_btn and not win:
            tie = True
            status["foreground"] = "#c040b1"
            status[
                "text"
            ] = f"""
Status:
The Game Got Tied!!
            """
        elif not required_clicks == click_btn:
            tie = False

    def play(btn_no):
        global turn, click_btn, clicked, win
        button_id = buttons[btn_no - 1]
        button_id_str = "button_" + str(btn_no)
        for i in click_btn:
            if i == button_id_str:
                clicked = True
                break
            else:
                clicked = False

        if not clicked and not win and not tie:
            status["foreground"] = "#26b1f3"
            status[
                "text"
            ] = f"""
Status:
Game In Progress
            """
            sub_heading["text"] = "All The Best!"
            if turn == "x":
                button_id["text"] = "X"
                turn = "o"
                click_btn.append(button_id_str)
                tie_check()
                win_function("x")
            else:
                button_id["text"] = "O"
                turn = "x"
                click_btn.append(button_id_str)
                tie_check()
                win_function("o")
        elif clicked or win or tie:
            return

    def score_reset():
        global x_score_number, o_score_number
        x_score_number = 0
        o_score_number = 0
        x_score_label["text"] = "X Score: 0"
        o_score_label["text"] = "O Score: 0"
        higher_score_calc()

    # Defining Widgets
    heading = Label(root, text="Welcome to Tic Tac Toe", font=("Arial", 45))
    sub_heading = Label(root, text="Click on any grid to start", font=("Arial", 25))
    score_heading = Label(root, text="Score Board", font=("Arial", 30))
    x_score_label = Label(root, text="X Score: 0", font=("Arial", 20))
    o_score_label = Label(root, text="O Score: 0", font=("Arial", 20))
    status = Label(
        root, text=default_status_text, font=("Arial", 35), foreground="orange"
    )
    reset_score_btn = Button(
        root,
        text="Reset Score",
        font=("Arial", 20),
        command=score_reset,
        foreground="white",
        background="black",
    )
    # -----------------------------Buttons-----------------------------
    button_1 = Button(
        root,
        font=("Arial", 50),
        command=lambda: play(1),
        border=10,
        foreground="white",
        background="black",
    )
    button_2 = Button(
        root,
        font=("Arial", 50),
        command=lambda: play(2),
        border=10,
        foreground="white",
        background="black",
    )
    button_3 = Button(
        root,
        font=("Arial", 50),
        command=lambda: play(3),
        border=10,
        foreground="white",
        background="black",
    )
    button_4 = Button(
        root,
        font=("Arial", 50),
        command=lambda: play(4),
        border=10,
        foreground="white",
        background="black",
    )
    button_5 = Button(
        root,
        font=("Arial", 50),
        command=lambda: play(5),
        border=10,
        foreground="white",
        background="black",
    )
    button_6 = Button(
        root,
        font=("Arial", 50),
        command=lambda: play(6),
        border=10,
        foreground="white",
        background="black",
    )
    button_7 = Button(
        root,
        font=("Arial", 50),
        command=lambda: play(7),
        border=10,
        foreground="white",
        background="black",
    )
    button_8 = Button(
        root,
        font=("Arial", 50),
        command=lambda: play(8),
        border=10,
        foreground="white",
        background="black",
    )
    button_9 = Button(
        root,
        font=("Arial", 50),
        command=lambda: play(9),
        border=10,
        foreground="white",
        background="black",
    )

    # Displaying Widgets
    heading.place(relx=0.5, rely=0.04, anchor=CENTER)
    sub_heading.place(relx=0.5, rely=0.109, anchor=CENTER)
    status.place(relx=0.05, rely=0.35)
    score_heading.place(relx=0.8, rely=0.3, anchor=CENTER)
    x_score_label.place(relx=0.76, rely=0.35)
    o_score_label.place(relx=0.76, rely=0.4)
    reset_score_btn.place(relx=0.745, rely=0.47)
    # -----------------Buttons--------------------
    button_1.place(relx=0.355, rely=0.2, height=370, width=370)
    button_2.place(relx=0.455, rely=0.2, height=370, width=370)
    button_3.place(relx=0.555, rely=0.2, height=370, width=370)
    button_4.place(relx=0.355, rely=0.38, height=370, width=370)
    button_5.place(relx=0.455, rely=0.38, height=370, width=370)
    button_6.place(relx=0.555, rely=0.38, height=370, width=370)
    button_7.place(relx=0.355, rely=0.56, height=370, width=370)
    button_8.place(relx=0.455, rely=0.56, height=370, width=370)
    button_9.place(relx=0.555, rely=0.56, height=370, width=370)

    # Other Codes
    buttons = [
        button_1,
        button_2,
        button_3,
        button_4,
        button_5,
        button_6,
        button_7,
        button_8,
        button_9,
    ]

    def restart():
        global click_btn, turn, clicked, win, winner, win_btn, button_id, button_id_str, tie
        turn = "x"
        click_btn = []
        clicked = False
        win = False
        winner = ""
        win_btn = []
        button_id = ""
        button_id_str = ""
        tie = False
        status["foreground"] = "orange"
        status["text"] = default_status_text
        sub_heading["text"] = "Click on any grid to start"
        for i in buttons:
            i["text"] = ""
            i["font"] = ("Arial", 50)

    restart_btn = Button(
        root,
        text="Restart",
        font=("Arial", 20),
        command=restart,
        foreground="white",
        background="black",
    )
    restart_btn.place(relx=0.5, rely=0.8, anchor=CENTER)


# Final Part
app()
root.mainloop()
