import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.Random;

public class Gra extends JFrame implements ActionListener {
    private final JButton[] buttons = new JButton[25];
    private final JRadioButton radioWithoutBot, radioWithBot;
    private final JLabel endWin;

    private final boolean[][][] wynik = new boolean[21][5][5];
    private final boolean[][][] board = new boolean[2][5][5];

    private int gameType = 0;
    private int queue = 0;
    private boolean bot = false;
    private boolean game = false;
    private boolean bTrwaGra = false;

    private final String[] type = {"3x3", "4x4", "5x5"};
    private final JComboBox cType = new JComboBox(type);

    private final ArrayList<Integer> playerMoves = new ArrayList<Integer>();
    private final ArrayList<Integer> botMoves = new ArrayList<Integer>();

    private final Photos p = new Photos();
    private final Buttons b = new Buttons();
    private final Labels l = new Labels();

    public Gra() {
        Config.load(wynik);

        setTitle("Kółko i krzyżyk");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setExtendedState(JFrame.MAXIMIZED_BOTH);
        setIconImage(p.img.getImage());
        setResizable(false);
        setLocationRelativeTo(null);
        setLayout(null);
        setVisible(true);

        radioWithBot = new JRadioButton();
        radioWithoutBot = new JRadioButton();
        endWin = l.trwaGra;

        radioWithoutBot.setSelected(true);

        startMenu();
    }

    public void startMenu()  {
        b.start.setBounds(800,200,210,210);
        b.ustawienia.setBounds(800,410,210,210);
        b.exit.setBounds(1650,825,210,210);

        add(b.start);
        add(b.ustawienia);
        add(b.exit);

        b.start.addActionListener(this);
        b.ustawienia.addActionListener(this);
        b.exit.addActionListener(this);
    }

    public void startGame() {
        if (bTrwaGra) return;
        gameType = cType.getSelectedIndex();
        remove(b.start);
        remove(b.ustawienia);
        remove(b.exit);
        repaint();
        bTrwaGra = true;
        game = true;
        for (int i = 0; i < (gameType+3) * (gameType+3); i++) {
            buttons[i] = new JButton();
            buttons[i].addActionListener(new Silnik());

            if (i < 3 + gameType)
                buttons[i].setBounds(300 + (i*210), 90-(40*gameType), 210, 210);
            else if (i >= 3 + gameType && i < 6 + (gameType*2))
                buttons[i].setBounds(300 + ((i - (3 + gameType))*210), 300-(40*gameType), 210, 210);
            else if (i >= 6 + (gameType*2) && i < 9 + (gameType*3))
                buttons[i].setBounds(300 + ((i - (3 + gameType)*2)*210), 510-(40*gameType), 210, 210);
            else if (i >= 9 + (gameType*3) && i < 12 + (gameType*4))
                buttons[i].setBounds(300 + ((i - (3 + gameType)*3)*210), 720-(40*gameType), 210, 210);
            else
                buttons[i].setBounds(300 + ((i - (3 + gameType)*4)*210), 930-(40*gameType), 210, 210);

            add(buttons[i]);
        }
        if (bot) {
            l.gracz.setBounds(90, 300, 210, 210);
            l.computer.setBounds(300 + ((3 + gameType) * 210), 300, 210, 210);
            add(l.gracz);
            add(l.computer);
        }
        else {
            l.gracz1.setBounds(90, 300, 210, 210);
            l.gracz2.setBounds(300 + ((3 + gameType) * 210), 300, 210, 210);
            add(l.gracz1);
            add(l.gracz2);
        }
        b.nowaGra.setBounds(1650, 10, 210, 210);
        b.back.setBounds(1440, 825, 210, 210);
        b.exit.setBounds(1650, 825, 210, 210);
        add(b.nowaGra);
        add(b.back);
        b.nowaGra.addActionListener(this);
        b.back.addActionListener(this);
        add(b.exit);
        endWin.setBounds(1440, 10, 210, 210);
        add(endWin);
    }

    public void settings() {
        remove(b.start);
        remove(b.ustawienia);
        remove(b.exit);
        repaint();

        l.playWithComputer.setBounds(250,100,210,210);
        l.playWithoutComputer.setBounds(460,100,210,210);
        l.gameType.setBounds(250,450,210,210);
        add(l.playWithoutComputer);
        add(l.playWithComputer);
        add(l.gameType);

        cType.setBounds(290, 650, 100, 25);
        add(cType);

        radioWithBot.setBounds(340, 300, 20, 20);
        radioWithoutBot.setBounds(560, 300, 20, 20);
        ButtonGroup g = new ButtonGroup();
        g.add(radioWithBot);
        g.add(radioWithoutBot);
        add(radioWithBot);
        add(radioWithoutBot);

        b.back.setBounds(1440,825,210,210);
        b.exit.setBounds(1650,825,210,210);
        add(b.back);
        add(b.exit);

        b.back.addActionListener(this);
        b.exit.addActionListener(this);
    }

