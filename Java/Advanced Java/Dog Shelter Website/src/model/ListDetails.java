//Brogan Avery
package model;

import java.time.LocalDate;
import java.util.List;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.JoinTable;
import javax.persistence.ManyToOne;
import javax.persistence.OneToMany;
import javax.persistence.Table;

@Entity
@Table(name="list_details") // each list is for a specific breed. all entries on that list are only of the one breed
public class ListDetails {
	
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(name="LIST_ID")
	private int id;
	@Column(name="LIST_NAME")
	private String listName;
	@Column(name="VAC_DATE") // date all the dogs for that list need to get their vaccinations
	private LocalDate vacDate;
	@ManyToOne (cascade=CascadeType.PERSIST)
	@JoinColumn(name="WORKER_ID") // shelter employee that has all the dogs of the breed that the list is for under their care
	private Worker worker;
	
	@OneToMany(cascade=CascadeType.MERGE, fetch=FetchType.EAGER)
	@JoinTable
	  (
	      name="dog_entries_on_list",
	      joinColumns={ @JoinColumn(name="LIST_ID", referencedColumnName="LIST_ID") },
	      inverseJoinColumns={ @JoinColumn(name="DOG_ENTRY_ID", referencedColumnName="ID", unique=true) }
	  )
    
	private List<DogEntry> listOfDogEntries;

	
	public ListDetails() {
		super();
	}
	

	public ListDetails(int id, String listName, LocalDate vacDate, Worker worker, List<DogEntry> listOfDogEntries) {
		super();
		this.id = id;
		this.listName = listName;
		this.vacDate = vacDate;
		this.worker = worker;
		this.listOfDogEntries = listOfDogEntries;
	}

	public ListDetails(String listName, LocalDate vacDate, Worker worker, List<DogEntry> listOfDogEntries) {
		super();
		this.listName = listName;
		this.vacDate = vacDate;
		this.worker = worker;
		this.listOfDogEntries = listOfDogEntries;
	}

	public ListDetails(String listName, LocalDate vacDate, Worker worker) {
		super();
		this.listName = listName;
		this.vacDate = vacDate;
		this.worker = worker;
	}


	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getListName() {
		return listName;
	}
	public void setListName(String listName) {
		this.listName = listName;
	}
	public LocalDate getVacDate() {
		return vacDate;
	}
	public void setVacDate(LocalDate vacDate) {
		this.vacDate = vacDate;
	}
	public Worker getWorker() {
		return worker;
	}
	public void setWorker(Worker worker) {
		this.worker = worker;
	}


	public List<DogEntry> getListOfDogEntries() {
		return listOfDogEntries;
	}


	public void setListOfDogEntries(List<DogEntry> listOfDogEntries) {
		this.listOfDogEntries = listOfDogEntries;
	}


	@Override
	public String toString() {
		return "ShoppingListDetails [id=" + id + ", ListName=" + listName + ", vacDate=" + vacDate + ", worker="
				+ worker + ", listOfDogEntries=" + listOfDogEntries + "]";
	}


	

	
}
