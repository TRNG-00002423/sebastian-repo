public class SearchLib {
    public static int linearSearch(int[] sorted, int target){
        for (int i = 0; i < sorted.length ; i++){
            if (sorted[i] == target){
                return i;
            }
        }
        return -1;
    }

    public static int binarySearch(int[] sorted, int target){
        int high = sorted.length-1;
        int low = 0;

        while (low <= high){
            int mid = (high+low)/2;
            if (sorted[mid] == target) return mid;
            else if (sorted[mid] > target) high = mid-1;
            else low = mid+1;
        }
        return -1;
    }
}
