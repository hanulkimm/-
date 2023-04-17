import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int[] arr = new int[n+1];
        for (int i = 1; i < n+1; i++) {
            arr[i]=i;
        }
        int m = Integer.parseInt(st.nextToken());
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            while (start<end) {
                int save = arr[end];
                arr[end] = arr[start];
                arr[start] = save;
                start ++;
                end--;
            }
        }
        for (int i = 1; i < n+1; i++) {
            System.out.print(arr[i]+" ");
        }
        }
    }
