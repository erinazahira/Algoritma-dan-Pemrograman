public class Calculation implements Runnable{
    double radius;
    double side;
    double area;
    double phi = 3.14;
    
    public void setSquare(double side, double area) {
        this.side = side;
        this.area = area;
        area = side*side;
    }

    public double getSquare() {
        return this.area;
    }

    public void setCircle(double radius, double phi, double area) {
        this.radius = radius;
        this.area = area;
        area = phi * radius * radius;
    }

    public double getCircle() {
        return this.area;
    }

    public void setTrapezoid(double a, double b, double t, double area) {
        this.area = area;
        area = 0.5 * t * (a+b);
    }

    public double getTrapezoid() {
        return this.area;
    }

    @Override
    public void run() {
        System.out.println("Program will start in");
        for (int i = 3; i > 0; i--) {
            System.out.println(i);
        }
        try {
            Thread.sleep(5000);
        } catch (Exception e) {
            e.printStackTrace();
    }
}