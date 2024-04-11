from matplotlib.ticker import MaxNLocator
import numpy as np
import matplotlib.pyplot as plt
from Agents import *
# both Colab, one colab one not, both not
rand_prob = 0.35


# TODO : for randomness, we need to call a rand function , if that happend we need to change the 1 to 0
# TODO : after each round , n players with the lowest points will removed and the agents with highest point will replace them
Agents = []


agent_changes = {}


def initial_counts():
    """
    Initializing a Dictionary of keys(agent names) and values(number of agents after playing a round of n_tourament)
    """
    agents_name_list = [type(agent).__name__ for agent in Agents]
    for agent_name in list(set(agents_name_list)):
        agent_changes[agent_name] = []


def PlayGame1(round, cooperate, reward, punishment, del_num, n_tour, randms):
    global Agents, rand_prob
    """
    round means, number of round each two agent play against each other
    del_num : number of players to delete after each torunoment match
    """
    initial_counts()
    count = 0
    while (count < n_tour):
        # TODO the round should not be here i guess , because now, it plays one round with each agent
        for i in range(len(Agents)):
            agent1 = Agents[i]
            for j in range(i+1, len(Agents)):
                agent2 = Agents[j]
                if (type(agent1).__name__ == "CopyCat" or type(agent1).__name__ == "Detective" or type(agent1).__name__ == "CopyKitten" or type(agent1).__name__ == "Simpleton" or type(agent1).__name__ == "Grudger"):
                    agent1.memory = []
                    if (type(agent1).__name__ == "Simpleton"):
                        agent1.actions = []
                    if (type(agent1).__name__ == "Detective"):
                        agent1.moves = [1, 1, 0, 1]
                        agent1.alway_cheat = False

                if (type(agent2).__name__ == "CopyCat" or type(agent2).__name__ == "Detective" or type(agent2).__name__ == "CopyKitten" or type(agent2).__name__ == "Simpleton" or type(agent2).__name__ == "Grudger"):
                    agent2.memory = []
                    if (type(agent2).__name__ == "Simpleton"):
                        agent2.actions = []
                    if (type(agent2).__name__ == "Detective"):
                        agent2.moves = [1, 1, 0, 1]
                        agent2.alway_cheat = False
                for _ in range(round):
                    ag1 = agent1.take_action()
                    ag2 = agent2.take_action()
                    if (randms):
                        if (np.random.rand() >= rand_prob):
                            ag1 = ag1
                        else:
                            ag1 = int(not (ag1))
                    if (randms):
                        if (np.random.rand() >= rand_prob):
                            ag2 = ag2
                        else:
                            ag2 = int(not (ag2))
                    if (type(agent1).__name__ == "CopyCat" or type(agent1).__name__ == "Detective" or type(agent1).__name__ == "CopyKitten" or type(agent1).__name__ == "Simpleton" or type(agent1).__name__ == "Grudger"):
                        agent1.memory.append(ag2)
                    if (type(agent2).__name__ == "CopyCat" or type(agent2).__name__ == "Detective" or type(agent2).__name__ == "CopyKitten" or type(agent2).__name__ == "Simpleton" or type(agent2).__name__ == "Grudger"):
                        agent2.memory.append(ag1)
                    # if (type(agent1).__name__ == "Simpleton"):
                    #         agent2.
                    if ag1 == 1 and ag2 == 1:

                        agent1.points += cooperate
                        agent2.points += cooperate
                    elif ag1 == 0 and ag2 == 0:
                        pass
                    elif ag1 == 1 and ag2 == 0:
                        agent1.points -= punishment
                        agent2.points += reward
                    elif ag1 == 0 and ag2 == 1:
                        agent1.points += reward
                        agent2.points -= punishment
        # Scores = sorted([agent.points for agent in Agents], reverse=True)# Removing the agent with the least point
        # Agents[del_num:]
        for i in range(len(Agents)):
            print(
                f"{type(Agents[i]).__name__} has {Agents[i].points} Point")
        print("_____________")
        get_agents_count()
        update_agents(del_num)
        count += 1


