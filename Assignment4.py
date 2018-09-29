from tkinter import *
from tkinter import messagebox
from time import localtime, strftime


class Game:
    def __init__(self):
        '''Inisiasi dari kelas Game dan membuat main menu dari game'''
        mainMenu = Tk()
        mainMenu.title('M,N,K Game')
        mainMenu.iconbitmap(default='DOTA 2.ico')
        labelBaris = Label(mainMenu, text='Row:')
        labelKolom = Label(mainMenu, text='Column:')
        labelCond = Label(mainMenu, text='Win Condition:')
        self.baris = IntVar()
        entryBaris = Entry(mainMenu, textvariable=self.baris)
        self.kolom = IntVar()
        entryKolom = Entry(mainMenu, textvariable=self.kolom)
        self.winCond = IntVar()
        entryWinCond = Entry(mainMenu, textvariable=self.winCond)
        entryWinCond.bind('<Return>', self.playGame)
        tombol = Button(mainMenu, text='Play!',
                        command=lambda x='gg': self.playGame(x))
        tombol2 = Button(mainMenu, text='History',
                         command=lambda x='gg': self.buttonHistory(x))
        self.player1 = StringVar()
        self.player2 = StringVar()
        labelPlayer1 = Label(mainMenu, text='Player 1:')
        labelPlayer2 = Label(mainMenu, text='Player 2:')
        entryPlayer1 = Entry(mainMenu, textvariable=self.player1)
        entryPlayer2 = Entry(mainMenu, textvariable=self.player2)
        entryPlayer2.bind('<Return>', self.playGame)
        canvasMenu = Canvas(mainMenu, width=200, height=100)
        canvasMenu.create_text(
            100, 50, text="MNK Game\nBy: TheSagab\nCSUI 2016", justify='center')
        canvasMenu.grid(column=0, columnspan=5, row=0, rowspan=2)
        labelBaris.grid(column=0, row=2, sticky=W)
        entryBaris.grid(column=1, row=2, sticky=W)
        labelKolom.grid(column=0, row=3, sticky=W)
        entryKolom.grid(column=1, row=3, sticky=W)
        labelCond.grid(column=0, row=4, sticky=W)
        entryWinCond.grid(column=1, row=4, sticky=W)
        tombol.grid(column=1, row=5, sticky=E)
        tombol2.grid(column=2, row=5, sticky=W)
        labelPlayer1.grid(column=2, row=2)
        entryPlayer1.grid(column=3, row=2)
        labelPlayer2.grid(column=2, row=3)
        entryPlayer2.grid(column=3, row=3)
        mainMenu.mainloop()

    def buttonHistory(self, event):
        '''Tombol untuk mengeluarkan window history'''
        windowHistory = Tk()
        container = Frame(windowHistory)
        textWindow = Text(container)
        scrollbar = Scrollbar(container)
        scrollbar.pack(side="right", fill="y")
        textWindow.pack(side="left", fill="both", expand=True)
        with open('history.txt', 'r') as file:
            text = file.read()
        textWindow.insert(END, text)
        container.pack()
        windowHistory.mainloop()

    def playGame(self, event):
        '''Saat menekan tombol, membuat window canvas dan membuat rectangle
        yang dapat berubah warna saat dipencet'''
        try:
            game = Tk()
            self.playArea = Canvas(game)
            self.playArea.pack()
            self.turn = 0
            self.listMNK = []
            self.draw = self.baris.get() * self.kolom.get()
            self.winCond.get()
            self.playArea.config(width=self.baris.get() * 33,
                                 height=self.kolom.get() * 33)
            # i untuk baris, dan j untuk kolom (berlaku juga untuk list)
            for i in range(self.baris.get()):
                self.listMNK.append([])
                for j in range(self.kolom.get()):
                    self.listMNK[i].append(j)
                    kotak = self.playArea.create_rectangle(
                        i * 33, j * 33, 33 + 33 * i, 33 + 33 * j, fill='white', tags=(i, j))
                    self.playArea.tag_bind(
                        kotak, '<Button-1>', lambda event, x=kotak: self.klikKotak(event, x))
        except TclError:
            messagebox.showerror(
                "Error", "Row, column or win conditions\nmust be in integers!\n")
            game.destroy()

    def klikKotak(self, event, x):
        '''Mewarnai kotak yang diklik, dan assign jalan pemain ke list'''
        self.ab = self.playArea.gettags(x)
        self.a = int(self.ab[0])
        self.b = int(self.ab[1])
        # Koordinat mengambil angka sebelum diubah menjadi 'x' atau 'o'
        # Jika kotak habis maka otomatis draw == 0
        # Pemain yang sedang jalan dinamakan self.player, sedangkan yang 
        # tidak jalan dinamakan self.notPlayer
        if self.turn % 2 == 0:
            self.playArea.itemconfig(x, fill='yellow')
            self.coordinate = self.listMNK[self.a][self.b]
            self.listMNK[self.a][self.b] = 'x'
            self.move = 'x'
            self.player = self.player1.get()
            self.notPlayer = self.player2.get()
            self.draw -= 1
            self.cekMenang()
        else:
            self.playArea.itemconfig(x, fill='blue')
            self.coordinate = self.listMNK[self.a][self.b]
            self.listMNK[self.a][self.b] = 'o'
            self.move = 'o'
            self.player = self.player2.get()
            self.notPlayer = self.player1.get()
            self.draw -= 1
            self.cekMenang()
        self.playArea.itemconfig(x, state='disabled')
        self.turn += 1
        print(self.listMNK)

    def cekMenang(self):
        '''Mengecek kemenangan'''
        win = self.winCond.get()
        countX, countY, countD1, countD2 = 0, 0, 0, 0
        # Cek ke kanan
        # Mengecek kondisi koordinat dan mengiterasi sebanyak panjang kolom
        for kolom in range(self.coordinate, len(self.listMNK[self.a])):
            if self.listMNK[self.a][kolom] == self.move:
                countX += 1
            else:
                break
        # cek ke kiri
        # Seperti kondisi cek ke kanan tetapi iterasi berlawanan arah
        for kolom in reversed(range(self.coordinate)):
            if self.listMNK[self.a][kolom] == self.move:
                countX += 1
            else:
                break
        # cek ke atas
        # Mengecek kondisi koordinat dan mengiterasi sebanyak panjang baris
        for baris in range(self.coordinate, len(self.listMNK)):
            if self.listMNK[baris][self.b] == self.move:
                countY += 1
            else:
                break
        # cek ke bawah
        # Seperti kondisi cek ke atas tetapi iterasi berlawanan arah
        for baris in reversed(range(self.coordinate)):
            if self.listMNK[baris][self.b] == self.move:
                countY += 1
            else:
                break
        # cek diagonal v10 super revisi
        # Kurang tahu, diajarkan oleh teman
        for baris, kolom in zip(range(self.a, len(self.listMNK)), range(self.b, len(self.listMNK[self.a]))):
            if self.listMNK[baris][kolom] == self.move:
                countD1 += 1
            else:
                break
        for baris, kolom in zip(reversed(range(self.a)), reversed(range(self.b))):
            if self.listMNK[baris][kolom] == self.move:
                countD1 += 1
            else:
                break
        for baris, kolom in zip(range(self.a, len(self.listMNK)), reversed(range(self.b+1))):
            if self.listMNK[baris][kolom] == self.move:
                countD2 += 1
            else:
                break
        for baris, kolom in zip(reversed(range(self.a)), range(self.b+1, len(self.listMNK[self.a]))):
            if self.listMNK[baris][kolom] == self.move:
                countD2 += 1
            else:
                break
        # cek menang
        if countX == win or countY == win or countD1 == win or countD2 == win:
            messagebox.showinfo('You win!', '{} wins against {} with {} turns!'.format(
                self.player, self.notPlayer, self.turn))
            self.gameHistory('win')
        # cek seri
        if self.draw == 0:
            messagebox.showinfo('Draw!', '{} draws against {} with {} turns!'.format(
                self.player1.get(), self.player2.get(), self.turn))
            self.gameHistory('draw')

    def gameHistory(self, cond):
        '''Setelah ada kemenangan maka menulis history menang ke dalam file history.txt'''
        with open('history.txt', 'a+') as file:
            if cond == 'win':
                file.write(str(strftime("%d-%m-%Y %H:%M:%S", localtime()) + '\n{} wins against {} with {} turns\n\n'.format(
                    self.player,self.notPlayer, self.turn)))
            elif cond == 'draw':
                file.write(str(strftime("%d-%m-%Y %H:%M:%S", localtime()) + '\n{} draws against {} with {} turns\n\n'.format(
                    self.player1.get(), self.player2.get(), self.turn)))

if __name__ == '__main__':
    # Jika dijalankan sebagai main program maka dijalankan gamenya,
    # tetapi jika diimport sebagai module maka game tidak berjalan
    Game()

