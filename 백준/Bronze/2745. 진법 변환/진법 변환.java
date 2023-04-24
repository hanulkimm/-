import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        int n = sc.nextInt();
        int ans = 0;
        for (int i = s.length()-1; i > -1; i--) {
            int num = s.charAt(i)-'0';
            if (num>10) {
                num -= 7;
            }
            ans += num * Math.pow(n, s.length()-1-i);
        }
        System.out.println(ans);
    }
}

