import javax.swing.*;

public class Photos {
    ImageIcon img;
    Icon imgBlank, imgCircle, imgCircleEnd1, imgCircleEnd2, imgCircleEnd3, imgCircleEnd4,
            imgCross, imgCrossEnd1, imgCrossEnd2, imgCrossEnd3, imgCrossEnd4,
            imgGracz1, imgGracz2, imgGracz1Highlighted, imgGracz2Highlighted,
            imgGracz, imgGraczHighlighted, imgKomputer, imgKomputerHighlighted,
            imgTrwaGra, imgRemis, imgWygralGracz1, imgWygralGracz2, imgWygralGracz, imgWygralKomputer,
            imgStart, imgExit, imgNowaGra, imgUstawienia, imgBack,
            imgPlayWithComputer, imgPlayWithoutComputer, imgGameType;
    Photos() {
        czytajObrazki();
    }
    private void czytajObrazki() {
        try {
            img = new ImageIcon("images/ikonka.png");
            imgBlank = new ImageIcon("images/blank.png");
            imgCircle = new ImageIcon("images/circle/circle.png");
            imgCircleEnd1 = new ImageIcon("images/circle/circle_end1.png");
            imgCircleEnd2 = new ImageIcon("images/circle/circle_end2.png");
            imgCircleEnd3 = new ImageIcon("images/circle/circle_end3.png");
            imgCircleEnd4 = new ImageIcon("images/circle/circle_end4.png");
            imgCross = new ImageIcon("images/cross/cross.png");
            imgCrossEnd1 = new ImageIcon("images/cross/cross_end1.png");
            imgCrossEnd2 = new ImageIcon("images/cross/cross_end2.png");
            imgCrossEnd3 = new ImageIcon("images/cross/cross_end3.png");
            imgCrossEnd4 = new ImageIcon("images/cross/cross_end4.png");
            imgGracz = new ImageIcon("images/subtitles/gracz.png");
            imgGracz1 = new ImageIcon("images/subtitles/gracz_1.png");
            imgGracz2 = new ImageIcon("images/subtitles/gracz_2.png");
            imgKomputer = new ImageIcon("images/subtitles/computer.png");
            imgGraczHighlighted = new ImageIcon("images/subtitles/gracz_highlighted.png");
            imgGracz1Highlighted = new ImageIcon("images/subtitles/gracz_1highlighted.png");
            imgGracz2Highlighted = new ImageIcon("images/subtitles/gracz_2highlighted.png");
            imgKomputerHighlighted = new ImageIcon("images/subtitles/computer_highlighted.png");
            imgTrwaGra = new ImageIcon("images/subtitles/gra_trwa.png");
            imgWygralGracz1 = new ImageIcon("images/subtitles/win_1.png");
            imgWygralGracz2 = new ImageIcon("images/subtitles/win_2.png");
            imgWygralGracz = new ImageIcon("images/subtitles/win_gracz.png");
            imgWygralKomputer = new ImageIcon("images/subtitles/win_computer.png");
            imgRemis = new ImageIcon("images/subtitles/remis.png");
            imgStart = new ImageIcon("images/subtitles/start.png");
            imgNowaGra = new ImageIcon("images/subtitles/new_game.png");
            imgExit = new ImageIcon("images/subtitles/exit.png");
            imgUstawienia = new ImageIcon("images/subtitles/settings.png");
            imgBack = new ImageIcon("images/subtitles/back.png");
            imgPlayWithComputer = new ImageIcon("images/subtitles/play_with_compuer.png");
            imgPlayWithoutComputer = new ImageIcon("images/subtitles/play_without_compuer.png");
            imgGameType = new ImageIcon("images/subtitles/tryb_gry.png");
        }
        catch (Exception e) {
            System.out.println("Błąd podczas wczytywania zdjęć.");
            System.exit(0);
        }
    }

}
