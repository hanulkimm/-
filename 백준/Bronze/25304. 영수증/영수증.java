import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int total = sc.nextInt();
        int compare = 0;
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            compare += a*b;
        }
        if (total==compare) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}
