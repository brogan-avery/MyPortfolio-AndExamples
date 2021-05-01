//Brogan Avery
package controller;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class addItemsToListServlet
 */
@WebServlet("/addDogEntriesToListServlet")
public class addDogEntriesToListServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public addDogEntriesToListServlet() {
        super();
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		DogEntryHelper helperObj = new DogEntryHelper();
		
		request.setAttribute("allDogEntries", helperObj.showAllDogEntries());
					
		if(helperObj.showAllDogEntries().isEmpty()){
				request.setAttribute("allItems", " ");
		}
		
		getServletContext().getRequestDispatcher("/new-list.jsp").forward(request, response);

	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
