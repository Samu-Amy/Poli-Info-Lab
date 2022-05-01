class Ticket:

    def __init__(self, name: str, number: int) -> None:
        self._name = name
        self._number = number

    def get_queue_pos(self) -> int:
        return self._number

    def __repr__(self) -> str:
        return f"{self._name}: {self._number}"

    def __lt__(self, other) -> bool:
        return self.get_queue_pos() < other.get_queue_pos()

class PriorityTicket(Ticket):

    def __init__(self, name: str, number: int, priority: int) -> None:
        super().__init__(name, number)
        self._priority = priority

    def get_queue_pos(self) -> int:
        return self._number - self._priority * 10

    def __repr__(self):
        return super().__repr__() + f", {self._priority}"


def main():

    ticket1 = Ticket("Alberto1", 5)
    ticket2 = Ticket("Alberto2", 2)
    ticket3 = Ticket("Alberto3", 10)
    ticket4 = Ticket("Alberto4", 8)
    ticket5 = Ticket("Alberto5", 4)

    pTicket1 = PriorityTicket("Gianni1", 3, 2)
    pTicket2 = PriorityTicket("Gianni2", 5, 4)
    pTicket3 = PriorityTicket("Gianni3", 2, 1)
    pTicket4 = PriorityTicket("Gianni4", 2, 3)
    pTicket5 = PriorityTicket("Gianni5", 10, 5)

    tickets = [ticket3, ticket2, pTicket2, ticket4, pTicket5, ticket1, pTicket1, pTicket3, ticket5, pTicket4]

    for ticket in tickets:
        print(ticket)

    print()
    tickets.sort()

    for ticket in tickets:
        print(ticket)


main()
