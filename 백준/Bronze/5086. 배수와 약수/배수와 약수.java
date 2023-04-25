import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        while (true) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            if (a!=0){
                if (a%b==0){
                    System.out.println("multiple");
                } else if (b%a==0) {
                    System.out.println("factor");
                } else {
                    System.out.println("neither");
                }
            } else {
                break;
            }
        }
    }
}

