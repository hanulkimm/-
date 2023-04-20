import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int ans = 0;
        for (int i = 0; i < n; i++) {
            String s = sc.next();
            Boolean flag = false;

            for (int j = 0; j < s.length(); j++) {
                for (int k = s.indexOf(s.charAt(j)); k < s.lastIndexOf(s.charAt(j))+1; k++) {
                    if (s.charAt(k)!=s.charAt(j)) {
                        flag =true;
                    }
                    if (flag) {break; }
                }
            }
            if (!flag) {
                ans += 1;
            }
        }
        System.out.println(ans);
    }
}

