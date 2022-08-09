public class EjemploClaseMath {
    public static void main(String[] args) {
            //Valor Real
        int absoluto = Math.abs(-3);
        System.out.println("absoluto = " + absoluto);
            //Valor Absoluto
        absoluto = Math.abs(3);
        System.out.println("absoluto = " + absoluto);
            //Valor mayor
        double max = Math.max(3.5, 1.2);
        System.out.println("max = " + max);
            //Valor menor
        double min = Math.min(3.5, 1.2);
        System.out.println("max = " + min);
            //valor maximo de un decimal
        double techo = Math.ceil(3.5);
        System.out.println("techo = " + techo);
            //Valor minimo redondear
        double piso = Math.floor(3.5);
        System.out.println("piso = " + piso);

        long entero = Math.round(3.5);
        System.out.println("entero = " + entero);

        long entero2 = Math.round(Math.PI);
        System.out.println("entero = " + entero2);

    }
}
