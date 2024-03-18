from Agents import *
Agents = []
n_iter = 1


def PlayGame(round, reward):
    global Agents, n_iter
    """
    round : number of rounds each two agent play against each other
    n_iter : number of iterations 
    """
    while (n_iter <= 1):
        # TODO the round should not be here i guess , because now, it plays one round with each agent
        for i in range(len(Agents)):
            agent1 = Agents[i]
            for j in range(i+1, len(Agents)):
                agent2 = Agents[j]
                for _ in range(round):
                    ag1 = agent1.take_action()
                    ag2 = agent2.take_action()
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
        n_iter += 1


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
