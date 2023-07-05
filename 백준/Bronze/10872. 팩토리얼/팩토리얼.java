import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		if (N == 0) {
			System.out.println(1);
		}
		else {
			int c = 1;
			for (int i = N; i > 1; i--) {
				c *= i;
			}
			System.out.println(c);
		}
	}
}