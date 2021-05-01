package mainPackage.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;

import mainPackage.beans.Location;
import mainPackage.repository.LocationRepository;

@Controller
public class WebController {
	@Autowired
	LocationRepository repo;
	
	@GetMapping({"/","/viewAll"})
	public String viewAllLocations(Model model) {
		if(repo.findAll().isEmpty()) {
			return addNewLocation(model);
		}
		model.addAttribute("locations", repo.findAll());
		return "results";
	}	
	
	@GetMapping("/addLocation")
	public String addNewLocation(Model model) {
		Location loc = new Location();
		model.addAttribute("newLocation", loc);
		return "input";
	}
	
	@PostMapping("/addLocation")
	public String addNewLocation(@ModelAttribute Location loc, Model model) {
		repo.save(loc);
		return viewAllLocations(model);
	}
	
	@GetMapping("/edit/{id}")
	public String showUpdateLocation(@PathVariable("id") long id, Model model) {
		Location loc = repo.findById(id).orElse(null);
		model.addAttribute("newLocation", loc);
		return "input";
	}
	
	@PostMapping("/update/{id}")
	public String reviseLocation(Location loc, Model model) {
		repo.save(loc);
		return viewAllLocations(model);
	}
	
	@GetMapping("/delete/{id}")
	public String deleteLocation(@PathVariable("id") long id, Model model) {
		Location loc = repo.findById(id).orElse(null);
		repo.delete(loc);
		return viewAllLocations(model);
	}
}
