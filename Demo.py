import Tkinter as tk
import numpy as np
from Voronoi import Voronoi

class MainWindow:
    # radius of drawn points on canvas
    RADIUS = 3

    # flag to lock the canvas when drawn
    LOCK_FLAG = False
    
    def __init__(self, master, width=500, height=500):
        self.master = master
        self.master.title("Voronoi")

        self.frmMain = tk.Frame(self.master, relief=tk.RAISED, borderwidth=1)
        self.frmMain.pack(fill=tk.BOTH, expand=1)

        self.width = width
        self.height = height
        # <Button-1>:left click
        # <Button-2>:middle click
        # <Button-3>:right click
        # <Double-Button-1>:left-double click
        # <Triple-Button-1>:left-triple click
        self.w = tk.Canvas(self.frmMain, width=self.width, height=self.height)
        self.w.config(background='white')
        self.w.bind('<Button-1>', self.onSingleClick)
        self.w.pack()       

        self.frmButton = tk.Frame(self.master)
        self.frmButton.pack()
        
        self.btnCalculate = tk.Button(self.frmButton, text='Calculate', width=25, command=self.onClickCalculate)
        self.btnCalculate.pack(side=tk.LEFT)

        self.btnRandom = tk.Button(self.frmButton, text='Random', width=25, command=self.onClickGenerate)
        self.btnRandom.pack(side=tk.LEFT)


        self.btnClear = tk.Button(self.frmButton, text='Clear', width=25, command=self.onClickClear)
        self.btnClear.pack(side=tk.LEFT)
        
    def onClickCalculate(self):
        if not self.LOCK_FLAG:
            self.LOCK_FLAG = True

            pObj = self.w.find_all()
            points = []
            for p in pObj:
                coord = self.w.coords(p)
                points.append((coord[0]+self.RADIUS, coord[1]+self.RADIUS))

            vp = Voronoi(points)
            vp.process()
            lines = vp.get_output()
            self.drawLinesOnCanvas(lines)
            
            print(lines)

    #generate random points
    def onClickGenerate(self):
        if not self.LOCK_FLAG:
            point_number = 30
            rand_x = self.width * np.random.rand(point_number)
            rand_y = self.height * np.random.rand(point_number)
            rand_point = list(zip(rand_x,rand_y))
            for i in rand_point:
                self.w.create_oval(i[0]-self.RADIUS, i[1]-self.RADIUS, i[0]+self.RADIUS, i[1]+self.RADIUS, fill="yellow")



    def onClickClear(self):
        self.LOCK_FLAG = False
        self.w.delete(tk.ALL)

    def onDoubleClick(self, event):
        if not self.LOCK_FLAG:
            self.w.create_oval(event.x-self.RADIUS, event.y-self.RADIUS, event.x+self.RADIUS, event.y+self.RADIUS, fill="black")

    def drawLinesOnCanvas(self, lines):
        for l in lines:
            self.w.create_line(l[0], l[1], l[2], l[3], fill='blue')

def main(): 
    root = tk.Tk()
    app = MainWindow(root,500,500)
    root.mainloop()

if __name__ == '__main__':
    main()
