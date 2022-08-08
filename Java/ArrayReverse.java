import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;

public class ArregloInversoStatic {
    public static void arregloInverso(String[] arreglo) {
        int total2 = arreglo.length;
        int total = arreglo.length;
        for (int i = 0; i < total2; i++) {
            String actual = arreglo[i];
            String inverso = arreglo[total - 1 - i];
            arreglo[i] = inverso;
            arreglo[total - 1 - i] = actual;
            total2--;
        }
    }
    public static void main(String[] args) {
            String[] productos = {"Kingston Pendrive 64GB", "Samsung Galaxy", "Disco Duro SSD Samsung Externo",
                    "Asus Notebook", "Macbook Air", "Chromecast 4ta generacion", "Bicicleta Oxford"};

            int total = productos.length;

        Arrays.sort(productos);
        arregloInverso(productos); //es como el reverse pero implementado por nosotros.
        //arregloInverso(productos)

        Collections.reverse(Arrays.asList(productos)); //Importado de java da reverso

        System.out.println("======Usando for =============");
        for(int i = 0; i < total; i ++){
            System.out.println("Para indice_" + i + " = " + productos[i]);
        }

    }
}
