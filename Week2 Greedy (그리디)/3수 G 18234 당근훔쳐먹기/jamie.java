
// 틀린 코드.....임니다 .. ...

import java.util.*;
import java.io.*;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int N = Integer.parseInt(st.nextToken());
    long T = Long.parseLong(st.nextToken());

    PriorityQueue<Carrot> pq = new PriorityQueue<>(new Comparator<Carrot>() {
      public int compare(Carrot c1, Carrot c2) {
        return Long.compare(c2.taste, c1.taste);
      }
    });

    for (int i = 0; i < N; i++) {
      st = new StringTokenizer(br.readLine());
      long wi = Long.parseLong(st.nextToken());
      long pi = Long.parseLong(st.nextToken());

      pq.offer(new Carrot(wi, pi));
    }

    long sum = 0;
    for (long day = 1; day <= T; day++) {
      if (!pq.isEmpty()) {
        Carrot carrotForEat = pq.poll();
        sum += carrotForEat.taste;
        carrotForEat.taste += carrotForEat.increment;
        pq.offer(carrotForEat);
      }
    }

    System.out.println(sum);
  }
}

class Carrot {
  long taste;
  long increment;

  Carrot(long taste, long increment) {
    this.taste = taste;
    this.increment = increment;
  }
}