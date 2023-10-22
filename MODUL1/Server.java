package MODUL1;

import java.util.Scanner;

public class Server {

    public static void main(String[] args) {
        Server object1 = new Server();
        System.out.println("Selamat datang di Restoran EAD");
        System.out.println("Silahkan Register Terlebih Dahulu");
        System.out.println("==================================");

        Scanner keyboard = new Scanner(System.in);
        System.out.println("Nama: ");
        String registrasi_nama = keyboard.nextLine();
        String registrasi = object1.setNama(registrasi_nama);

        System.out.println("No. Handphone: ");
        int registrasi_no = keyboard.nextInt();
        int registrasi1 = object.setNo(registrasi_no);

        System.out.println("Register Success");
        System.out.println("Nama: ", registrasi);
        System.out.println("No. Handphone: ", registrasi1);

        System.out.println("====================================");
        System.out.println("1. Menu");
        System.out.println("2. Pilih Menu: ");
        System.out.println("3. Keluar");
        System.out.println("=====================================");

        
    }

}
        // TODO Create Menu

        // TODO Insert Menu to Database


        // TODO Display Main Menu

        // TODO Create User

        // Display Menu
