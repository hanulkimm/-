import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            int num = sc.nextInt();
            int quarter = 0;
            quarter += num/100*4;
            num%=100;
            quarter += num/25;
            num%=25;
            int dime = 0;
            dime += num/10;
            num%=10;
            int nickel = 0;
            nickel += num/5;
            num%=5;
            int penny = num;
            System.out.println(quarter + " " + dime + " " + nickel + " " + penny) ;
        }

    }
}

