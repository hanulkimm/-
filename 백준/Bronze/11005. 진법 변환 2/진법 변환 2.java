import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int n = sc.nextInt();
        List<Character> list = new ArrayList<>();
        while (num > 0) {
            int left = num%n;
            num = num/n;
            if (left>=10) {
                list.add((char) (left-10+'A'));
            } else {
                list.add((char) (left+'0'));
            }
        }
        for (int i = list.size()-1; i >-1 ; i--) {
            System.out.print(list.get(i));
        }
    }
}

