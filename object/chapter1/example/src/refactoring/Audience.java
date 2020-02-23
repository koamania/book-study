package refactoring;

class Audience {

    private Bag bag;

    Audience(Bag bag) {
        this.bag = bag;
    }

    Long buy(Ticket ticket) {
        return this.bag.hold(ticket);
    }
}
