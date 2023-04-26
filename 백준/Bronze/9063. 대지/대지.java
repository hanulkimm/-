import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int max_x = -100000;
        int min_x = 100000;
        int max_y = -100000;
        int min_y = 100000;
        for (int i = 0; i < n; i++) {
            int a = sc.nextInt();
            if (max_x<a) {
                max_x = a;
            }
            if (min_x>a) {
                min_x = a;
            }
            int b = sc.nextInt();
            if (max_y<b) {
                max_y = b;
            }
            if (min_y>b) {
                min_y = b;
            }
        }
        System.out.println((max_x-min_x)*(max_y-min_y));
    }
}

