import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public final class Config {
    public static void load(boolean[][][] wynik) {
        try {
            File file = new File("config.txt");
            Scanner s = new Scanner(file);
            String line;
            for (int i = 0; i < wynik.length; i++) {
                for (int w = 0; w < 5; w++) {
                    line = s.nextLine();
                    for (int k = 0; k < 5; k++) {
                        if (line.charAt(k) - '0' == 1) wynik[i][w][k] = true;
                        else wynik[i][w][k] = false;
                    }
                    if (w == 4) line = s.nextLine();
                }
            }
        }
        catch (FileNotFoundException e) {
            System.out.println("Plik nie istnieję.");
            System.exit(0);
        }
        catch (Exception e) {
            System.out.println("Błąd w pliku konfiguracyjnym.");
            System.exit(0);
        }
    }
}
