//Brogan Avery 
import java.time.LocalDate;
import java.util.List;

import controller.ListDetailsHelper;
import controller.WorkerHelper;
import model.ListDetails;
import model.Worker;
import controller.LocalDateAttributeConverter;

public class DogShelterWebsiteTester {
	public static void main(String[] args) {
		
		Worker bill = new Worker("Bill");
		
		WorkerHelper sh = new WorkerHelper();
		
		sh.insertWorker(bill);

		ListDetailsHelper ldh = new ListDetailsHelper();
		
		ListDetails billList = new ListDetails("Bill's List", LocalDate.now(), bill);
		
		ldh.insertNewListDetails(billList);
		
		List<ListDetails> allLists = ldh.getLists();
			
		for(ListDetails a : allLists) {
				System.out.println(a.toString());
		}
	}	

}
