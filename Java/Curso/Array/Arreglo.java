public class Arreglo {
    public static void main(String[] args) {
        int[] arreglo = {1, 2, 3, 4, 5, 6, 7, 8};
        int total = arreglo.length;


        for (int i = 0; i <= total-1; i++){
            int resto = arreglo[i] % 2;
            if (resto == 0){
                System.out.println("El valor de " + (i+1) + " es PAR");
            }else {
                int resto1 = arreglo[i] + 9;
                System.out.println("El " + (i+1) + " es IMPAR y se le suma 9 = " + resto1);
            }
        }
    }
}
