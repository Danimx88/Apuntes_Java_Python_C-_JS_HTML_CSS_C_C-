import java.util.Arrays;

public class EjemploArregloForInversoMutable {
    public static void main(String[] args) {
        String[] productos = {"Kingston Pendrive 64GB", "Samsung Galaxy", "Disco Duro SSD Samsung Externo",
                "Asus Notebook", "Macbook Air", "Chromecast 4ta generacion", "Bicicleta Oxford"};

        int total = productos.length;

        Arrays.sort(productos);
        System.out.println("=====================================  Usando for ======================================");
        for (int i = 0; i < total; i++){
            System.out.println("Para indice_" + i + " : " + productos[i]);
        }

        for(int i = 0; i < total/2; i++){
            String actual = productos[i];
            String inverso = productos[total-1-i];
            productos[i] = inverso;
            productos[total-1-i] = actual;
        }

        System.out.println("======================================= Usando for =====================================");
        for(int i = 0; i< total; i++){
            System.out.println("Para indice " + i + " : " + productos[i]);
        }
    }
}
