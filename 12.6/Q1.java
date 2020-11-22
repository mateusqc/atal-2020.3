import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Q1 {
    public static List<List<Integer>> a = new ArrayList<>();
    public static List<Boolean> v = new ArrayList<>();
    public static List<Integer> ans = new ArrayList<>();

    public static void dfs (Integer n) {
        if (v.get(n)) {
            return;
        }
        v.set(n, true);
        for (Integer e : a.get(n)) {
            dfs(e);
        }
        ans.add(n);
        return;
    }
    
    public static void main(String []args) {
        int n;
        int m;
        Scanner in = new Scanner(System.in);
        String line = in.nextLine();
        String[] splitedLine = line.split(" ");

        m = Integer.parseInt(splitedLine[0]);
        n = Integer.parseInt(splitedLine[1]);
        
        Map<String, Integer> mp = new HashMap<>();

        for (int i = 0; i <= 301; i++) {
            v.add(false);
            a.add(new ArrayList<>());
        }

        String x;
        // String y;
        String z;

        int i = 1;

        while (n-- > 0) {
            line = in.nextLine();
            splitedLine = line.split(" ");
            x = splitedLine[0];
            // y = splitedLine[1];
            z = splitedLine[2];

            if (!mp.containsKey(x)) {
                mp.put(x, i++);
            }
            if (!mp.containsKey(z)) {
                mp.put(z, i++);
            }
            a.get(mp.get(x)).add(mp.get(z));
            a.get(mp.get(z)).add(mp.get(x));
        }

        int count = 0;
        for (int ii = 1; ii < i; ii++) {
            if (!v.get(ii)) {
                dfs(ii);
                count++;
            }
        }
        System.out.println(count);
    }
 }