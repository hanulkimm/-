import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        double[] arr = new double[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextDouble();
        }
        sc.close();
        Arrays.sort(arr);
        double sum = 0;
        for (int i = 0; i < n; i++) {
            sum += (arr[i]/arr[n-1])*100;
        }
        System.out.println(sum/n);
        }
    }
