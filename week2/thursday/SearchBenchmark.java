import java.util.Random;
//from SearchLib import linearSearch, binarySearch;

class SearchBenchmark{
    public static void main(String[] args) {
        int num_list[] = new int[1000];
        Random rand = new Random();

        for (int i = 0; i < 1000; i++){
            num_list[i] = i*2;
        }

        int ranNum = rand.nextInt(1000);

        long now = System.currentTimeMillis();;
        SearchLib.binarySearch(num_list, ranNum);
        System.out.println(System.currentTimeMillis() - now);

        now = System.currentTimeMillis();
        SearchLib.linearSearch(num_list, ranNum);
        System.out.println(System.currentTimeMillis() - now);

    }
}
