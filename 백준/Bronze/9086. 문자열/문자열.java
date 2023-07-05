import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		sc.nextLine();
		for (int i = 0; i < T; i++) {
			String s = sc.nextLine();
			System.out.println(s.charAt(0) + "" + s.charAt(s.length()-1));
		}
	}
}