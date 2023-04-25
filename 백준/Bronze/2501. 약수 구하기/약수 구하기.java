import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int ans = 0;
        int cnt = 0;
        for (int i = 1; i < n+1; i++) {
            if (n%i==0) {
                cnt += 1;
                if (cnt==k) {
                    ans = i;
                }
            }
        }
        System.out.println(ans);
    }
}

