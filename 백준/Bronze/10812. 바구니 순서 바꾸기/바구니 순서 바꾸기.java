import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] list = new int[n+1];
        for (int i = 0; i < n+1; i++) {
            list[i] = i;
        }
        for (int i = 0; i < m; i++) {
            int start = sc.nextInt();
            int end = sc.nextInt();
            int mid = sc.nextInt();

            int[] replace = new int[n+1];
            for (int j = 0; j < end-mid+1; j++) {
                replace[start+ j] = list[mid+j];
            }
            for (int j = 0; j < mid-start; j++) {
                replace[start + (end-mid+1) + j] = list[start+j];
            }
            for (int j = start; j < end+1; j++) {
                list[j] = replace[j];
            }
        }
        for (int i = 1; i < list.length; i++) {
            System.out.print(list[i] + " ");
        }
    }
}

