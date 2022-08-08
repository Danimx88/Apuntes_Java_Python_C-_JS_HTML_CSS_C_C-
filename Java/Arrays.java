import java.lang.reflect.Array;
import java.util.Arrays;

public class IterarInversa {
    public static void main(String[] args) {
        int[] var_1 = {1, 2, 3, 4, 5, 6};
        String[] names = {"Daniel", "Omar", "Jose", "Pepe", "Susana"};

        //For//
        for (int i = 0; i < var_1.length; i ++){
            System.out.println("Numeros = " + var_1[i]);
        }
        System.out.println(" "); //Utilizo un println solo para dejar espacio
        for (int i = 0; i < names.length; i++) {
            System.out.println("Nombres = " + names[i]);
        }
        //For Each
        System.out.println(" "); //Utilizo un println solo para dejar espacio
        for (int nm:var_1){
            System.out.println("Numeros con For-each: " + nm);
        }
        System.out.println(" "); //Utilizo un println solo para dejar espacio
        for (String nom:names){
            System.out.println("Nombres con For-each: " + nom);
        }

        int[] numeros = new int[5];

        numeros[0] = 1;
        numeros[1] = Integer.valueOf("2");
        numeros[2] = (int)3L;
        numeros[3] = 4;
        numeros[4] = 5;
        // nunmeros[5] = 5 ---> No se de debe de asignar a la cadena mas valores de los que tiene, error!

        int ii = numeros[0];
        int jj = numeros[1];
        int kk = numeros[2];
        int ll = numeros[3];
        int mm = numeros[4];
        int nn = numeros[numeros.length-1];
        System.out.println(" "); //Utilizo un println solo para dejar espacio
        System.out.println("i = " + ii);
        System.out.println("j = " + jj);
        System.out.println("k = " + kk);
        System.out.println("l = " + ll);
        System.out.println("m = " + mm);
        System.out.println("n = " + nn);

        System.out.println(" "); //Utilizo un println solo para dejar espacio

        String[] productos_0 = new String[7];
        System.out.println("prodcutos_0 [0] = " + productos_0[0]);  //Valor NULL ya que no tiene valor asignado
        System.out.println("prodcutos_0 [1] = " + productos_0[0]);  //Valor NULL ya que no tiene valor asignado
        System.out.println("prodcutos_0 [2] = " + productos_0[0]);  //Valor NULL ya que no tiene valor asignado
        System.out.println("prodcutos_0 [3] = " + productos_0[0]);  //Valor NULL ya que no tiene valor asignado
        System.out.println("prodcutos_0 [4] = " + productos_0[0]);  //Valor NULL ya que no tiene valor asignado
        System.out.println("prodcutos_0 [5] = " + productos_0[0]);  //Valor NULL ya que no tiene valor asignado
        System.out.println("prodcutos_0 [6] = " + productos_0[0]);  //Valor NULL ya que no tiene valor asignado
        System.out.println("prodcutos_0 [7] = " + productos_0[0]);  //Valor NULL ya que no tiene valor asignado

        String[] productos_1 = new String [7];
        productos_1[0] = "Kingston Pendrive 64GB";
        productos_1[1] = "Samsung Galaxy";
        productos_1[2] = "Disco Duro SSD Samsung Externo";
        productos_1[3] = "Asus Notebook";
        productos_1[4] = "Macbook Air";
        productos_1[5] = "Chromecast 4ta generacion";
        productos_1[6] = "Bicicleta Oxford";

        Arrays.sort(productos_1); //Acomoda elementos por orden

        String prod1 = productos_1[0];
        String prod2 = productos_1[1];
        String prod3 = productos_1[2];
        String prod4 = productos_1[3];
        String prod5 = productos_1[4];
        String prod6 = productos_1[5];
        String prod7 = productos_1[6];

        System.out.println(" "); //Utilizo un println solo para dejar espacio
        System.out.println("producto_1[0] = " + productos_1[0]);
        System.out.println("producto_1[1] = " + productos_1[1]);
        System.out.println("producto_1[2] = " + productos_1[2]);
        System.out.println("producto_1[3] = " + productos_1[3]);
        System.out.println("producto_1[4] = " + productos_1[4]);
        System.out.println("producto_1[5] = " + productos_1[5]);
        System.out.println("producto_1[6] = " + productos_1[6]);
        System.out.println(" "); //Utilizo un println solo para dejar espacio
        System.out.println("prod1 = " + prod1);
        System.out.println("prod2 = " + prod2);
        System.out.println("prod3 = " + prod3);
        System.out.println("prod4 = " + prod4);
        System.out.println("prod5 = " + prod5);
        System.out.println("prod6 = " + prod6);
        System.out.println("prod7 = " + prod7);
        System.out.println(" "); //Utilizo un println solo para dejar espacio
//////////////////////For/////////////////FOR/////////////FOR//////////////////////////////FOR/////////////////////////////////////7

        String[] productos_2 = new String [7];
        ///////SE VA A MOSTRAR PURO NULL PORQUE AUN NO SE LE ASIGAN LOS VALORES AL ARREGLO//////////////////////////
        int total = productos_2.length;
            for (int i = 0; i < total; i++ ){
                System.out.println("Recorrido = " + i + " : " + productos_2[i]);
        }
        System.out.println(" "); //Utilizo un println solo para dejar espacio
        productos_2[0] = "Camisa azul";
        productos_2[1] = "Blusa gris";
        productos_2[2] = "Corbata negra";
        productos_2[3] = "Sudadera verde";
        productos_2[4] = "Bufanda negra";
        productos_2[5] = "Tenis nike 403-327";
        productos_2[6] = "Zapato modelo 92-3782";
//////////////VALORES ASIGNADOR AL ARREGLO, SE MUESTRA AHORA LA CADENA CORRECTAMENTE EN EL FOR///////////////////////77
        for (int i = 0; i < total; i++ ){
            System.out.println("Recorrido = " + i + " : " + productos_2[i]);
        }
        System.out.println(" "); //Utilizo un println solo para dejar espacio
/////////////////AHORA CON SORT PARA QUE ORDENE LOS ELEMENTOS///////////////////////////////////////////////////////7777
        Arrays.sort(productos_2);
        for (int i = 0; i < total; i++ ){
            System.out.println("Recorrido usando sort = " + i + " : " + productos_2[i]);
        }
        System.out.println(" "); //Utilizo un println solo para dejar espacio
        System.out.println("========================Usando While==============================");
        int i = 0;
        while (i < total){
            System.out.println("Para indice " + i + " : " + productos_2[i]);
            i ++;
        }

        System.out.println("=================Usando do---While==============================");
        int j = 0;
        do{
            System.out.println("Para indice " + j + " : " + productos_2[j]);
            j++;
        } while (j < total);
            //System.out.println("Para indice " + i + " : " + productos_2[i]);
        System.out.println(" "); ///Espacio
        int[] number = new int[11];

        int totalNumber = number.length;

        for (int k = 1; k < totalNumber; k++){
            number[k] = k*3;
        }

        for (int k = 0; k < totalNumber; k++){
            System.out.println("3 X "+ (k) + " = " + number[k]);
        }


    }
}
