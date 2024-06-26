import java.util.*;
import java.io.*;

public class jamie {

  static int k;
  static ArrayList<Integer> numbers;
  static StringBuilder sb;
  static boolean[] visited;

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    sb = new StringBuilder();

    while (true) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      int isZero = Integer.parseInt(st.nextToken());
      if (isZero == 0) {
        break;
      }

      k = isZero;
      numbers = new ArrayList<>();
      visited = new boolean[k];

      for (int i = 0; i < k; i++) {
        numbers.add(Integer.parseInt(st.nextToken()));
      }

      match(0, 0, new ArrayList<Integer>());
      sb.append(" ");
    }

    System.out.println(sb.toString());
  }
  
  static void match(int start, int count, ArrayList<Integer> selected) {

    if (count == k) {
      for (int i = 0; i < k; i++) {
        sb.append(numbers.get(i));
        if (i < numbers.size() - 1) {
          sb.append(" ");
        }
      }
      sb.append("\n");
      return;
    }

    for (int i = count; i < k; i++) {
      if (!visited[i]) {
        visited[i] = true;
        match(i+1, count + 1, selected);
        visited[i] = false;
      }
    }
  }
}
