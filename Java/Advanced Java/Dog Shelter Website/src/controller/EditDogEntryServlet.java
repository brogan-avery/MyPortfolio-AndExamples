package controller;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import model.DogEntry;

/**
 * Servlet implementation class editItemServlet
 */
@WebServlet("/editDogEntryServlet")
public class EditDogEntryServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public EditDogEntryServlet() {
        super();
    }

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		DogEntryHelper helperObj = new DogEntryHelper();
		
		String name = request.getParameter("name");
		String breed = request.getParameter("breed");
		String ageStr = request.getParameter("age");
		int age = Integer.parseInt(ageStr);
		Integer tempId = Integer.parseInt(request.getParameter("id"));
				
		DogEntry dogEntryToUpdate = helperObj.searchForDogEntryById(tempId);
		dogEntryToUpdate.setBreed(breed);
		dogEntryToUpdate.setName(name);
		dogEntryToUpdate.setAge(age);
				
		helperObj.updateDogEntry(dogEntryToUpdate);

		getServletContext().getRequestDispatcher("/viewAllDogEntriesServlet").forward(request, response);


	}

}
