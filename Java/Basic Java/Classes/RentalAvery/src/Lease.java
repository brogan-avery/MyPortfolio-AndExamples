//Brogan Avery
import java.time.LocalDateTime;

public class Lease {
private Rental rental;
private LocalDateTime leaseStart;
private LocalDateTime leaseEnd;
private Renter renter;

//constructors
public Lease() {
	super();
}

public Lease(Rental rental, LocalDateTime leaseStart, LocalDateTime leaseEnd, Renter renter) {
	super();
	this.rental = rental;
	this.leaseStart = leaseStart;
	this.leaseEnd = leaseEnd;
	this.renter = renter;
}

public Rental getRental() {
	return rental;
}

public LocalDateTime getLeaseStart() {
	return leaseStart;
}

public LocalDateTime getLeaseEnd() {
	return leaseEnd;
}

public Renter getRenter() {
	return renter;
}

public void setRental(Rental rental) {
	this.rental = rental;
}

public void setLeaseStart(LocalDateTime leaseStart) {
	this.leaseStart = leaseStart;
}

public void setLeaseEnd(LocalDateTime leaseEnd) {
	this.leaseEnd = leaseEnd;
}

public void setRenter(Renter renter) {
	this.renter = renter;
}
//methods
@Override
public String toString() {
	return "Lease [rental=" + rental + ", leaseStart=" + leaseStart + ", leaseEnd=" + leaseEnd + ", renter=" + renter
			+ "]";
}


}
