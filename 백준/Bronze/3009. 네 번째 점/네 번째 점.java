import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int[] x = new int[1001];
        int[] y = new int[1001];
        for (int i = 0; i < 3; i++) {
            x[sc.nextInt()] += 1;
            y[sc.nextInt()] += 1;
        }
        for (int i = 0; i < 1001; i++) {
            if (x[i]==1){
                System.out.println(i);
            }
        }
        for (int i = 0; i < 1001; i++) {
            if (y[i]==1){
                System.out.println(i);
            }
        }
    }
}

