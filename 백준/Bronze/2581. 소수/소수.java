import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        int n = sc.nextInt();
        int sum = 0;
        int min_prime = 10000;
        for (int i = m; i < n+1; i++) {
            boolean prime = true;
            if (i==1) {
                continue;
            } else {
                for (int j = 2; j <= Math.sqrt(i); j++) {
                    if (i%j==0) {prime = false;}
                }
            }
            if (prime) {
                sum += i;
                if (i<min_prime) {min_prime = i;}

            }
        }
        if (sum>0) {
            System.out.println(sum);
            System.out.println(min_prime);
        } else {
            System.out.println(-1);
        }

    }
}

