//Brogan Avery
import javax.swing.JPanel;
import javax.swing.JButton;
import java.awt.Dimension;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;


public class StopLightPanel extends JPanel{

	StopLightDrawing light = new StopLightDrawing();

//constructor
	public StopLightPanel() {

		JButton switchButton = new JButton("Switch");

		light.setPreferredSize(new Dimension(160,260));


		ButtonListener l = new ButtonListener();    //a thing to do
		switchButton.addActionListener(l); 			// tells button it will do thing

		//add things to panel
		add(light);
		add(switchButton);
	}



	class ButtonListener implements ActionListener{

		@Override
		public void actionPerformed(ActionEvent e) {
			light.changeColor();

		}

	}
}
