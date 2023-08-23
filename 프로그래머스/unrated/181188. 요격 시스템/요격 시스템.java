import java.util.Arrays;

class Solution {
	
	public int solution(int[][] targets) {
        Arrays.sort(targets, (t1, t2) -> {
        	int cmp = Integer.compare(t1[1], t2[1]);
        	
        	if (cmp == 0) {
        		cmp = Integer.compare(t1[0], t2[0]);
        	}
        	return cmp;
        });

        int cnt = 0;
		int end = 0;
		for (int i = 0; i < targets.length; i++) {
			if (targets[i][0] >= end) {
				cnt++;
				end = targets[i][1];
			}
		}
        return cnt;
    }
	
}