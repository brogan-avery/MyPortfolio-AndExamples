//Brogan Avery

import javax.swing.JPanel;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JTextField;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class BankAccountPanel extends JPanel {

	BankAccount account;

	// object variables
	private JLabel amount = new JLabel("Amount: ");

	final int BOXSIZE = 6;
	private JTextField textBox = new JTextField(BOXSIZE);
	private JButton deposit = new JButton("Deposite");
	private JButton withdraw = new JButton("Withdraw");
	private JLabel balance = new JLabel();

	// constructor
	public BankAccountPanel(BankAccount b) {
		account = b;
		balance.setText("Balance = $"+ account.getBalance());
		DepositClickListener d = new DepositClickListener();
		deposit.addActionListener(d); 

		WithdrawClickListener w = new WithdrawClickListener();
		withdraw.addActionListener(w);

		add(balance);
		add(amount);
		add(textBox);
		add(deposit); // adding buttons to panel
		add(withdraw);


	}

//inner classes
	class DepositClickListener implements ActionListener {

		@Override
		public void actionPerformed(ActionEvent e) {
			double depositAmount = 0;
			String str = textBox.getText();
			try {
				depositAmount = Double.parseDouble(str);
			}
			catch(Exception E) {
				textBox.setText("Invalid Entry");

			}

			finally {
				account.deposit(depositAmount);
			    }
			balance.setText("Balance=$" + account.getBalance());
		}
	}

	class WithdrawClickListener implements ActionListener {

		@Override
		public void actionPerformed(ActionEvent e) {
			double withdrawAmount = 0;
			String str = textBox.getText();
			try {
				withdrawAmount = Double.parseDouble(str);
			}
			catch(Exception E) {
				textBox.setText("Invalid Entry");

			}
			finally {
				account.withdraw(withdrawAmount);
			    }
			balance.setText("Balance=$" + account.getBalance());
		}
	}

}
