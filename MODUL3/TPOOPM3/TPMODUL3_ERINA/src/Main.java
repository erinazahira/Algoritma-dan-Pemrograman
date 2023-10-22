import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        try (Scanner inputorder = new Scanner(System.in)) {
            Restaurant resto = new Restaurant();
            int orderQty, customerID;

            try {
                System.out.println("Enter customer ID: ");
                customerID = inputorder.nextInt();

                System.out.println("Enter the number of food: ");
                orderQty = inputorder.nextInt();

                Thread tsatu = new Thread(resto);
                Waiters waiter = new Waiters(orderQty, customerID);
                Thread tdua = new Thread(waiter);

                tsatu.start();
                tdua.start();
                tsatu.join();
                tdua.join();

            } catch (Exception a) {
                System.out.println("Input must be integer");
            }
        }
    }
}
