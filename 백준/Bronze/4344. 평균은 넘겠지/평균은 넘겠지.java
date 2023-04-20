import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            int num = sc.nextInt();
            int[] scores = new int[num];
            for (int j = 0; j < num; j++) {
                scores[j] = sc.nextInt();
            }
            double sum = 0;
            for (int j = 0; j < scores.length; j++) {
                sum += scores[j];
            }
            double student = 0;
            for (int j = 0; j < scores.length; j++) {
                if (scores[j]>(sum/num)) {
                    student += 1;
                }
            }
            double ans = student/num*100;
            System.out.printf("%.3f", ans);
            System.out.print("%\n");
        }
    }
}

