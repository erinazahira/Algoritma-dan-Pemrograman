public class Waiters implements Runnable {
    private final int orderQty;
    private final int customerID;
    static int foodPrice = 30000;

    public Waiters(int orderQty, int customerID) {
        this.orderQty = orderQty;
        this.customerID = customerID;
    }

    public void run() {
        // call getCoffee method and pending it to 5000 ms
        while (true) {
            makeFood();
            try {
                Thread.sleep(15000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    public void orderInfo() {

        System.out.println("----------------------------------------");

        System.out.println("Customer ID: "+ this.customerID);
        System.out.println("Number of food: "+ this.orderQty);
        System.out.println("Total price: "+ foodPrice * this.orderQty);

        System.out.println("----------------------------------------");
    }

    public void makeFood() {
        synchronized(Restaurant.getLock()) {

            System.out.println("Waiters: Food is ready to deliver");
            Restaurant restaurant = new Restaurant();
            restaurant.setWaitingForPickup(false);

            if (Restaurant.getFoodNumber() == this.orderQty + 1) {
                orderInfo();
                System.exit(0);
            }
            Restaurant.getLock().notifyAll();
            System.out.println("Waiters: Tell the restaurant to make another food\n");
        }
    }

}
