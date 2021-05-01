package controller;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import model.DogEntry;

/**
 * Servlet implementation class AddItemServlet
 */
@WebServlet("/addDogEntryServlet")
public class AddDogEntryServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public AddDogEntryServlet() {
        super();
    }

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String name = request.getParameter("name");
		String breed = request.getParameter("breed");
		String ageStr = request.getParameter("age");
		
		int age = Integer.parseInt(ageStr);
		
		DogEntry dogEntryObj = new DogEntry(breed, name, age);
		DogEntryHelper helperObj = new DogEntryHelper();
		helperObj.insertDogEntry(dogEntryObj);
		getServletContext().getRequestDispatcher("/index.html").forward(request, response);
	}

}
