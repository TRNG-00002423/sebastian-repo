public class BuggyReport {

    public static void main(String[] args) {
        String[] cases = {"alpha", "beta", "gamma"};
        System.out.println("countWords=" + countWords(cases));

        int[] scores = {10, 20, 25};
        System.out.println("average=" + average(scores));

        String label = buildLabel(null);
        System.out.println("label=" + label);

        boolean gate = allowAccess(5, 3);
        System.out.println("allowAccess=" + gate);

        int idx = findFirst(scores, 20);
        System.out.println("findFirst(20)=" + idx);

        if (countWords(cases) == 3
                && Math.abs(average(scores) - (55.0 / 3.0)) < 0.001
                && "guest".equals(label)
                && gate
                && idx == 1) {
            System.out.println("VERIFIED: all checks passed");
        } else {
            System.out.println("VERIFICATION FAILED — keep debugging");
        }
    }

    static String buildLabel(String user) {
        if (user == null || user.trim().isEmpty()) {
            return "guest";
        }
        return user.trim().toLowerCase();
    }

    static boolean allowAccess(int roleLevel, int required) {
        return roleLevel >= required;
    }

    /** BUG 3: integer division — need floating-point average */
    static double average(int[] values) {
        float sum = 0;
        for (int v : values) {
            sum += v;
        }
        return sum / values.length;
    }

    static int findFirst(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target) {
                return i;
            }
        }
        return -1;
    }

    static int countWords(String[] words) {
        int c = 0;
        for (int i = 0; i < words.length; i++) {
            if (words[i] != null && !words[i].isEmpty()) {
                c++;
            }
        }
        return c;
    }
}
