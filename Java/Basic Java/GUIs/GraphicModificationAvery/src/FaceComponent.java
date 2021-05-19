//Brogan Avery
import java.awt.Graphics; 
import java.awt.Color; 
import javax.swing.JComponent;

public class FaceComponent extends JComponent {

	public void paintComponent(Graphics g){
		
		g.drawOval(100, 100, 200, 200);
		
		g.setColor(Color.GREEN);
		g.drawOval(150, 155, 15, 15);
		
		g.setColor(Color.GREEN);
		g.drawOval(230, 155, 15, 15);
		
		g.setColor(Color.RED);
		g.drawArc(125, -15, 150, 290, 225, 90);
	}

}