def update_agents(del_num):
    global Agents
    # Removing the agent with the lowest point
    Agents = sorted(Agents, key=lambda agent: agent.points, reverse=True)
    Agents = Agents[:-del_num]

    for _ in range(del_num):
        # Creating New object from Agent with the Highest point
        new_instance = globals().get(type(Agents[0]).__name__)()
        Agents.append(new_instance)
    for i in range(len(Agents)):
        Agents[i].points = 0


def add_agent(agent, number, Random_miss=False):
    global Agents
    for _ in range(number):
        new_instance = agent()
        Agents.append(new_instance)


def plot_agents3():

    global agent_changes
    max_agent_len = len(agent_changes[(
        max(agent_changes, key=lambda k: len(agent_changes[k])))])
    bins = max_agent_len//2 + 1
    for key, value in agent_changes.items():
        while (len(value) < max_agent_len):
            agent_changes[key].append(0)
    colors = plt.cm.tab10.colors

    plt.figure(figsize=(15, 9))  # Adjust the figure size as needed
    # You can add more line styles if needed
    linestyles = ['-', '--', '-.', ':']
    markers = ['o', 's', '^', 'D']
    # Loop through agent_changes dictionary and plot each agent's data with a different color
    for i, (key, value) in enumerate(agent_changes.items()):
        plt.plot(range(len(value)), value, linestyle=linestyles[i % len(
            linestyles)], color=colors[i % len(colors)], label=key)

    plt.xticks(range(0, len(value), len(value) // bins),
               ['{}'.format(i)
                for i in range(1, len(value) + 1, len(value) // bins)],
               rotation=45)
    # plt.ylim(0, max_agent_len + 5)  # Adjust the upper limit as needed

    plt.xlabel('Number of iteration')
    plt.ylabel('Count')
    plt.tight_layout()  # Adjust layout to prevent overlap

    plt.legend()  # Add legend

    # Set y-axis tick locator to display only integer values
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
    # plt.gca().set_yticks(
    #     [item for sublist in agent_changes.values() for item in sublist])

    plt.show()


def plot_agents2():
    max_agent_len = len(
        agent_changes[max(agent_changes, key=lambda k: len(agent_changes[k]))])
    bins = max_agent_len // 2 + 1
    # bins = 5
    colors = plt.cm.tab10.colors

    fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(
        16, 8), gridspec_kw={'hspace': 0.5, 'wspace': 0.5})  # Adjust figsize as needed and add space between subplots

    # Loop through agent_changes dictionary and plot each agent's data in a separate subplot
    for i, (key, value) in enumerate(agent_changes.items()):
        row = i // 4
        col = i % 4
        ax = axes[row, col]
        while len(value) < max_agent_len:
            agent_changes[key].append(0)
        linestyle = '-'
        color = colors[i % len(colors)]
        ax.plot(range(len(value)), value,
                linestyle=linestyle, color=color, label=key)
        ax.set_xticks(range(0, len(value), len(value) // bins))
        ax.set_xticklabels(['{}'.format(i) for i in range(
            1, len(value) + 1, len(value) // bins)], rotation=45)
        ax.set_xlabel('Number of iteration')
        ax.set_ylabel('Count')
        ax.set_title(key)
        ax.legend()
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    # plt.tight_layout()  # Adjust layout to prevent overlap
    plt.show()


def get_agents_count():
    global agent_changes
    agents_name_list = [type(agent).__name__ for agent in Agents]
    for i in list(set([type(agent).__name__ for agent in Agents])):
        print(f"Count {i} is {agents_name_list.count(i)}")
        agent_changes[i].append(agents_name_list.count(i))


# Global variab
if __name__ == "__main__":
    # n_cop = 21
    # n_copy = 2
    n_cheater = 5
    n_copycit = 2
    n_cop = 17

    add_agent(Cooperative, 14)
    add_agent(Cheater, 11)
    # add_agent(Detective, 1)
    # add_agent(Detective, 1)
    # add_agent(Cheater, 10)
    # add_agent(Detective, 12)

    reward = 1
    PlayGame1(6, reward, 1)
    # plot_agents2()
