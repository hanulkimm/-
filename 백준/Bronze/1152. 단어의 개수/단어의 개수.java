import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        String[] sent = s.split(" ");
        int ans = 0;
        for (String num : sent) {
            if (num.length()>0) {
                ans +=1;
            }
        }
        System.out.println(ans);
        }
    }
