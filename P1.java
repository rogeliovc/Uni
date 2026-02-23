public class P1 {
    public static void main(String[] args) {
        int numeroOriginal = 43261596;
        
        // Llamamos a la función
        int resultado = reverseBits(numeroOriginal);
        
        System.out.println("Número original: " + numeroOriginal);
        System.out.println("Número invertido: " + resultado);
    }

    public static int reverseBits(int n) {
        int res = 0;
        for (int i = 0; i < 32; i++) {
            res <<= 1;
            res |= (n & 1);
            n >>>= 1;
        }
        return res;
    }
}