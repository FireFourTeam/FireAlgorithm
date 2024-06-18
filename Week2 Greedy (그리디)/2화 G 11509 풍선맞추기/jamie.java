import java.util.*;
import java.io.*;

public class B11509_풍선맞추기 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int N = Integer.parseInt(br.readLine());
    StringTokenizer st = new StringTokenizer(br.readLine());

    int[] arr = new int[1000000];
    int result = 0;

    for (int i = 0; i < N; i++) {
      int currentHeight = Integer.parseInt(st.nextToken());

      if (arr[currentHeight] > 0) {
        arr[currentHeight]--;
      }
    }

    for (int i : arr) {
      result += i;
    }

    System.out.println(result);
  }
}
