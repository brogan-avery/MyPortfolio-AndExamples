import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class RPSLSAveryTest {

	
		@Test
		void testGetWinner() {
			assertEquals("TIE", RPSLSAvery.getWinner("ROCK", "ROCK"));
			assertEquals("PLAYER1 WINS", RPSLSAvery.getWinner("ROCK", "SCISSORS"));
			assertEquals("PLAYER1 WINS", RPSLSAvery.getWinner("PAPER", "ROCK"));
			assertEquals("PLAYER2 WINS", RPSLSAvery.getWinner("SPOCK", "PAPER"));
			assertEquals("PLAYER2 WINS", RPSLSAvery.getWinner("PAPER", "LIZARD"));
		
	}

}
