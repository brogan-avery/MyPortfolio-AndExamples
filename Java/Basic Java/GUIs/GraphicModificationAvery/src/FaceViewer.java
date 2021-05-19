//Brogan Avery
import javax.swing.JFrame;
import javax.swing.JComponent;
public class FaceViewer {
	public static void main(String[] args) {
		final int W = 400;
		final int H = 400;
		
		JFrame frame = new JFrame();
		frame.setSize(W, H);
		frame.setTitle("Face");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		JComponent component = new FaceComponent();
		
		frame.add(component);
		
		frame.setVisible(true);

		
		
	}
}
