import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int h = sc.nextInt();
        int m = sc.nextInt();
        sc.close();
        if (m>=45) {
            System.out.println(h + " " + (m-45));
        } else {
            h -=1;
            if (h<0) {
                System.out.println(23 + " " + (60-(45-m)));
            } else {
                System.out.println(h + " " + (60-(45-m)));
            }
        }
    }
}
