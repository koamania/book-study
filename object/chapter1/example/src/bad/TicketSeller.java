package bad;

class TicketSeller {
    private TicketOffice ticketOffice;

    TicketSeller(TicketOffice ticketOffice) {
        this.ticketOffice = ticketOffice;
    }

    TicketOffice getTicketOffice() {
        return this.ticketOffice;
    }
}
