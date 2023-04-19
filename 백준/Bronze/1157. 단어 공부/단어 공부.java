import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] alphabet = new int[26];
        String s = sc.next();
        s = s.toLowerCase();

        for (int i = 0; i < s.length(); i++) {
//            System.out.println(s.charAt(i));
            alphabet[s.charAt(i)-'0'-49]+=1;
        }
        int max = 0;
        for (int i = 0; i < alphabet.length; i++) {
            if (max < alphabet[i]) {
                max = alphabet[i];
            }
        }
        int cnt = 0;
        int ans = 0;
        for (int i = 0; i < alphabet.length; i++) {
            if (alphabet[i]==max) {
                cnt += 1;
                ans = i;
            }
        }
        if (cnt>1) {
            System.out.println("?");
        } else {
            String ch = String.valueOf((char) (ans+97));
            ch = ch.toUpperCase();
            System.out.println(ch);
//            System.out.println((char)ans);
        }
        }

    }

