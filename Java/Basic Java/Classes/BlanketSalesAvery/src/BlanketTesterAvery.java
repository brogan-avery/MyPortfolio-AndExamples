//Brogan Avery
import java.util.ArrayList;

import model.Blanket;
import model.ElectricBlanket;
public class BlanketTesterAvery {

	public static void main(String[] args) {
		Blanket cashmereKing = new Blanket("king","red","cashmere");
		//Blanket impossibleBlanket = new Blanket("twwin","red","cashmere"); <-- Tries to set size to "twwin" but the only options it can take are the literals "twin","king", or "queen". Since it isn't one of those, it throws a custom error telling the user that it is not an option.
		Blanket firstBlanket = new Blanket("queen","yellow","wool");
		Blanket secondBlanket = new Blanket("twin","green","chenille");
		ElectricBlanket thirdBlanket = new ElectricBlanket();
		ElectricBlanket fourthBlanket = new ElectricBlanket("king","orange","chenille",2,true);
		
		ArrayList<Blanket> BlanketsOrdered = new ArrayList<Blanket>();
		BlanketsOrdered.add(cashmereKing);
		BlanketsOrdered.add(firstBlanket);
		BlanketsOrdered.add(secondBlanket);
		BlanketsOrdered.add(thirdBlanket);
		BlanketsOrdered.add(fourthBlanket);
		
		System.out.println(cashmereKing);
		System.out.println(cashmereKing.featureReport());
		System.out.println(firstBlanket.featureReport());
		System.out.println(secondBlanket.featureReport());
		System.out.println(thirdBlanket.featureReport());
		System.out.println(fourthBlanket.featureReport());
		System.out.println("____Blankets under $100____");
		for (Blanket object : BlanketsOrdered) {
			if (object.getPrice() <= 100) {
				System.out.println(object.featureReport());
			}
		}
		

	}

}
