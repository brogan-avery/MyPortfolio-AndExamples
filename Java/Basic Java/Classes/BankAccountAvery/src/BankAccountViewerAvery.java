
//Brogan Avery
import javax.swing.JFrame;
import javax.swing.JPanel;

public class BankAccountViewerAvery extends JFrame {
	public static void main(String[] args) {
		double initBal = 500;
		BankAccount newAccount = new BankAccount(initBal);

//frame
		// 1. construct frame object
		JFrame frame = new JFrame();
		
		JPanel panel = new BankAccountPanel(newAccount); // makes the panel object
		frame.add(panel);

		// 2. set frame size
		final int FRAME_WIDTH = 400;
		final int FRAME_HEIGHT = 400;
		frame.setSize(FRAME_WIDTH, FRAME_HEIGHT);

		// 3.title
		frame.setTitle("Bank Account");

		// 4.set close
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		
		// 5.make visible
		frame.setVisible(true);
	}
}
