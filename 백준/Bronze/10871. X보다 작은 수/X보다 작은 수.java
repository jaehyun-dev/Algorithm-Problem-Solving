import java.util.*;
import java.util.stream.Collectors;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N, X;
		N = sc.nextInt();
		X = sc.nextInt();
		ArrayList<Integer> A = new ArrayList<>();
		for(int i = 0;i < N;i++){
			int j = sc.nextInt();
			if (j < X) {
			A.add(j);
			}
		}
		System.out.println(A.stream().map(String::valueOf).collect(Collectors.joining(" ")));
	}
}