
import java.util.Scanner;

public class Pino {
    public static void main(String[] args) {

        PineElementos parametro = new PineElementos();
        Scanner scanner = new Scanner(System.in);
        System.out.print("ingre el dato: ");
        parametro.size = scanner.nextInt();
        System.out.println("Ingrese el tamano del pino: " + parametro.size + " y el valor de n es igual a " + parametro.n + " inicialmente.");
        int nf = parametro.n;
        int s = parametro.size;

        while (nf < s){   //0 < 12
            for (int i = 0; i < (s/2)-(nf/2); i++){       //16/2
                System.out.print(" ");
            }
            for (int i= 1; i < nf; i++){
                System.out.print("*");


            }
            System.out.println();
            nf+=2;
        }
    }
}
