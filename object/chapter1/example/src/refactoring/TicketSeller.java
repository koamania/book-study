package refactoring;

class TicketSeller {
    private TicketOffice ticketOffice;

    TicketSeller(TicketOffice ticketOffice) {
        this.ticketOffice = ticketOffice;
    }

    void sellTo(Audience audience) {
        Ticket ticket = this.ticketOffice.getTicket();
        audience.buy(ticket);
    }
}
