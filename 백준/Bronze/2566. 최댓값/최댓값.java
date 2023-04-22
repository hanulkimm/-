import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int max = 0;
        int max_i = 1;
        int max_j = 1;
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                int num = sc.nextInt();
                if (max < num) {
                    max = num;
                    max_i = i+1;
                    max_j = j+1;
                }
            }
        }
        System.out.println(max);
        System.out.print(max_i + " " + max_j);
    }
}

