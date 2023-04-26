import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        while (true) {
            boolean flag = false;
            int[] num = new int[3];
            for (int i = 0; i < 3; i++) {
                num[i]= sc.nextInt();
                if (num[i]==0) {flag=true;}
            }
            if (flag) {break;}
            Arrays.sort(num);
            if (num[2]>= num[0]+num[1]){
                System.out.println("Invalid");
            } else {
                if (num[0]==num[1] && num[1]==num[2] && num[2]==num[0]) {
                    System.out.println("Equilateral");
                } else if (num[0]==num[1] || num[1]==num[2] || num[2]==num[0]) {
                    System.out.println("Isosceles ");
                } else {
                    System.out.println("Scalene ");
                }
            }
        }

    }
}

