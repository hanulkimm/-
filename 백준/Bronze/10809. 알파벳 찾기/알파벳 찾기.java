import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        StringBuilder st = new StringBuilder();
        String s = sc.next();
        for (char ch = 'a';  ch<='z' ; ch++) {
            st.append(s.indexOf(ch)+ " ");
        }
        System.out.println(st);
    }
}