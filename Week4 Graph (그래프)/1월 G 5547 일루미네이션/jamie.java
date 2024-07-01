package local;

import java.util.*;
import java.io.*;

public class jamie {

  // 풀다 말았씁니당...

  static int W, H;
  static int[][] graph;
  static boolean[][] visited;
  static int[] dx = { 1, -1, 0, 0 };
  static int[] dy = { 0, 0, 1, -1 };

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    W = Integer.parseInt(st.nextToken());
    H = Integer.parseInt(st.nextToken());
    graph = new int[W][H];
    visited = new boolean[W][H];

    for (int i = 0; i < H; i++) {
      st = new StringTokenizer(br.readLine());
      for (int j = 0; j < W; j++) {
        graph[j][i] = Integer.parseInt(st.nextToken());
      }
    }


  }
  
  static int count = 0;

  static void bfs(int x, int y) {
    if (visited[x][y]) {
      if (graph[x][y] == 0) {
        
      }
      return;
    }



    for (int i = 0; i < 4; i++) {
      int newX = x + dx[i];
      int newY = y + dx[i];
      if (newX >= 0 && newX < W && newY >= 0 && newY < H) {
        bfs(newX, newY);
      }
    }
  }
}
