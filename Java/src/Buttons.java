import javax.swing.*;

public class Buttons extends Photos {
    JButton start, exit, nowaGra, ustawienia, back;
    Buttons() {
        czytajButtons();
    }
    private void czytajButtons() {
        try {
            start = new JButton(imgStart);
            nowaGra = new JButton(imgNowaGra);
            exit = new JButton(imgExit);
            ustawienia = new JButton(imgUstawienia);
            back = new JButton(imgBack);
        }
        catch (Exception e) {
            System.out.println("Błąd podczas wczytywania Buttons.");
            System.exit(0);
        }
    }
}
