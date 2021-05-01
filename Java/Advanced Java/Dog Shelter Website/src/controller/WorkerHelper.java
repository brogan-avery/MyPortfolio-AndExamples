//Brogan Avery
package controller;

import java.util.List;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.NoResultException;
import javax.persistence.Persistence;
import javax.persistence.TypedQuery;

import model.Worker;

public class WorkerHelper {
	static EntityManagerFactory emfactory = Persistence.createEntityManagerFactory("DogShelterWebsite");

	public void insertWorker(Worker worker) {
		EntityManager em = emfactory.createEntityManager();
		em.getTransaction().begin();
		em.persist(worker);
		em.getTransaction().commit();
		em.close();
	}

	public List<Worker> showAllWorkers() {
		EntityManager em = emfactory.createEntityManager();
		List<Worker> allWorkers = em.createQuery("SELECT w FROM Worker w").getResultList();
		return allWorkers;
	}
// can not have multiple people with same name 
	public Worker findWorker(String nameToLookUp) {

		EntityManager em = emfactory.createEntityManager();
		em.getTransaction().begin();
		TypedQuery<Worker> typedQuery = em.createQuery("select w from Worker w where w.workerName = :selectedName",
				Worker.class);
		typedQuery.setParameter("selectedName", nameToLookUp);
		Worker foundWorker;
		try {
			foundWorker = typedQuery.getSingleResult();
		} catch (NoResultException ex) {
			foundWorker = new Worker(nameToLookUp);
		}
		em.close();

		return foundWorker;
	}
}

