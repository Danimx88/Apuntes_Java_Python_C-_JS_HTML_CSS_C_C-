import javax.swing.plaf.synth.SynthOptionPaneUI;
import java.util.Calendar;
/*
*
* @author DanielRomero
* 28 / 07 / 2022
*
 */
public class TipoVariablesJava {
    public static void main(String[] args) {
        String saludo = "Variables en Java";
        System.out.println(saludo);
        System.out.println("saludo.toUpperCase() = " + saludo.toUpperCase());

        //Variables booleanas
        boolean vbf = false;  //Variable booleana valor false
        boolean vbt = true;   //Variable booleana valor true

        //Variables char
        char vc1 = 'a';      //Variable char valor a
        char vc2 = '1';      //Variable char valor 1
        char vc3 = '\u0021'; //Variable char valor \u0021

        //Variables Enteras
        byte enteroByte = 127;                  //Variable con valor entre -128 a 127
        short enteroShort = 32767;              //Variable con valor entre -32768 a 32767
        int enteroInt = 2147483647;             //Variable con valor entre -2147483648 a 2147483647
        long enteroLong = 922372036854775807L;  //Variable con valor entre -922372036854775808 a 922372036854775807L

        //Variables de Números Reales
        float realFloat = 3.1416f;          //Variable con valor entre -1.4E-45 a 3.4028235E38
        double realDouble = 4.7029235E3;    //Variable con valor entre -4.9E-324 a 1.7976931348623157e308

        if(vbf){
            System.out.println("Valor de booleano es: true");
        }else{
            System.out.println("Valor de booleano es: false");
        }

        System.out.println("Valor de booleano 1: " + vbf);
        System.out.println("Valor de booleano 2: " + vbt);
        System.out.println("boolean puede ser " + vbf + " y " + vbt);
        vbt = realFloat < realDouble;
        System.out.println("vbt" + vbt);

        char simbolo = '@';
        System.out.println(simbolo);
        System.out.println("simbolo = vc1: " + (simbolo == vc1));
        System.out.println("tipoChar = " + vc1);
        char espacio = '\u0020';
        char retroceso = '\b';
        char tabulador = '\t';
        char nuevaLinea = '\n';
        char retornoCarro = '\r';
        System.out.println("tipo byte correspondiente en byte a " + Character.BYTES);
        System.out.println("tipo byte correspondiente en bites a " + Character.SIZE);
        System.out.println("Valor maximo de un chat " + Character.MAX_VALUE);
        System.out.println("Valor minimo de un char " + Character.MIN_VALUE);

        System.out.println("enteroByte = " + enteroByte);
        System.out.println("tipo byte correspondiente en byte a " + Byte.BYTES);
        System.out.println("tipo byte correspondiente en bites a " + Byte.SIZE);
        System.out.println("Valor maximo de un byte " + Byte.MAX_VALUE);
        System.out.println("Valor minimo de un byte " + Byte.MIN_VALUE);

        System.out.println("enteroShort = " + enteroShort);
        System.out.println("tipo short correspondiente en byte a " + Short.BYTES);
        System.out.println("tipo short correspondiente en bites a " + Short.SIZE);
        System.out.println("Valor maximo de un short " + Short.MAX_VALUE);
        System.out.println("Valor minimo de un short " + Short.MIN_VALUE);

        System.out.println("enteroInt = " + enteroInt);
        System.out.println("tipo int correspondiente en byte a " + Integer.BYTES);
        System.out.println("tipo int correspondiente en bites a " + Integer.SIZE);
        System.out.println("Valor maximo de un int " + Integer.MAX_VALUE);
        System.out.println("Valor minimo de un int " + Integer.MIN_VALUE);

        System.out.println("enteroLong = " + enteroLong);
        System.out.println("tipo long correspondiente en byte a " + Long.BYTES);
        System.out.println("tipo long correspondiente en bites a " + Long.SIZE);
        System.out.println("Valor maximo de un long " + Long.MAX_VALUE);
        System.out.println("Valor minimo de un long " + Long.MIN_VALUE);

        System.out.println("enteroLong = " + realFloat);
        System.out.println("tipo float correspondiente en byte a " + Float.BYTES);
        System.out.println("tipo float correspondiente en bites a " + Float.SIZE);
        System.out.println("Valor maximo de un float " + Float.MAX_VALUE);
        System.out.println("Valor minimo de un float " + Float.MIN_VALUE);

        System.out.println("enteroDouble = " + realDouble);
        System.out.println("tipo bouble correspondiente en byte a " + Double.BYTES);
        System.out.println("tipo double correspondiente en bites a " + Double.SIZE);
        System.out.println("Valor maximo de un double " + Double.MAX_VALUE);
        System.out.println("Valor minimo de un double " + Double.MIN_VALUE);





    }
}
