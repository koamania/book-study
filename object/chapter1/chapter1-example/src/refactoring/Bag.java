package refactoring;

class Bag {

    private Long amount;
    private Invitation invitation;
    private Ticket ticket;


    Bag(Invitation invitation) {
        this.invitation = invitation;
    }


    Bag(Long amount, Ticket ticket) {
        this.amount = amount;
        this.ticket = ticket;
    }


    private boolean hasInvitation() {
        return this.invitation != null;
    }

    private void minusAmount(Long amount) {
        this.amount -= amount;
    }

    public Long hold(Ticket ticket) {
        if(hasInvitation()) {
            this.ticket = ticket;
            return 0L;
        } else {
            Long fee = ticket.getFee();
            this.minusAmount(fee);
            return fee;
        }
    }
}
