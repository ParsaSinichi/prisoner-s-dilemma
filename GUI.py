from tkinter import *
from tkinter import ttk
from Agents import *
from Game import *
root = Tk()


def pr():
    print(number_of_cheater.get())
    print(number_of_cop.get())
    print(number_of_CopyCat.get())
    if (number_of_cheater.get() != 0):
        add_agent(Cheater, int(number_of_cheater.get()))
    if (number_of_cop.get() != 0):
        add_agent(Coperative, int(number_of_cop.get()))
    if (number_of_CopyCat.get() != 0):
        add_agent(CopyCat, int(number_of_CopyCat.get()))
    reward = int(number_of_reward.get())
    round = int(number_of_round.get())
    elim = int(number_of_elim.get())
    PlayGame1(round, reward, elim)


frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
ttk.Button(frm, text="play", command=pr).grid(column=1, row=1)
number_of_cheater = StringVar()
ttk.Label(frm, text="Number of Cheaters : ").grid(column=1, row=2)
number = ttk.Entry(frm, textvariable=number_of_cheater).grid(column=2, row=2)
##
number_of_cop = StringVar()
ttk.Label(frm, text="Number of Coperative : ").grid(column=1, row=3)
number1 = ttk.Entry(frm, textvariable=number_of_cop).grid(column=2, row=3)
##
number_of_CopyCat = StringVar()
ttk.Label(frm, text="Number of Copy Cat : ").grid(column=1, row=4)
number2 = ttk.Entry(frm, textvariable=number_of_CopyCat).grid(column=2, row=4)
#
number_of_reward = StringVar()
ttk.Label(frm, text="Number of Reward: ").grid(column=1, row=5)
number3 = ttk.Entry(frm, textvariable=number_of_reward).grid(column=2, row=5)
#
number_of_round = StringVar()
ttk.Label(frm, text="Number of Round: ").grid(column=1, row=6)
number4 = ttk.Entry(frm, textvariable=number_of_round).grid(column=2, row=6)
#
number_of_elim = StringVar()
ttk.Label(frm, text="Number of elim: ").grid(column=1, row=7)
number5 = ttk.Entry(frm, textvariable=number_of_elim).grid(column=2, row=7)
#
root.mainloop()
print(number_of_cheater.get())
