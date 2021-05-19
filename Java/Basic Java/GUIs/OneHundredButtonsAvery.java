/**************************************************************
* Title: 100 buttons
* Author: Brogan Avery
* Created: 2019
***************************************************************/
import javax.swing.JFrame;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JPanel;


public class OneHundredButtonsAvery {
	public static void main(String[] args) {
	
		JFrame frame = new JFrame();
		
		JPanel panel = new JPanel(); 
		
		String labelText = "Brogan Avery";
		JLabel label = new JLabel(labelText);
		
		panel.add(label);
		
		for(int i= 1; i<101; i++) {
		String buttonText = String.valueOf(i);
		JButton button = new JButton(buttonText);
		
		panel.add(button); 
		}
		
		//add panel to frame at the end of formatting it
		frame.add(panel);
		
		final int FRAME_WIDTH = 600; 
		final int FRAME_HEIGHT = 700; 
		frame.setSize(FRAME_WIDTH, FRAME_HEIGHT);
		frame.setTitle("100 Buttons");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setVisible(true);
	}
}
