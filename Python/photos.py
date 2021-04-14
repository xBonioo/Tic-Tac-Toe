from PIL import Image, ImageTk

imgBlank = Image.open('images/blank.png')
photoBlank = ImageTk.PhotoImage(imgBlank)

imgCircle = Image.open('images/circle/circle.png')
imgCircleEndList = []
for i in range(1, 5):
    imgCircleEndList.append(Image.open('images/circle/circle_end' + str(i) + '.png'))

photoCircle = ImageTk.PhotoImage(imgCircle)
photoCircleEndList = []
for i in range(0, 4):
    photoCircleEndList.append(ImageTk.PhotoImage(imgCircleEndList[i]))

imgCross = Image.open('images/cross/cross.png')
imgCrossEndList = []
for i in range(1, 5):
    imgCrossEndList.append(Image.open('images/cross/cross_end' + str(i) + '.png'))
photoCross = ImageTk.PhotoImage(imgCross)
photoCrossEndList = []
for i in range(0, 4):
    photoCrossEndList.append(ImageTk.PhotoImage(imgCrossEndList[i]))

imgGracz = Image.open('images/subtitles/gracz.png')
photoGracz = ImageTk.PhotoImage(imgGracz)
imgGracz1 = Image.open('images/subtitles/gracz_1.png')
photoGracz1 = ImageTk.PhotoImage(imgGracz1)
imgGracz2 = Image.open('images/subtitles/gracz_2.png')
photoGracz2 = ImageTk.PhotoImage(imgGracz2)
imgKomputer = Image.open('images/subtitles/computer.png')
photoKomputer = ImageTk.PhotoImage(imgKomputer)

imgGraczHighlighted = Image.open('images/subtitles/gracz_highlighted.png')
photoGraczHighlighted = ImageTk.PhotoImage(imgGraczHighlighted)
imgGracz1Highlighted = Image.open('images/subtitles/gracz_1highlighted.png')
photoGracz1Highlighted = ImageTk.PhotoImage(imgGracz1Highlighted)
imgGracz2Highlighted = Image.open('images/subtitles/gracz_2highlighted.png')
photoGracz2Highlighted = ImageTk.PhotoImage(imgGracz2Highlighted)
imgKomputerHighlighted = Image.open('images/subtitles/computer_highlighted.png')
photoKomputerHighlighted = ImageTk.PhotoImage(imgKomputerHighlighted)

imgTrwaGra = Image.open('images/subtitles/gra_trwa.png')
photoTrwaGra = ImageTk.PhotoImage(imgTrwaGra)
imgWygralGracz1 = Image.open('images/subtitles/win_1.png')
photoWygralGracz1 = ImageTk.PhotoImage(imgWygralGracz1)
imgWygralGracz2 = Image.open('images/subtitles/win_2.png')
photoWygralGracz2 = ImageTk.PhotoImage(imgWygralGracz2)
imgWygralGracz = Image.open('images/subtitles/win_gracz.png')
photoWygralGracz = ImageTk.PhotoImage(imgWygralGracz)
imgWygralKomputer = Image.open('images/subtitles/win_computer.png')
photoWygralKomputer = ImageTk.PhotoImage(imgWygralKomputer)
imgRemis = Image.open('images/subtitles/remis.png')
photoRemis = ImageTk.PhotoImage(imgRemis)

imgStart = Image.open('images/subtitles/start.png')
photoStart = ImageTk.PhotoImage(imgStart)
imgNowaGra = Image.open('images/subtitles/new_game.png')
photoNowaGra = ImageTk.PhotoImage(imgNowaGra)
imgExit = Image.open('images/subtitles/exit.png')
photoExit = ImageTk.PhotoImage(imgExit)
imgUstawienia = Image.open('images/subtitles/settings.png')
photoUstawienia = ImageTk.PhotoImage(imgUstawienia)
imgBack = Image.open('images/subtitles/back.png')
photoBack = ImageTk.PhotoImage(imgBack)

imgPlayWithComputer = Image.open('images/subtitles/play_with_compuer.png')
photoPlayWithComputer  = ImageTk.PhotoImage(imgPlayWithComputer)
imgPlayWithoutComputer = Image.open('images/subtitles/play_without_compuer.png')
photoPlayWithoutComputer  = ImageTk.PhotoImage(imgPlayWithoutComputer)
imgGameType = Image.open('images/subtitles/tryb_gry.png')
photoGameType  = ImageTk.PhotoImage(imgGameType)
imgRozdzielczosc = Image.open('images/subtitles/rozdzielczosc.png')
photoRozdzielczosc  = ImageTk.PhotoImage(imgRozdzielczosc)