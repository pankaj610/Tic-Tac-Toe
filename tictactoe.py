import random
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

root = tk.Tk()


board=[1,2,3,4,5,6,7,8,9]
pcturn = False
def pboard(p1, cp,):
    global board
    j=0
    for i in board:
        j+=1
        if i in cp:
            print(" X |",end="")
        elif i in p1:
            print(" O |",end="")
        else:
            print("   |",end="")
        if i%3 is 0:
            j=0
            print("\n----------")


def checkwin(cl):
    win=0
    winli=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for w in winli:
        cmn_set = set(w) & set(cl)
        if cmn_set == set(w):
            win+=1
    return win

def cmpchoice(p1,cp):
    global board
    f_choice=0
    filled = p1 + cp
    unfilled = list(set(board) - set(filled))
    # print(len(unfilled),unfilled,"unfilled")
    if len(p1) > 1 or len(cp) > 1:
        for i in unfilled:
            ncp=p1.copy()
            ncp.append(i)
            if checkwin(ncp) > 0 :
                f_choice=i
        for i in unfilled:
            ncp=cp.copy()
            ncp.append(i)
            if checkwin(ncp) > 0:
                f_choice=i
        if f_choice is 0:
            r = random.randint(0, len(unfilled) - 1)
            f_choice = unfilled[r]
    else:
        r=random.randint(0,len(unfilled)-1)
        # print(unfilled)
        f_choice=unfilled[r]
    return f_choice

p1=[]
cp=[]
def turn(mychoice, button):
    if int(mychoice) in (p1+cp):
        tkinter.messagebox.showinfo('Error', 'Incorrect Choice!!')
        return
    p1.append(int(mychoice))
    button["text"] = "X"
    if len(list(set(board) - set(p1 + cp))) is 0:
        print("Match Drawn")
        tkinter.messagebox.showinfo('Winner', 'Match Drawn')
        resetgame()
        return
    if (checkwin(p1) is 1):
        print("You Win")
        tkinter.messagebox.showinfo('Winner', 'You Win')
        resetgame()
    cc = cmpchoice(p1, cp)
    cp.append(cc)
    buttons[cc]["text"] = "O"
    if (checkwin(cp) is 1):
        print("Computer Wins")
        tkinter.messagebox.showinfo('Winner', 'Computer Win')
        resetgame()


def resetgame():
    for i in range(1,10):
        buttons[i]["text"] = ""
    p1.clear()
    cp.clear()


button1 = ttk.Button(root, text=" ", command=lambda: turn("1",  button1))
button2 = ttk.Button(root, text=" ", command=lambda: turn("2",  button2))
button3 = ttk.Button(root, text=" ", command=lambda: turn("3",  button3))
button4 = ttk.Button(root, text=" ", command=lambda: turn("4",  button4))
button5 = ttk.Button(root, text=" ", command=lambda: turn("5",  button5))
button6 = ttk.Button(root, text=" ", command=lambda: turn("6",  button6))
button7 = ttk.Button(root, text=" ", command=lambda: turn("7",  button7))
button8 = ttk.Button(root, text=" ", command=lambda: turn("8",  button8))
button9 = ttk.Button(root, text=" ", command=lambda: turn("9",  button9))


root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)

button_reset = ttk.Button(root, text="Reset Game", command=lambda: resetgame())

button1.grid(row=0, column=0, sticky="nsew", padx=4, pady=4)
button2.grid(row=0, column=1, sticky="nsew", padx=4, pady=4)
button3.grid(row=0, column=2, sticky="nsew", padx=4, pady=4)
button4.grid(row=1, column=0, sticky="nsew", padx=4, pady=4)
button5.grid(row=1, column=1, sticky="nsew", padx=4, pady=4)
button6.grid(row=1, column=2, sticky="nsew", padx=4, pady=4)
button7.grid(row=2, column=0, sticky="nsew", padx=4, pady=4)
button8.grid(row=2, column=1, sticky="nsew", padx=4, pady=4)
button9.grid(row=2, column=2, sticky="nsew", padx=4, pady=4)

button_reset.grid(row=3, column=1, sticky="nsew", padx=4, pady=4)


buttons = {1:button1,2:button2,3:button3,4:button4,5:button5,6:button6,7:button7,8:button8,9:button9}

root.mainloop()
