/*
	100 Days of Code
	Day 1 : Adjacency Matrix
	Alyza Paige L. Ng
*/

import java.util.*;

public class AdjacentNodes_Aly {
	static Scanner in = new Scanner(System.in);
	
	private int vertices, matrix[][];
	
	// constructor
	public AdjacentNodes_Aly(int vertices) {
		this.vertices = vertices;
		matrix = new int[vertices][vertices];
	}	
	
	public void connectNodes(int from, int to) {
		matrix[from][to] = 1;
		matrix[to][from] = 1; // undirected
	}
	
	public void printMatrix() {
		System.out.println();
		for(int i = 0; i < vertices; i++) {
			for(int j = 0; j < vertices; j++)
				System.out.print(matrix[i][j] + " ");
			System.out.println();
		}
	}
	
	public static int validate(int number) {
		for(; number <= 0 || number >= 25000; number = in.nextInt())
			System.out.print("Graphs may have between 0 and 25,000 nodes.\nPlease enter again: ");
		return number;
	}
	
	public static void main(String[] args) {
		System.out.print("Enter the number of nodes: "); int numVer = validate(in.nextInt());
		System.out.print("Enter the number of edges: "); int numEdg = in.nextInt();
		AdjacentNodes_Aly graph = new AdjacentNodes_Aly(numVer);
		
		for(int i = 0; i < numEdg; i++) {
			System.out.print("Enter the source vertex: "); int start = in.nextInt();
			System.out.print("Enter the destination vertex: "); int next = in.nextInt();
			graph.connectNodes(start, next);
		}
		graph.printMatrix();
	}
}