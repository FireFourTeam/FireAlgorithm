package local;

import java.util.*;
import java.io.*;

public class jamie {

  /* 규칙 찾기
  20은 1번만 나눠도 10이 2개 생김
  30은 2번만 나눠도 10이 3개 생김
  -> 10의 배수가 나온다면 배수만큼 10이 생긴다.
  
  => 10의 배수인 수를 가장 먼저 해야 함
   */ 

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    StringTokenizer st = new StringTokenizer(br.readLine());
    int N = Integer.parseInt(st.nextToken());
    int M = Integer.parseInt(st.nextToken());

    // 10으로 나눈 나머지가 작은 순서대로 정렬
    PriorityQueue<Integer> rollcakes = new PriorityQueue<>((l1, l2) -> Integer.compare(l1 % 10, l2 % 10));

    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < N; i++) {
      rollcakes.offer(Integer.parseInt(st.nextToken()));
    }


    int count = 0;
    for (int rollcake : rollcakes) {
      if (rollcake < 10) {
        return;
      } else if (rollcake == 10) {
        count++;
      } else {
        int temp;
        if (rollcake % 10 == 0) {
          temp = rollcake / 10 - 1;
        } else {
          temp = rollcake / 10;
        }

        if (M >= temp) {
          M -= temp;
          count += rollcake / 10;
        } else {
          count += M;
          break;
        }
      }

      if (M == 0) {
        break;
      }

    }

    System.out.println(count);
  }
}
