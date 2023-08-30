import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		for (int t = 1; t <= T; t++) {
			int N = sc.nextInt(), K = sc.nextInt();
			int[] arr = new int[N];
			for (int n = 0; n < N; n++) {
				arr[n] = sc.nextInt();
			}
			
			int sum;
			int cnt = 0;
			for (int i = 0; i < (1 << N); i++) {
				sum = 0;
				for (int j = 0; j < N; j++) {
					if ((i & (1 << j)) > 0) {
						sum += arr[j];
					}
				}
				if (sum == K) cnt++;
			}
			
			System.out.println(String.format("#%d %d", t, cnt));
		}
		
		sc.close();
	}

}