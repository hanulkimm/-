import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int i = 1;
        int total = 1;
        int num = sc.nextInt();
        if (num==1) {
            System.out.println(1);
        } else {
            while (num>total+6*i) {
                total += 6*i;
                i += 1;
            }
            System.out.println(i+1);
        }

        
    }
}

