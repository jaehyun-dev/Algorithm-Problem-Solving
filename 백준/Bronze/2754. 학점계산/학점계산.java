import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String grade = sc.next();
		char alphabet = grade.charAt(0);
		float score = 0;
		if (alphabet == 'A') {
			score += 4;
		}
		else if (alphabet == 'B') {
			score += 3;
		}
		else if (alphabet == 'C') {
			score += 2;
		}
		else if (alphabet == 'D') {
			score += 1;
		}
		if (grade.length() == 2) {
			char bonus = grade.charAt(1);
			if (bonus == '+') {
				score += 0.3;
			}
			else if (bonus == '-') {
				score -= 0.3;
			}
		}
		System.out.println(score);
	}
}