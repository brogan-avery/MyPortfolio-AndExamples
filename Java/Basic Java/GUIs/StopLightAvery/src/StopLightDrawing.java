
//Brogan Avery
import java.awt.Color;
import java.awt.Graphics;
import javax.swing.JComponent;

public class StopLightDrawing extends JComponent {
	Color go = Color.gray;
	Color slow = Color.gray;
	Color stop = Color.red;

	String activeLight = "red";
	
	public void paintComponent(Graphics g) {
		g.setColor(Color.yellow);
		g.fillRect(0, 0, 150, 250);

		g.setColor(Color.black);
		g.drawRect(0, 0, 150, 250);

		g.setColor(stop);
		g.fillOval(44, 15, 70, 70);

		g.setColor(slow);
		g.fillOval(44, 90, 70, 70);

		g.setColor(go);
		g.fillOval(44, 165, 70, 70);
	}

	public void changeColor() {
		go = Color.gray;
		slow = Color.gray;
		stop = Color.gray;
		
		if (activeLight.equals("red")) {
			activeLight = "green";
			go = Color.green;
		}
		else if(activeLight.equals("green")) {
			activeLight = "yellow";
			slow = Color.orange;
		}
		
		else {
			activeLight = "red";
			stop = Color.red;
		}
		
		repaint();
	}

}