    public void reset(boolean gra) {
        Photos p = new Photos();
        for (int i = 0; i < (gameType+3) * (gameType+3); i++) {
            buttons[i].setEnabled(true);
            buttons[i].setIcon(p.imgBlank);
        }
        playerMoves.clear();
        botMoves.clear();
        queue = 0;
        endWin.setIcon(p.imgTrwaGra);
        bTrwaGra = gra;
        for (int x = 0; x < 2; x++) {
            for (int k = 0; k < 3 + gameType; k++) {
                for (int w = 0; w < 3 + gameType; w++) {
                    board[x][w][k] = false;
                }
            }
        }
        if (bot) {
            l.gracz.setIcon(p.imgGraczHighlighted);
            l.computer.setIcon(p.imgKomputer);
        }
        else {
            l.gracz1.setIcon(p.imgGracz1Highlighted);
            l.gracz2.setIcon(p.imgGracz2);
        }
    }

    private class Silnik implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            for (int i = 0; i < (gameType+3) * (gameType+3); i++) {
                if (e.getSource() == buttons[i]) {
                    addFieldToPlayer(i);
                    playerMoves.add(i);
                    break;
                }
            }

            JButton buttonClicked = (JButton) e.getSource();
            buttonClicked.setIcon(chceckImage(queue % 2));
            buttonClicked.setEnabled(false);

