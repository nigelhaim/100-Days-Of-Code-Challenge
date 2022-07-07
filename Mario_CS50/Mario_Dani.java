/*
 * Mario_Dani.java file
 * 100 Days of Code - Day 1: Mario
 * Sophia Danielle F. Durana
 * July 4, 2022 
 * Time Used: 40:30
 */
import java.util.*;
public class Mario_Dani {
	
	static Scanner in = new Scanner(System.in);
	public static void main(String args[]) {
		
		String gap;
		char space, hash;
		int ctr, spaces, hashes, rows;
		int spacesBuffer, hashBuffer;

		space = ' ';
		hash = '#';
		gap = "  ";
		
		System.out.println(); // spacing purposes
		
		// rows user input
		System.out.print("Enter number of rows: ");
		rows = in.nextInt();
		rows = isValid(rows);
		
		spaces = rows;
		hashes = 1;
		hashBuffer = 1; // secondary storage
		
		System.out.println(); // spacing purposes
		
		while (rows != 0) {
			//System.out.println("Inside rows loop.");
			spacesBuffer = spaces--;
			
			while (spacesBuffer != 0) {
				//System.out.print("Inside spaces loop.");
				System.out.print(space);
				//System.out.print("."); // debugger
				spacesBuffer--;
			}
			
			printHash(hash, hashes++);
			System.out.print(gap);
			 
			printHash(hash, hashBuffer++);
			System.out.println(); // next line
			rows--;
		}
	}
	
	public static int isValid(int rows) {
		boolean validator = false;
		
		while (validator != true) {
			if (rows <= 0) {
				System.out.print("(Error: Input should be greater than 0)" +
								"\nPlease re-enter a valid number of rows: ");
				rows = in.nextInt();
			} else
				validator = true;
		}
		return rows;
	}
	
	public static void printHash(char hash, int rows) {
		for (int hashes = 1; hashes != rows + 1; hashes++) {
			//System.out.print("Inside hash loop.");
			System.out.print(hash);
		}
	}
}