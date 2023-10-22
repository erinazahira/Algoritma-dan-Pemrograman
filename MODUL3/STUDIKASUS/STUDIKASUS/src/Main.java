import java.util.Scanner;
import java.io.InputStream;
import java.util.InputMismatchException;

public class Main {
    boolean repeat = true;
    
    public static void main(String[] args) throws Exception {
        Scanner myobj = new Scanner(System.in);
        do {
            try {
                switch (key) {
                    case 1:
                        System.out.println("Masukkan sisi: ");
                        double side = myobj.nextDouble();
                        setSquare(double side);

                        break;
                
                    default:
                        break;
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        } while (condition);
    }
}
