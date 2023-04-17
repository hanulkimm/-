import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc= new Scanner(System.in);
        int[] leftover = new int[42];
        for (int i = 0; i < 10; i++) {
            int num = sc.nextInt();
            leftover[num%42]=1;
        }
        int ans = 0;
        for (int i = 0; i < 42; i++) {
            if (leftover[i]==1) {
                ans ++;
            }
        }
        System.out.println(ans);
    }
}