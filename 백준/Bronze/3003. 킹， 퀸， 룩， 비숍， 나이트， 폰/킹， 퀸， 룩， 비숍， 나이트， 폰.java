import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        StringTokenizer st = new StringTokenizer(sc.nextLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());
        int e = Integer.parseInt(st.nextToken());
        int f = Integer.parseInt(st.nextToken());
        if (a>=1) {
            System.out.print(1-a + " ");
        } else {
            System.out.print(1-a+ " ");
        }
        if (b>=1) {
            System.out.print(1-b+ " ");
        } else {
            System.out.print(1-b+ " ");
        }
        if (c>=2) {
            System.out.print(2-c+ " ");
        } else {
            System.out.print(2-c+ " ");
        }
        if (d>=2) {
            System.out.print(2-d+ " ");
        } else {
            System.out.print(2-d+ " ");
        }
        if (e>=2) {
            System.out.print(2-e+ " ");
        } else {
            System.out.print(2-e+ " ");
        }
        if (f>=8) {
            System.out.print(8-f+ " ");
        } else {
            System.out.print(8-f+ " ");
        }
    }
}

