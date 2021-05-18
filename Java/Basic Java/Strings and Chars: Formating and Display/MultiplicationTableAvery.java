
/**************************************************************
* Title: Multiplication table
* Author: Brogan Avery
* Created: 2019 
***************************************************************/
public class MultiplicationTableAvery {

	public static void main(String[] args) {
		final int ROW_MAX = 12;
		final int COL_MAX = 12;

		for (int c = 1; c <= COL_MAX; c++) {
			System.out.printf("%6d", c);
		}
		System.out.println();

		for (double r = 2; r <= ROW_MAX; r++) {

			for (int c = 1; c <= COL_MAX; c++) {
				System.out.printf("%6.0f", (r * c));
			}
			System.out.println();
		}
	}

}
