import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            StringBuilder st = new StringBuilder();
            int num = sc.nextInt();
            String s = sc.next();
            for (int j = 0; j < s.length(); j++) {
                for (int k = 0; k < num; k++) {
                    st.append(s.charAt(j));
                }
            }
            System.out.println(st);
        }

    }
}