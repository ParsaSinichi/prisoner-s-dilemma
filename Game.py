from Agents import *
Agents = []
n_iter = 1


def PlayGame(round, reward, del_num):
    global Agents, n_iter
    """
    round means, number of round each two agent play against each other
    n_iter : number of iterations 
    """
    while (n_iter <= 50):
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
        for i in range(len(Agents)):
            print(
                f"{type(Agents[i]).__name__} has {Agents[i].points} Point")
        print("_____________")

        update_agents(del_num)
        n_iter += 1


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


def add_agent(agent, number):
    global Agents
    for _ in range(number):
        new_instance = agent()
        Agents.append(new_instance)


if __name__ == "__main__":
    n_coop = 21

    n_cheater = 4
    add_agent(Cheater, n_cheater)
    add_agent(Coperative, n_coop)
    reward = 1
    rounds = 6
    PlayGame(rounds, reward)
