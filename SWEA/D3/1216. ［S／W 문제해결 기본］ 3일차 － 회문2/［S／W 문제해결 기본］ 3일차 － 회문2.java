import java.util.Scanner;
 
public class Solution {
 
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
         
        int T = 10;
        int N = 100;
 
        for (int t = 1; t <= T; t++) {
            sc.nextInt();
            char[][] map = new char[N][N];
            for (int r = 0; r < N; r++) {
                String line = sc.next();
                for (int c = 0; c < N; c++) {
                    map[r][c] = line.charAt(c);
                }
            }
 
            int longestH = 0;
            int longestV = 0;
            int ans = 0;
            int temp = 0;
            int[] arr = new int[4];
            for (int r = 0; r < N; r++) {
                for (int c = 0; c < N; c++) {
                    length: for (int i = N - 1; i > c; i--) {
                        boolean flagH = true;
                        boolean flagV = true;
                        for (int j = 0; j < (i - c + 1) / 2; j++) {
                            if (flagH) {
                                if (map[r][c + j] != map[r][i - j]) {
                                    flagH = false;
                                }
                            }
                            if (flagV) {
                                if (map[c + j][r] != map[i - j][r]) {
                                    flagV = false;  
                                }
                            }
                             
                            if (!flagH && !flagV) break;
                        }
                        if (flagH) {
                            longestH = i - c + 1;
                            temp = longestH;
                        }
                        if (flagV) {
                            longestV = i - c + 1;
                            temp = longestV;
                        }
                        if (flagH || flagV) {
                            if (temp > ans) {
                                ans = temp;
                                 
                            }
                                 
                            break length;
                        }
                    }
 
                }
            }
            System.out.println(String.format("#%d %d", t, ans));
 
        }
 
        sc.close();
    }
 
}