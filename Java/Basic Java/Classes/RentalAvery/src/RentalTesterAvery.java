import java.time.LocalDateTime;
import java.util.ArrayList;
public class RentalTesterAvery {

	public static void main(String[] args) {
		House jewel111 = new House();
		jewel111.setHasYard(true);
		jewel111.setAddress("111 Jewel Dr.");
		jewel111.setBedrooms(2);
		jewel111.setBathrooms(2);
		
		System.out.println(jewel111.toString());
		
		House ruby222 = new House(1500, "222 Ruby St",1,1,true,true);
		
		System.out.println(ruby222.toString());
		
		Building theEdge = new Building("The Edge", true);
		
		Apartment theEdge112d = new Apartment(500,"112 Rose St",2,1,true, "Apt D",1, theEdge);
		
		System.out.println(theEdge112d.toString());
		
		Renter brogan = new Renter("Brogan","Avery","111-111-1111");
		Renter mike = new Renter("Mike","Jones","121-122-1441");		
		
		Lease lease1 = new Lease(theEdge112d,LocalDateTime.now(), LocalDateTime.of(2021, 4,8,17,00),brogan);
		System.out.println(lease1.toString());
		
		Lease lease2 = new Lease(ruby222,LocalDateTime.of(1999,2,3,13,00),LocalDateTime.of(2001,2,3,13,00), mike);
		System.out.println(lease2.toString());
	
		ArrayList<Lease> allLeases = new ArrayList<Lease>();
		allLeases.add(lease1);
		allLeases.add(lease2);
		System.out.println("All leases in the system:");
		for (Lease item: allLeases) {
			System.out.println(item.toString());
			System.out.println("--------");
		}
		
	}
	
	

}
