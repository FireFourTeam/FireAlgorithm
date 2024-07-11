import java.util.*;

public class jamie {
  /*
   * 참고: https://st-lab.tistory.com/141
   * 
   * dp[3][0] = items[0][1]
   * dp[3][1] = dp[3][1]
   * ...
   * dp[5][0] = items[0][1]
   * dp[5][1] = dp[5][0] 또는 (if items[1][0] <=5) items[1][1]
   * dp[5][2] = dp[5][1] 또는 (if items[2][1] <=5) 
   */
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int K = sc.nextInt();

    int[][] items = new int[N][2];
    int[][] dp = new int[K + 1][N];

    for (int i = 0; i < N; i++) {
      items[i][0] = sc.nextInt();
      items[i][1] = sc.nextInt();
    }
    Arrays.sort(items, new Comparator<int[]>() { // [][0] 기준 오름차순 정렬
      @Override
      public int compare(int[] o1, int[] o2) {
        return o1[0] - o2[0];
      }
    });

    for (int i = items[0][0]; i <= K; i++) {
      dp[i] = dp[i - items[i][0]];
    }

    // ...

  }
}
