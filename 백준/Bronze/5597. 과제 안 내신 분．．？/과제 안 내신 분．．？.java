import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc= new Scanner(System.in);
        int[] lst = new int[30];
        for (int i = 0; i < 28; i++) {
            int num = sc.nextInt();
            lst[num-1]=1;
        }
        for (int i = 0; i < 30; i++) {
            if (lst[i]==0) {
                System.out.println(i+1);
            }
        }
    }
}