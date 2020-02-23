package bad;

class Bag {

    private Long amount;
    private Invitation invitation;
    private Ticket ticket;


    public Bag(Invitation invitation) {
        this.invitation = invitation;
    }


    public Bag(Long amount, Ticket ticket) {
        this.amount = amount;
        this.ticket = ticket;
    }


    boolean hasInvitation() {
        return this.invitation != null;
    }

    boolean hasTicket() {
        return this.ticket != null;
    }

    void setTicket(Ticket ticket) {
        this.ticket = ticket;
    }

    void minusAmount(Long amount) {
        this.amount -= amount;
    }

    void plusAmount(Long amount) {
        this.amount += amount;
    }
}
