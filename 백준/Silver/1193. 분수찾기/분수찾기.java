import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int i = 0;
        while (num>0) {
            num -= (i+1);
            i += 1;
        }
        if (i%2==1) {
            System.out.println((i+1)-(i+num)+"/"+(i+num));
        } else {
            System.out.println((i+num) + "/"+ ((i+1)-(i+num)));
        }
    }
}

