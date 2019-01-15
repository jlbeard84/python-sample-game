from tkinter import Tk, Frame, Canvas

class Game(Frame):
    def __init__(self, master):
        super(Game, self).__init__(master)
        self.lives = 3
        self.width = 610
        self.height = 400
        self.canvas = Canvas(self, width=self.width, height=self.height, bg='#aaaaff')

        self.canvas.pack()
        self.pack()

if __name__ == '__main__':
    root = Tk()
    root.title('Hello Game')
    game = Game(root)
    game.mainloop()