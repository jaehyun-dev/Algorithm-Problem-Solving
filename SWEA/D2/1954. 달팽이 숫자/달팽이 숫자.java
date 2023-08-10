import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();
		for (int t = 1; t <= T; t++) {
			int N = sc.nextInt();
			int[][] map = new int[N][N];
			int r = 0;
			int c = -1;
			int num = 1;
			int dir = 0;
			int rep = N;
			while (num <= N * N) {
				for (int i = 0; i < rep; i++) {
					switch (dir % 4) {
						case 0:
							c++;
							break;
						case 1:
							r++;
							break;
						case 2:
							c--;
							break;
						case 3:
							r--;
							break;
					}
					map[r][c] = num++;
				}
				if (dir++ % 2 == 0) {
					rep--;
				}
			}
			
			System.out.printf("#%d\n", t);
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					System.out.printf("%d ", map[i][j]);
				}
				System.out.println();
			}

		}

	}
}