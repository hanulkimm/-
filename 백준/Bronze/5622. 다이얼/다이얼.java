import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        int ans = 0;
        for (int i = 0; i < s.length(); i++) {
            int num = s.charAt(i)-'A';
            if (num<3) {ans += 3;} else if (num < 6) {ans += 4 ; } else if (num<9) {ans+=5; }
            else if (num<12) {ans+=6; } else if (num<15) {ans+=7; } else if (num<19) {ans+=8; }
            else if (num<22) {ans+=9;} else if (num<26) {ans+=10; }
        }
        System.out.println(ans);

        }
    }