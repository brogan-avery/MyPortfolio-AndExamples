//Brogan Avery
package moneyclip;
import cards.Card;
public class MoneyClip {
//vars
	public Card card1;
	public Card card2;

//methods
	public void addCard(Card cardn) {
		 if (card1 == null) {
			 card1 = cardn;
		 }
		 else if (card2 == null) {
			 card2 = cardn;
		 }
	}
	
	public  String formatCards() {
		return  "[" + card1.format() + "\n|\n" + card2.format() + "]";
	}
	
	public int getExpiredCardCount() {
		int count = 0;
		if (card1.isExpired() == true) {
			count = count + 1;
		}
		
		if (card2.isExpired() == true) {
			count = count + 1;
		}
		
		return count;
	}
}
