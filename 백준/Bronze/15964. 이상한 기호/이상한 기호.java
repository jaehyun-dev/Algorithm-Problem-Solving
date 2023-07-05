import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int A, B;
		A = sc.nextInt();
		B = sc.nextInt();
		int result = newOperation(A, B);
		System.out.println(result);
	}
	
	public static int newOperation(int A, int B) {
		int first = A + B;
		int second = A - B;
		return first * second;
	}	
}