package cards;
//Brogan Avery
public class CreditCard extends Card{
//vars	
	private String cardNumber;
	private String cvv;
	
//constructors
	public CreditCard(){
		setCardNumber(null);
		setCvv(null);
	}
	
	public CreditCard(String name, String cardNumber, String cvv){
		super(name);
		setCardNumber(cardNumber);
		setCvv(cvv);
	}
//getters
	public String getCardNumber() {
		return cardNumber;
	}

	public String getCvv() {
		return cvv;
	}
//setters
	public void setCardNumber(String cardNumber) {
		this.cardNumber = cardNumber;
	}

	public void setCvv(String cvv) {
		this.cvv = cvv;
	}
	
//methods
	public String format() {
		return super.format() + "\n card number: " + cardNumber + "\n CVV: " + cvv;
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = super.hashCode();
		result = prime * result + ((cardNumber == null) ? 0 : cardNumber.hashCode());
		result = prime * result + ((cvv == null) ? 0 : cvv.hashCode());
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (!super.equals(obj))
			return false;
		if (getClass() != obj.getClass())
			return false;
		CreditCard other = (CreditCard) obj;
		if (cardNumber == null) {
			if (other.cardNumber != null)
				return false;
		} else if (!cardNumber.equals(other.cardNumber))
			return false;
		if (cvv == null) {
			if (other.cvv != null)
				return false;
		} else if (!cvv.equals(other.cvv))
			return false;
		return true;
	}
	
	
}
