import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        String star = "*";
        int n = sc.nextInt();
        for (int i = 1; i < 2*n; i++) {
            int k = i;
            if (i>=n) {
                k = n-(i-n);
            }
            for (int j = 0; j < n-k; j++) {
                System.out.print(" ");
            }
            for (int j = 0; j < 2*k-1; j++) {
                System.out.print(star);
            }
            System.out.println();
        }
    }
}

