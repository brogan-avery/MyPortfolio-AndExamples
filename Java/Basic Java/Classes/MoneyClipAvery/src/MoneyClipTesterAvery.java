//Brogan Avery
import cards.*;
import moneyclip.MoneyClip;
import java.time.LocalDate;
public class MoneyClipTesterAvery {

	public static void main(String[] args) {
		 DriverLicense dl = new DriverLicense("Brogan", "AF346V2S", LocalDate.of(2025, 1, 12));
		 CreditCard Chase = new CreditCard("Brogan","1234 2345 3456 4567", "361");
		 DMACCOneCard DMACC = new DMACCOneCard("Brogan" , "165345789");
		 DriverLicense otherDl = new DriverLicense("Brogan", "AF346V2S", LocalDate.of(2019, 1, 12));
		 DMACCOneCard mine = new DMACCOneCard("Brogan", "345sdf798");
		 DMACCOneCard yours = new DMACCOneCard("Brogan", "345sdf798");
		 CreditCard Master = new CreditCard("Brogan","1111 2222 3333 4444", "234");
		 CreditCard Visa = new CreditCard("Brogan","5432 7654 9876 0987", "789");
		 DMACCOneCard someonesDMACC = new DMACCOneCard("Someone" , "1234565352");
		 DriverLicense someonesDl = new DriverLicense("someone", "GDH234HWK", LocalDate.of(2023, 4, 16));
		 DriverLicense MikeDl = new DriverLicense("Mike", "CXL432IF89", LocalDate.of(2018, 9, 21));
		 CreditCard MikeCredit = new CreditCard("Mike","8877 6688 9900 7755", "098");
		 
		 MoneyClip myClip = new MoneyClip();
		 myClip.addCard(dl);
		 myClip.addCard(Chase);
		 System.out.println("__FIRST CLIP__ ");
		 System.out.print(myClip.formatCards());		
		
		 System.out.print("\n-----------\n");
		 MoneyClip myOtherClip = new MoneyClip();
		 System.out.println("__SECOND CLIP__ ");
		 myOtherClip.addCard(otherDl);
		 myOtherClip.addCard(DMACC);
		 System.out.print(myOtherClip.formatCards());
		
		 System.out.print("\n-----------\n");
		 System.out.println(myOtherClip.getExpiredCardCount() + " expired card");
		
		 System.out.print("\n-----------\n");
		 System.out.print(mine.equals(yours));
		 
		 System.out.print("\n-----------\n");
		 MoneyClip thirdClip = new MoneyClip();
		 System.out.println("__THIRD CLIP__ ");
		 thirdClip.addCard(Master);
		 thirdClip.addCard(Visa);
		 System.out.print(thirdClip.formatCards());
		 
		 System.out.print("\n-----------\n");
		 System.out.print(Master.equals(Visa));
		 
		 System.out.print("\n-----------\n");
		 MoneyClip fourthClip = new MoneyClip();
		 System.out.println("__FOURTH CLIP__ ");
		 fourthClip.addCard(someonesDMACC);
		 fourthClip.addCard(someonesDl);
		 System.out.print(fourthClip.formatCards());
		 
		 System.out.print("\n-----------\n");
		 MoneyClip fifthClip = new MoneyClip();
		 System.out.println("__FIFTH CLIP__ ");
		 fifthClip.addCard(MikeDl);
		 fifthClip.addCard(MikeCredit);
		 System.out.print(fifthClip.formatCards());
		 
		 //Card a = new Card();
	}

}
