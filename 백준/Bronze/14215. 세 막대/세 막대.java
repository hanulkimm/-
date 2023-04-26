import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int[] list = new int[3];
        for (int i = 0; i < 3; i++) {
            list[i]=sc.nextInt();
        }
        Arrays.sort(list);
        while (list[0]+list[1]<=list[2]){
            list[2]-=1;
        }
        System.out.println(list[0]+list[1]+list[2]);
    }
}

