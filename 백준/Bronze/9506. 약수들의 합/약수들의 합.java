import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        while (true){
            int n = sc.nextInt();
            if (n!=-1) {
                ArrayList<String> list = new ArrayList<>();
                for (int i = 1; i < n; i++) {
                    if (n%i==0) {
                        list.add(""+i);
                    }
            }
                int tmp = 0;
                for (int i = 0; i < list.size(); i++) {
                    tmp += Integer.parseInt(list.get(i));
                }
                if (tmp==n){
                    System.out.println(n + " = " + String.join(" + ", list));
                }else {
                    System.out.println(n + " is NOT perfect.");
                }
        } else {
                break;
            }

        }
    }
}

