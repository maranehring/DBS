import java.util.Scanner; //importiere Scanner

class Uebung1{
	public static void main (String args []){
		System.out.println("Wie heißen Sie?"); //Print "Wie heißen Sie?"
		Scanner k = new Scanner(System.in); //Scanne die Eingabe k
		System.out.println("Hallo " + k.nextLine() + "!"); //Print "Hallo k!"
	}
}
