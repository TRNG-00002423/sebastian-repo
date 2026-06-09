/**
 * Hello HelloWeek2
 * if it has 2 arguments prints name and lastname
 * if it was 1 argument prints name 
 * if it is nonoe print trainnee
 */
public class HelloWeek2{
    public static void main(String[] args){
        if (args.length == 2){
            System.out.println("Hello " + args[0] + " " + args[1]);
        }

        else if (args.length >= 1){
            System.out.println("Hello " + args[0]);
        }
        else{
            System.out.println("Hello, trainee!");
        }
        System.out.println(Runtime.version());
    }
}
