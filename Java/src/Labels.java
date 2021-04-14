import javax.swing.*;

public class Labels extends Photos {
    JLabel gracz, gracz1, gracz2, computer, trwaGra, playWithComputer, playWithoutComputer, gameType;
    Labels(){
        czytajLabels();
    }
    private void czytajLabels() {
        try {
            gracz = new JLabel(imgGraczHighlighted);
            gracz1 = new JLabel(imgGracz1Highlighted);
            gracz2 = new JLabel(imgGracz2);
            computer = new JLabel(imgKomputer);
            trwaGra = new JLabel(imgTrwaGra);
            playWithComputer = new JLabel(imgPlayWithComputer);
            playWithoutComputer = new JLabel(imgPlayWithoutComputer);
            gameType = new JLabel(imgGameType);
        }
        catch (Exception e) {
            System.out.println("Błąd podczas wczytywania Labels.");
            System.exit(0);
        }
    }
}
