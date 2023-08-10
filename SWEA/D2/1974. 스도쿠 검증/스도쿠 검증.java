import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();
		for (int t = 1; t <= 10; t++) {
			int[][] map = new int[9][9];
			for (int i = 0; i < 9; i++) {
				for (int j = 0; j < 9; j++) {
					map[i][j] = sc.nextInt();
				}
			}
			int ans = 1;
			line: for (int i = 0; i < 9; i++) {
				List<Integer> usedRow = new ArrayList<>();
				List<Integer> usedCol = new ArrayList<>();
				for (int j = 0; j < 9; j++) {
					if (usedRow.contains(map[i][j])) {
						ans = 0;
						break line;
					}
					usedRow.add(map[i][j]);
					if (usedCol.contains(map[j][i])) {
						ans = 0;
						break line;
					}
					usedCol.add(map[j][i]);
				}
			}
			grid: for (int k = 0; k < 3; k++) {
				for (int l = 0; l < 3; l++) {
					int r = 1 + 3 * k;
					int c = 1 + 3 * l;
					List<Integer> usedGrid = new ArrayList<>();
					for (int i = -1; i < 2; i++) {
						for (int j = -1; j < 2; j++) {
							if (usedGrid.contains(map[r + i][c + j])) {
								ans = 0;
								break grid;
							}
							usedGrid.add(map[r + i][c + j]);
						}
					}
				}
			}
			System.out.println(String.format("#%d %d", t, ans));

		}

		sc.close();

	}
}