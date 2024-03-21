from matplotlib.ticker import MaxNLocator
import numpy as np
import matplotlib.pyplot as plt
# both Colab, one colab one not, both not
Points = [(1, 1), (1, 0), (0, 1), (0, 0)]

# TODO : for randomness, we need to call a rand function , if that happend we need to change the 1 to 0
# TODO : after each round , n players with the lowest points will removed and the agents with highest point will replace them
Agents = []

Tourn = 0

agent_changes = {}


def initial_counts():
    """
    Initializing a Dictionary of keys(agent names) and values(number of agents after playing a round of tournament)
    """
    agents_name_list = [type(agent).__name__ for agent in Agents]
    for agent_name in list(set(agents_name_list)):
        agent_changes[agent_name] = []


def PlayGame(agent1, agent2, round, reward):
    for _ in range(round):
        ag1 = agent1.take_action()
        ag2 = agent2.take_action()
        if ag1 == 1 and ag2 == 1:
            agent1.points += reward
            agent2.points += reward
        if ag1 == 0 and ag2 == 0:
            pass
        if ag1 == 1 and ag2 == 0:
            agent1.points += reward
            agent2.points -= reward
        if ag1 == 0 and ag2 == 1:
            agent1.points -= reward
            agent2.points += reward
    print(f"AGENT 1 : {agent1.points}")
    print(f"AGENT 2 : {agent2.points}")


def PlayGame1(round, reward, del_num):
    global Agents, Tourn
    """
    round means, number of round each two agent play against each other
    del_num : number of players to delete after each torunoment match
    """
    initial_counts()
    while (Tourn <= 20):
        # TODO the round should not be here i guess , because now, it plays one round with each agent
        for i in range(len(Agents)):
            agent1 = Agents[i]
            for j in range(i+1, len(Agents)):
                agent2 = Agents[j]
                if (type(agent1).__name__ == "CopyCat" or type(agent1).__name__ == "CopyKitten"):
                    agent1.memory = []
                if (type(agent2).__name__ == "CopyCat" or type(agent2).__name__ == "CopyKitten"):
                    agent2.memory = []
                for _ in range(round):
                    ag1 = agent1.take_action()
                    ag2 = agent2.take_action()
                    if (type(agent1).__name__ == "CopyCat" or type(agent1).__name__ == "CopyKitten"):
                        agent1.memory.append(ag2)
                    if (type(agent2).__name__ == "CopyCat" or type(agent2).__name__ == "CopyKitten"):
                        agent2.memory.append(ag1)
                    if ag1 == 1 and ag2 == 1:

                        agent1.points += reward
                        agent2.points += reward
                    elif ag1 == 0 and ag2 == 0:
                        pass
                    elif ag1 == 1 and ag2 == 0:
                        agent1.points -= reward
                        agent2.points += reward
                    elif ag1 == 0 and ag2 == 1:
                        agent1.points += reward
                        agent2.points -= reward
        # Scores = sorted([agent.points for agent in Agents], reverse=True)# Removing the agent with the least point
        # Agents[del_num:]
        for i in range(len(Agents)):
            print(
                f"{type(Agents[i]).__name__} has {Agents[i].points} Point")
        print("_____________")
        get_agents_count()
        update_agents(del_num)
        Tourn += 1


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


class Coperative:
    def __init__(self) -> None:
        self.points = 0

    def take_action(self):
        return 1  # 1 means Coperate


class Cheater:
    def __init__(self) -> None:
        self.points = 0

    def take_action(self):
        return 0  # 0 means no coperate


class Random:
    def __init__(self) -> None:
        self.points = 0

    def take_action(self):
        if np.random.rand() > 0.5:
            return 1
        else:
            return 0


class CopyKitten:
    def __init__(self) -> None:
        self.points = 0
        self.memory = []

    def take_action(self):
        if len(self.memory) == 0:
            return 1  # coperates at first
        if len(self.memory) > 1:
            if self.memory[-1] == 0 and self.memory[-2] == 0:
                return 0  # the enemy didn't coperated two time in a row
            else:
                return 1
        else:
            return 1


class CopyCat:
    def __init__(self) -> None:
        self.points = 0
        self.memory = []

    def take_action(self):
        if len(self.memory) == 0:

            return 1  # first coperates
        elif (self.memory[-1] == 0):
            return 0
        else:
            return 1


def add_agent(agent, number):
    global Agents
    for _ in range(number):
        new_instance = agent()
        Agents.append(new_instance)


def plot_agents(agent_number, bins, agent_name):
    num_bins = bins
    # for i in agent_changes
# Increase figure size
    plt.figure(figsize=(10, 6))

    # Plotting
    plt.plot(range(len(agent_number)), agent_number, color='blue')
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.title(f'Number of {agent_name}')
    plt.xticks(range(0, len(agent_number), len(agent_number) // num_bins),
               [' {}'.format(i) for i in range(
                   1, len(agent_number) + 1, len(agent_number) // num_bins)],
               rotation=45)
    plt.tight_layout()  # Adjust layout to prevent overlap
    plt.show()


def plot_agents2():
    global agent_changes

    colors = ['blue', 'green', 'red', 'orange',
              'purple']  # Define a list of colors

    # Loop through agent_changes dictionary and plot each agent's data with a different color
    for i, (key, value) in enumerate(agent_changes.items()):
        plt.plot(range(len(value)), value, color=colors[i % len(
            colors)], label=key)  # Add label=key for legend

    plt.xticks(range(0, len(value), len(value) // 5),
               ['{}'.format(i)
                for i in range(1, len(value) + 1, len(value) // 5)],
               rotation=45)

    plt.xlabel('Number of iteration')
    plt.ylabel('Count')
    plt.tight_layout()  # Adjust layout to prevent overlap

    plt.legend()  # Add legend

    # Set y-axis tick locator to display only integer values
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))

    plt.show()


def get_agents_count():
    global agent_changes
    agents_name_list = [type(agent).__name__ for agent in Agents]
    for i in list(set([type(agent).__name__ for agent in Agents])):
        print(f"Count {i} is {agents_name_list.count(i)}")
        agent_changes[i].append(agents_name_list.count(i))


if __name__ == "__main__":
    n_cop = 21
    n_copy = 2
    n_cheater = 5
    n_copycit = 3
    n_cop = 17

    add_agent(CopyKitten, n_copycit)
    add_agent(Cheater, n_cheater)
    add_agent(Coperative, n_cop)

    reward = 1
    PlayGame1(6, reward, 1)
    # plot_agents(agent_changes['CopyKitten'], 5, "CopyKitten")
    # plot_agents(agent_changes['Cheater'], 5, "Cheater")
    # plot_agents(agent_changes['Coperative'], 5, "Coperative")
    # plot_agents2()
    print("Hello")
