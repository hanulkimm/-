import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        String st = br.readLine();

        int ans = 0;
        for (int i = 0; i < n; i++) {
            ans += Integer.parseInt(String.valueOf(st.charAt(i)));
        }
        System.out.println(ans);

    }
}