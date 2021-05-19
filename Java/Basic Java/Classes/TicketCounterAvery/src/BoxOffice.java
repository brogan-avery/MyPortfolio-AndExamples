//Brogan Avery
public class BoxOffice {
	private int ticketsLeft = 28;
	private int ticketsSold;
	private int buyerCount; //used to get total number of sales transactions made(total buyer count, not total people attending)
	

	
//constructor
public BoxOffice() {
	setTicketsLeft(ticketsLeft);
	setBuyerCount(buyerCount);
}
//getters

public int getTicketsLeft() {
	return ticketsLeft;
}

public int getTicketsSold() { //per each transaction
	return ticketsSold;
}


public int getBuyerCount() { // will be used to get total buyer count
	return buyerCount;
}

//setters

public void setTicketsLeft(int ticketsLeft) {
	this.ticketsLeft = ticketsLeft;
}

public void setBuyerCount(int buyerCount) { 
	this.buyerCount = buyerCount;
}

//methods

public String attemptSale(int ticketsRequested,int ticketsLeft,int buyerCount) {
	String returnStr = null;
	
	if (ticketsRequested > 4 || ticketsRequested < 1) {
		 returnStr = "You may not purchase more than 4 tickets in one transaction.";
	}
	
	else if (ticketsRequested > ticketsLeft) {
		returnStr = "Sorry, we only have " + ticketsLeft + " ticket(s) available";
	}
	
	else {
		returnStr = makeSale(ticketsRequested,ticketsLeft,buyerCount);
	}
	
	
	return returnStr;
}

public String makeSale(int ticketsRequested, int ticketsLeft, int buyerCount) {
	
	int ticketPrice = 5;
	ticketsSold = ticketsRequested;
	ticketsLeft = ticketsLeft - ticketsSold;
	setTicketsLeft(ticketsLeft);
	buyerCount = buyerCount +1;
	setBuyerCount(buyerCount);
	
	String receipt = ("############# \n__The Playhouse__\n" + "thank you for your purchase of: " + ticketsSold + " ticket(s).\n Price per ticket: $" + ticketPrice + "\n Total price: $" + (ticketPrice * ticketsSold) +"\n Reciept number: " + buyerCount +"\n############# ");	
	
	return receipt;
}
}//Class end
