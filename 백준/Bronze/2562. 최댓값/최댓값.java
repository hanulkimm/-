import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int i = 1;
        int max = 0;
        int max_i = 0;
        while (i<10) {
            int num = Integer.parseInt(br.readLine());
            if (max < num ) {
                max = num;
                max_i = i;
            }
            i++;
        }
        System.out.println(max);
        System.out.println(max_i);
    }
}