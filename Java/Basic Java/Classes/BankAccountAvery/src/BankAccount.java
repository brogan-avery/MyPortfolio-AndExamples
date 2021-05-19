//Brogan Avery
public class BankAccount {

	private double balance;

//constructor

	public BankAccount(double balance) {
		super();
		this.balance = balance;
	}

//getter

	public double getBalance() {
		return balance;
	}

//setter
	public void setBalance(double balance) {
		this.balance = balance;
	}

//to string
	@Override
	public String toString() {
		return "BankAccount [balance=" + balance + "]";
	}

	public void deposit(double depositAmount) {
		double newBalance = this.balance + depositAmount;
		setBalance(newBalance);
	}

	public void withdraw(double withdrawAmount) {
		double newBalance = this.balance - withdrawAmount;
		setBalance(newBalance);
	}

}