            playerCheck(queue % 2);
            if (bot) botMove();
        }

        public Icon chceckImage(int num) {
            if (num == 0)
                return p.imgCircle;
            return p.imgCross;
        }

        public void playerCheck(int num) {
            for (int i = 0; i < wynik.length; i++) {
                int[] fields = new int[25];
                int field_num = 0;
                for (int k = 0; k < 3 + gameType; k++) {
                    for (int w = 0; w < 3 + gameType; w++) {
                        if (wynik[i][w][k] && board[num][w][k]) {
                            fields[field_num++] = k + (w * (3 + gameType));
                        }
                    }
                }
                if (field_num >= 3) {
                    if (fields[0] == fields[1] - 1) {
                        if (fields[1] == fields[2] - 1) {
                            endMessage(num, buttons[fields[0]], buttons[fields[1]], buttons[fields[2]], 0);
                            return;
                        }
                    }
                    if (fields[0] + 3 + gameType == fields[1]) {
                        if (fields[1] + 3 + gameType == fields[2]) {
                            endMessage(num, buttons[fields[0]], buttons[fields[1]], buttons[fields[2]], 1);
                            return;
                        }
                    }
                    if (fields[0] + 4 + gameType == fields[1]) {
                        if (fields[1] + 4 + gameType == fields[2]) {
                            endMessage(num, buttons[fields[0]], buttons[fields[1]], buttons[fields[2]], 2);
                            return;
                        }
                    }
                    if (fields[2] + 2 + gameType == fields[1]) {
                        if (fields[1] + 2 + gameType == fields[0]) {
                            endMessage(num, buttons[fields[0]], buttons[fields[1]], buttons[fields[2]], 3);
                            return;
                        }
                    }
                }
            }
            int remis = 0;
            for (int x = 0; x < 2; x++) {
                for (int k = 0; k < 3 + gameType; k++) {
                    for (int w = 0; w < 3 + gameType; w++) {
                        if (board[x][w][k]) remis++;
                    }
                }
            }
            if (remis == (gameType + 3) * (gameType + 3)) {
                endMessage(2, buttons[0], buttons[0], buttons[0], 0);
                return;
            }
            queue++;
            highlight();
        }

        public void highlight() {
            if (bot) {
                if (queue%2 == 0) {
                    l.gracz.setIcon(p.imgGraczHighlighted);
                    l.computer.setIcon(p.imgKomputer);
                }
                else {
                    l.gracz.setIcon(p.imgGracz);
                    l.computer.setIcon(p.imgKomputerHighlighted);
                }
            }
            else {
                if (queue%2 == 0) {
                    l.gracz1.setIcon(p.imgGracz1Highlighted);
                    l.gracz2.setIcon(p.imgGracz2);
                }
                else {
                    l.gracz1.setIcon(p.imgGracz1);
                    l.gracz2.setIcon(p.imgGracz2Highlighted);
                }
            }
        }

        public void addFieldToPlayer(int num) {
            if (num >= 0 && num < 3 + gameType)
                board[queue % 2][0][num] = true;
            else if (num >=3 + gameType && num <6 + (gameType * 2))
                board[queue % 2][1][num - (3 + gameType)] = true;
            else if (num >=6 + (gameType * 2) && num <9 + (gameType * 3))
                board[queue % 2][2][num - (6 + (gameType * 2))] = true;
            else if (num >=9 + (gameType * 3) && num <12 + (gameType * 4))
                board[queue % 2][3][num - (9 + (gameType * 3))] = true;
            else
                board[queue % 2][4][num - (12 + (gameType * 4))] = true;
        }

        public void endMessage(int num, JButton filed1, JButton filed2, JButton filed3, int type) {
            bTrwaGra = false;
            endWin.setIcon(endImage(num));
            for (int i = 0; i < (gameType+3) * (gameType+3); i++) buttons[i].setEnabled(false);
            if (num == 2)
                return;

            JButton[] fields = new JButton[3];
            fields[0] = filed1;
            fields[1] = filed2;
            fields[2] = filed3;
            for (JButton b : fields) {
                if (num == 0) {
                    switch (type) {
                        case 0 -> b.setIcon(p.imgCircleEnd1);
                        case 1 -> b.setIcon(p.imgCircleEnd2);
                        case 2 -> b.setIcon(p.imgCircleEnd3);
                        case 3 -> b.setIcon(p.imgCircleEnd4);
                    }
                }
                else {
                    switch (type) {
                        case 0 -> b.setIcon(p.imgCrossEnd1);
                        case 1 -> b.setIcon(p.imgCrossEnd2);
                        case 2 -> b.setIcon(p.imgCrossEnd3);
                        case 3 -> b.setIcon(p.imgCrossEnd4);
                    }
                }
            }
        }

        public Icon endImage(int num) {
            if (bot) {
                if (num == 0)
                    return p.imgWygralGracz;
                else if (num == 1)
                    return p.imgWygralKomputer;
            }
            else {
                if (num == 0)
                    return p.imgWygralGracz1;
                else if (num == 1)
                    return p.imgWygralGracz2;
            }
            return p.imgRemis;
        }

        public boolean checkFieldState(int num) {
            for (int i = 0; i < botMoves.size(); i++) {
                if (num == botMoves.get(i))
                    return true;
            }
            for (int i = 0; i < playerMoves.size(); i++) {
                if (num == playerMoves.get(i))
                    return true;
            }
            return false;
        }

        public void botMove() {
            if (!bTrwaGra) return;

            Random rand = new Random();
            int los = 0;
            while (true) {
                los = rand.nextInt(((gameType+3) * (gameType+3))-1);
                if (checkFieldState(los))
                    continue;
                break;
            }
            botMoves.add(los);
            buttons[los].setIcon(chceckImage(queue % 2));
            buttons[los].setEnabled(false);
            addFieldToPlayer(los);
            playerCheck(queue % 2);
        }
    }

    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == b.start) startGame();
        else if (e.getSource() == b.ustawienia) settings();
        else if (e.getSource() == b.nowaGra) {
            reset(true);
            repaint();
        }
        else if (e.getSource() == b.exit) {
            int result = JOptionPane.showConfirmDialog(null, "Czy na pewno chcesz wyjść?", "Exit", JOptionPane.YES_NO_OPTION);
            if (result == JOptionPane.YES_OPTION) {
                System.exit(0);
            }
        }
        else if (e.getSource() == b.back) {
            if (game) {
                int result = JOptionPane.showConfirmDialog(null, "Czy na pewno chcesz wrócić?", "Back", JOptionPane.YES_NO_OPTION);
                if (result == JOptionPane.YES_OPTION) {
                    reset(false);
                    for (int i = 0; i < (gameType+3) * (gameType+3); i++)
                        remove(buttons[i]);
                    if (bot) {
                        remove(l.gracz);
                        remove(l.computer);
                    }
                    else {
                        remove(l.gracz1);
                        remove(l.gracz2);
                    }
                    remove(b.nowaGra);
                    remove(b.back);
                    remove(endWin);
                    repaint();
                    game = false;
                    bTrwaGra = false;
                    startMenu();
                }
            }
            else {
                remove(l.playWithoutComputer);
                remove(l.playWithComputer);
                remove(l.gameType);
                remove(cType);
                remove(radioWithBot);
                remove(radioWithoutBot);
                remove(b.back);
                repaint();
                startMenu();
            }
        }

        if (radioWithBot.isSelected()) bot = true;
        else if (radioWithoutBot.isSelected()) bot = false;
    }



    public static void main(String[] args) {
        try {
            new Gra();
        }
        catch (Exception e) {
            System.out.println("Błąd podczas włącznia gry.");
            System.exit(0);
        }
    }
}