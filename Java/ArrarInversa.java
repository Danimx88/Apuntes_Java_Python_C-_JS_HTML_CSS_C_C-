import java.util.Arrays;

public class ForInversa {
    public static void main(String[] args) {

        String[] productos = new String [7];
        int total = productos.length;

        productos[0] = "Kingston Pendrive 64GB";
        productos[1] = "Samsung Galaxy";
        productos[2] = "Disco Duro SSD Samsung Externo";
        productos[3] = "Asus Notebook";
        productos[4] = "Macbook Air";
        productos[5] = "Chromecast 4ta generacion";
        productos[6] = "Bicicleta Oxford";

        Arrays.sort(productos); //Se ordenan elementos del arreglo
        System.out.println("====================== Usando for ===================================");
        for(int i = 0; i < total; i++){
            System.out.println("Para indice " + i + " : " + productos[i]);
        }

        for(int i = 0; i < total; i++){
            System.out.println("Para i = " + (total -1 - i) + " valor: " + productos[total-1-i]);
        }
    }
}
