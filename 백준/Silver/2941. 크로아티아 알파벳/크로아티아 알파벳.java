import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder(sc.next());
        String[] croat = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
        int ans = 0;
        int i = 0;
        while (i<sb.length()) {
            Boolean flag = true;
            if (i<sb.length()-2) {
                String s3 = sb.substring(i, i + 3);
                for (String ch : croat) {
                    if (s3.equals(ch)) {
                        ans += 1;
                        flag = false;
                        i += 3;
                        break;
                    }
                }
            }
            if (flag &&  i<sb.length()-1) {
                String s2 = sb.substring(i, i + 2);
                for (String ch : croat) {
                    if (s2.equals(ch)) {
                        ans += 1;
                        flag = false;
                        i += 2;
                        break;
                    }
                }
            }

            if (flag) {
                ans += 1;
                i+=1;
            }
        }
        System.out.println(ans);
    }
}

