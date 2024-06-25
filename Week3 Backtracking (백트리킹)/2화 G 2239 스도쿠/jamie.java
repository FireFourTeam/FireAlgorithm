package local;

import java.util.*;
import java.io.*;

public class jamie {

  // 모르겠어요 ... ... ㅠ ㅠ
  // 앤디 교수님 help ... .
  
  static boolean[] visited = new boolean[9];
  static int[][] graph;

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    graph = new int[9][9];
    for (int i = 0; i < 9; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      for (int j = 0; j < 9; j++) {
        graph[i][j] = Integer.parseInt(st.nextToken());
      }
    }

    for (int i = 0; i < 9; i++) {
      make(0, i);
    }
  }
  
  static void make(int row, int column) {
    ArrayList<Integer> current = new ArrayList<>();

    if (graph[row][column] != 0) {
      current.add(graph[row][column]);
    } else {

    }

    for (int i = 0; i < 9; i++) {
      if (!visited[i]) {
        visited[i] = true;
        make(i);
        visited[i] = false;

      }
    }
  }
}
