
//Brogan Avery
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class ButtonFrame1 extends JFrame {

	private static final int FRAME_WIDTH = 300;
	private static final int FRAME_HEIGHT = 150;

	public ButtonFrame1() {
		createComponents();
		setSize(FRAME_WIDTH, FRAME_HEIGHT);
	}

	private void createComponents() {

		JButton buttonA = new JButton("A"); //makes new buttons
		JButton buttonB = new JButton("B");
		JPanel panel = new JPanel();
		
		panel.add(buttonA);   //adds them to panel
		panel.add(buttonB);                
		
		add(panel);       // add panel to frame
		
		ActionListener listenerA = new ClickListener(); //makes listener for a
		buttonA.addActionListener(listenerA);           //when a is clicked does listener thing
		
		ActionListener listenerB = new ClickListener(); //when b is clicked
		buttonB.addActionListener(listenerB);
	}
}