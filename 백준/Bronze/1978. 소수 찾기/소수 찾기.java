import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int ans = n;
        for (int i = 0; i < n; i++) {
            int num = sc.nextInt();
            if (num==1){
                ans -=1;
            } else {
                for (int j = 2; j < num; j++) {
                    if (num%j==0) {
                        ans -= 1;
                        break;
                    }
                }
            }

        }
        System.out.println(ans);
    }
}

