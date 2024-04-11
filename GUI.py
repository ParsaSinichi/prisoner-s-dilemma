from tkinter import *
from tkinter import ttk
from Agents import *
from Game import *

root = Tk()
root.title("Game Theory")

# Function to start the game


def start_game():
    randm=False
    num_cheaters = int(entries[0].get())
    if (num_cheaters != 0):
        add_agent(Cheater, num_cheaters)
    num_cops = int(entries[1].get())
    if num_cops != 0:
        add_agent(Cooperative, num_cops)

    num_copycats = int(entries[2].get())
    if num_copycats != 0:
        add_agent(CopyCat, num_copycats)
    num_detective = int(entries[3].get())
    if num_detective != 0:
        add_agent(Detective, num_detective)
    num_grud = int(entries[4].get())
    if num_grud != 0:
        add_agent(Grudger, num_grud)
    num_random = int(entries[5].get())
    if num_random != 0:
        add_agent(Random, num_random)
    num_simple = int(entries[6].get())
    if num_simple != 0:
        add_agent(Simpleton, num_simple)
    num_kit = int(entries[7].get())
    if num_kit != 0:
        add_agent(CopyKitten, num_kit)
    coop = int(entries[-6].get())
    punishment = int(entries[-5].get())
    reward = int(entries[-4].get())
    num_rounds = int(entries[-3].get())
    elim_per_round = int(entries[-2].get())
    n_tour = int(entries[-1].get())
    ###
    if (randomness.get() != ""):
        randm=True
        # num_cheaters = int(entries[0].get())
        # if (num_cheaters != 0):
        #     add_agent(Cheater, num_cheaters)
        # num_cops = int(entries[1].get())
        # if num_cops != 0:
        #     add_agent(Cooperative, num_cops)

        # num_copycats = int(entries[2].get())
        # if num_copycats != 0:
        #     add_agent(CopyCat, num_copycats)
        # num_detective = int(entries[3].get())
        # if num_detective != 0:
        #     add_agent(Detective, num_detective)
        # num_grud = int(entries[4].get())
        # if num_grud != 0:
        #     add_agent(Grudger, num_grud)
        # num_random = int(entries[5].get())
        # if num_random != 0:
        #     add_agent(Random, num_random)
        # num_simple = int(entries[6].get())
        # if num_simple != 0:
        #     add_agent(Simpleton, num_simple)
        # num_kit = int(entries[7].get())
        # if num_kit != 0:
        #     add_agent(CopyKitten, num_kit)
    # add_agent(CopyCat, num_copycats)
    PlayGame1(num_rounds, coop, reward, punishment, elim_per_round, n_tour,randm)


# Creating a frame
frame = ttk.Frame(root, padding=20)
frame.grid(row=0, column=0, padx=20, pady=20)

# Labels and Entry Widgets
labels = ["Number of Cheaters:", "Number of Cooperative:", "Number of Copy Cats:",
          "Number of Detective", "Number of Grudger", "Number of Random", "Number of Simpleton",
          "Number of Copy Kitten", "Points  for both Cooperate:", "Number of punishment",
          "Number of Rewards:", "Number of Rounds:", "Eliminations per Round:", "N tour : "]
entries = [StringVar() for _ in range(len(labels))]

for i, label_text in enumerate(labels):
    ttk.Label(frame, text=label_text).grid(column=0, row=i, padx=5, pady=5)
    ttk.Entry(frame, textvariable=entries[i]).grid(
        column=1, row=i, padx=5, pady=5)

# Setting default values
default_values = ["10", "0", "100", "0", "75","0", "0", "0", "1", "1", "2", "15", "3", "20"]
for entry, value in zip(entries, default_values):
    entry.set(value)

randomness = StringVar()
check = ttk.Checkbutton(frame, text='Randomness',
                        command="", variable=randomness,
                        onvalue=True, offvalue='imperial')
check.grid(column=0, row=len(labels), columnspan=1, pady=10)
# Button to start the game
start_button = ttk.Button(frame, text="Start Game", command=start_game)
start_button.grid(column=0, row=len(labels)+1, columnspan=2, pady=10)
plt_button = ttk.Button(frame, text="Plot result ", command=plot_agents2)
plt_button.grid(column=0, row=len(labels)+2, columnspan=2, pady=10)
# Styling
style = ttk.Style()
style.configure('TButton', foreground='white', font=('Arial', 12))
style.configure('TFrame', background='#E0E0E0')
style.configure('TLabel', background='#E0E0E0')
style.configure('TEntry', fieldbackground='#FFFFFF')

root.mainloop()
