//Brogan Avery
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
	
public class ClickListener implements ActionListener { 
	int clicked;
	
	@Override
	public void actionPerformed(ActionEvent event) { 
		clicked++;
		System.out.println("I was clicked " + clicked + " times!");
	} 
}

