import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        String st = sc.next();
        String[] croat = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
        for (int i = 0; i < croat.length; i++) {
            if (st.contains(croat[i])) {
                st = st.replace(croat[i], ".");
            }
        }
        System.out.println(st.length());

    }
}

