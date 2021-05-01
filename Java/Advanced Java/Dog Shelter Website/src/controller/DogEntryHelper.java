//Brogan Avery
package controller;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;
import javax.persistence.TypedQuery;

import java.util.List;
import model.DogEntry;

public class DogEntryHelper {
	static EntityManagerFactory emfactory = Persistence.createEntityManagerFactory("DogShelterWebsite");
	
	public void insertDogEntry(DogEntry entry) {
		EntityManager em = emfactory.createEntityManager();
		em.getTransaction().begin();
		em.persist(entry);
		em.getTransaction().commit();
		em.close();
		
	}
	
	public List<DogEntry> showAllDogEntries(){
		EntityManager em = emfactory.createEntityManager();
		List<DogEntry> allEntries = em.createQuery("SELECT i FROM DogEntry i").getResultList();
		return	allEntries;
	}
	
	public void	deleteDogEntry(DogEntry	toDelete){
		EntityManager em = emfactory.createEntityManager();
		em.getTransaction().begin();
		TypedQuery<DogEntry> typedQuery	= em.createQuery("select row from DogEntry row	where row.breed = :selectedBreed and row.name = :selectedName  and row.age = :selectedAge", DogEntry.class);
	
		//Substitute parameter	with actual	data from the toDelete item
		typedQuery.setParameter("selectedBreed", toDelete.getBreed());
		typedQuery.setParameter("selectedName",	toDelete.getName());
		typedQuery.setParameter("selectedAge",	toDelete.getAge());
		
		//we only want one result
		typedQuery.setMaxResults(1);
		
		//get	the	result	and	save it	into a new list item
		DogEntry result	= typedQuery.getSingleResult();
		
		//remove it
		em.remove(result);
		em.getTransaction().commit();
		em.close();
	
	}

	public DogEntry searchForDogEntryById(int idToEdit) {
		EntityManager em = emfactory.createEntityManager();
		em.getTransaction().begin();
		DogEntry found = em.find(DogEntry.class, idToEdit);
		em.close();
		return found;
	}

	public void updateDogEntry(DogEntry toEdit) {
		EntityManager em =	emfactory.createEntityManager();
		em.getTransaction().begin();
		em.merge(toEdit);
		em.getTransaction().commit();
		em.close();
	}

	public List<DogEntry> searchForDogEntryByBreed(String breed) {
		EntityManager em =	emfactory.createEntityManager();
		em.getTransaction().begin();
		TypedQuery<DogEntry> typedQuery	= em.createQuery("select row from DogEntry row where row.breed	= :selectedBreed", DogEntry.class);
		typedQuery.setParameter("selectedBreed", breed);
		List<DogEntry> foundDogEntry = typedQuery.getResultList();
		em.close();
		return foundDogEntry;
	}

	public List<DogEntry> searchForDogEntryByName(String name) {
		EntityManager em =	emfactory.createEntityManager();
		em.getTransaction().begin();
		TypedQuery<DogEntry> typedQuery	= em.createQuery("select row from DogEntry row where row.name = :selectedName", DogEntry.class);
		typedQuery.setParameter("selectedName",	name);
		List<DogEntry> foundDogEntry =	typedQuery.getResultList();
		em.close();
		return foundDogEntry;
	}
	
	public List<DogEntry> searchForDogEntryByAge(int age) {
		EntityManager em =	emfactory.createEntityManager();
		em.getTransaction().begin();
		TypedQuery<DogEntry> typedQuery	= em.createQuery("select row from DogEntry row where row.age = :selectedAge", DogEntry.class);
		typedQuery.setParameter("selectedAge", age);
		List<DogEntry> foundDogEntry =	typedQuery.getResultList();
		em.close();
		return	foundDogEntry;
	}
	
	public	void cleanUp(){
		emfactory.close();
		}
}

