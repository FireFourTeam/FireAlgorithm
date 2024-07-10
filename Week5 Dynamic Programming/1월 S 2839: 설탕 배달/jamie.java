import java.util.*;

public class jamie {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int min = Integer.MAX_VALUE;
    

    if (N % 5 == 0) {
      System.out.println(N / 5);
    } else if (N % 3 == 0) {
      min = Math.min(N / 3, min);
    } else {

      int count = 0;

      while (N >= 0) {
        N -= 5;
        count += 1;

        if (N % 3 == 0) {
          N -= N / 3;
          count += N / 3;
          break;
        }
      }

      min = Math.min(min, count);
    }

    if (N == 0) {
      System.out.println(min);
    } else {
      System.out.println(-1);
    }

  }
}
