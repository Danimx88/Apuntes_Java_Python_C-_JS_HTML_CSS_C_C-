public class ClaseRandom {
    public static void main(String[] args) {

        double random = Math.random();           //Valor random de 0 a 0.99999
        System.out.println("random = " + random);
        random *= 7;

        System.out.println("random = " + random);

        random = Math.floor(random);
        System.out.println("random = " +random);

        String[] colores = {"azul", "gris", "verde", "morado", "rosa", "blanco", "negro", "rojo"};
        double random2 = Math.random();
        random2 *= colores.length;
        random = Math.floor(random2);
        System.out.println("random2 = " +random2);
        
        System.out.println("colores = " + colores[(int) random2]);
        
    }
}
