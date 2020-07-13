from queue import PriorityQueue
from threading import Thread


def queue_ticket(ticket, prio, tickets):
    levels = {"low": 3, "medium": 2, "high": 1}

    tickets.put((levels[prio], ticket))


def get_ticket(tickets):
    print(tickets.get())


if __name__ == "__main__":
    tickets = PriorityQueue()

    while True:
        prompt = input("Problem eingeben (e) oder lösen (l)?")
        if prompt == "e":
            problem = input("Was ist das Problem?")
            prio = input("Wie wichtig? (low, medium, high)")
            p1 = Thread(target=queue_ticket, args=[problem, prio, tickets])
            p1.start()
        elif prompt == "l":
            l1 = Thread(target=get_ticket, args=[tickets])
            l1.start()

    # queue_ticket("PC funktioniert nicht", "medium", tickets)
    # queue_ticket("Haus brennt", "high", tickets)
    # queue_ticket("Katze ist weggelaufen", "low", tickets)
    # queue_ticket("Katze brennt", "high", tickets)

    # print(get_ticket(tickets))
    # print(get_ticket(tickets))
    # print(get_ticket(tickets))
    # print(get_ticket(tickets))
