import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        StringBuilder sb1 = new StringBuilder();
        StringBuilder sb2 = new StringBuilder();
        a = Integer.parseInt(sb1.append(a).reverse().toString());
        b = Integer.parseInt(sb2.append(b).reverse().toString());
        System.out.println(a>b?a:b);
        }
    }