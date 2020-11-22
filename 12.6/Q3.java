import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Q3 {
    public static List<List<Integer>> adj = new ArrayList<>();
    public static List<Integer> dp = new ArrayList<>();
    public static List<Hos> hos = new ArrayList<>();
    public static List<Boolean> seen = new ArrayList<>();

    public static void getGroup (int v, List<Hos> gp) {
        gp.add(hos.get(v));
        seen.set(v, true);
        for (Integer u : adj.get(v)) {
            if (!seen.get(u)) {
                getGroup(u, gp);
            }
        }
    }

    public static void main(String []args) {
        Scanner in = new Scanner(System.in);
        int n;
        int m;
        int mxw;
        String line = in.nextLine();
        String[] splitedLine = line.split(" ");

        n = Integer.parseInt(splitedLine[0]);
        m = Integer.parseInt(splitedLine[1]);
        mxw = Integer.parseInt(splitedLine[2]);

        for (int i = 0; i < n; i++) {
            hos.add(new Hos());
            adj.add(new ArrayList<>());
            seen.add(false);
        }
        
        for (int i = 0; i <= mxw; i++) {
            dp.add(0);
        }

        line = in.nextLine();
        String[] splitedLineW = line.split(" ");
        line = in.nextLine();
        String[] splitedLineB = line.split(" ");

        for (int i = 0; i < n; i++) {
            int w = Integer.parseInt(splitedLineW[i]);
            int b = Integer.parseInt(splitedLineB[i]);
            Hos ho = hos.get(i);
            ho.w = w;
            ho.b = b;
            hos.set(i, ho);
        }

        
        for (int v, u; m-- > 0;) {
            line = in.nextLine();
            splitedLine = line.split(" ");
            v = Integer.parseInt(splitedLine[0]) - 1;
            u = Integer.parseInt(splitedLine[1]) - 1;
            adj.get(v).add(u);
            adj.get(u).add(v);
        }

        for (int i = 0; i < n; i++) {
            if (!seen.get(i)) {
                List<Hos> gp = new ArrayList<>();
                getGroup(i, gp);
                int sumw = 0;
                int sumb = 0;
                for (Hos ho : gp) {
                    sumb += ho.b;
                    sumw += ho.w;
                }
                Hos newHo = new Hos();
                newHo.b = sumb;
                newHo.w = sumw;
                gp.add(newHo);

                for (int j = mxw; j >=0; j--) {
                    for (Hos ho : gp) {
                        if (j >= ho.w) {
                            dp.set(j, Math.max(dp.get(j), dp.get(j - ho.w) + ho.b));
                        }
                    }
                }
            }
        }
        System.out.println(dp.get(mxw));
    }

    public static class Hos {
        int w = 0;
        int b = 0;
    }
 }