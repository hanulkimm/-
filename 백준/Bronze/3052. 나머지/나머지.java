import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc= new Scanner(System.in);
        HashSet<Integer> h = new HashSet<Integer>();
        for (int i = 0; i < 10; i++) {
            int num = sc.nextInt() % 42;
            h.add(num);
        }
        sc.close();
        System.out.println(h.size());
        }

    }
