package bad;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class TicketOffice {
    private Long amount;
    private List<Ticket> tickets = new ArrayList<>();

    TicketOffice(Long amount, Ticket ... tickets) {

        this.amount = amount;
        this.tickets.addAll(Arrays.asList(tickets));
    }

    public Ticket getTicket() {
        return this.tickets.remove(0);
    }

    public void minusAmount(Long amount) {
        this.amount -= amount;
    }

    public void plusAmount(Long amount) {
        this.amount += amount;
    }

}
