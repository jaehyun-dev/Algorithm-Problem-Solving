import java.util.*;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		for (int t = 1; t <= T; t++) {
			Stack<Character> st = new Stack<>();
			int cnt = 0;
			char prev = '(';
			String line = sc.next();
			for (int i = 0; i < line.length(); i++) {
				char c = line.charAt(i);
				if (c == '(') {
					st.push(c);
				} else {
					st.pop();
					if (prev == '(') {
						cnt += st.size();
					}
					else cnt++;
				}
				prev = c;
				
			}
			
		
			System.out.println(String.format("#%d %d", t, cnt));
		}
		
		sc.close();
	}

}