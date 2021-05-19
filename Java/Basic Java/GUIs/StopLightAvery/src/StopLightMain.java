import javax.swing.JFrame;
import javax.swing.JPanel;

//Brogan Avery
public class StopLightMain {

	public static void main(String[] args) {
		
		// 1. construct frame object
				JFrame frame = new JFrame();
				
				JPanel panel = new StopLightPanel(); // makes the panel object
				frame.add(panel);

				// 2. set frame size
				final int FRAME_WIDTH = 250;
				final int FRAME_HEIGHT = 400;
				frame.setSize(FRAME_WIDTH, FRAME_HEIGHT);

				// 3.title
				frame.setTitle("Stop Light");

				// 4.set close
				frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

				
				// 5.make visible
				frame.setVisible(true);
	}

}
