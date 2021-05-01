//Brogan Avery
package model;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name="worker")
public class Worker {
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(name="WORKER_ID")
	private int id;
	@Column(name="WORKER_NAME")
	private String workerName;
	
	
	public Worker() {
		super();
		// TODO Auto-generated constructor stub
	}
	public Worker(int id, String workerName) {
		super();
		this.id = id;
		this.workerName = workerName;
	}
	
	public Worker(String workerName) {
		super();
		this.workerName = workerName;
	}
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getWorkerName() {
		return workerName;
	}
	public void setWorkerName(String workerName) {
		this.workerName = workerName;
	}
	@Override
	public String toString() {
		return "Worker [id=" + id + ", workerName=" + workerName + "]";
	}

}
