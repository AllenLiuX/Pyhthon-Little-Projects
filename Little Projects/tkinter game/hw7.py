#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: Wenxuan Liu 805152602
"""

import Tkinter as Tk
import sys

class MainScreen:
    def __init__(self, master,n):
        self.master = master
        self.canvas = Tk.Canvas(master, width=500, height=500)
        self.canvas.pack()
        self.side = 500/n
        self.curx = 0
        self.cury = 0
        self.count = 0
        self.first = True
        for i in range(0,n+1):
            self.canvas.create_line(0, i*self.side, n*self.side, i*self.side)
            self.canvas.create_line(i*self.side, 0, i*self.side, n*self.side)
        self.canvas.bind("<Button-1>", self.rectangle)

    def rectangle(self,ev):
        tx = int(ev.x/self.side)
        ty = int(ev.y/self.side)
        if self.first or (abs(tx-self.curx)==1 and abs(ty-self.cury)==2) or (abs(tx-self.curx)==2 and abs(ty-self.cury)==1):
            if not self.first:
                self.canvas.create_rectangle(self.curx * self.side, self.cury * self.side, (self.curx + 1) * self.side, \
                                         (self.cury + 1) * self.side, fill="blue")
            self.first = False
            self.curx = tx
            self.cury = ty
            self.canvas.create_rectangle(self.curx*self.side, self.cury*self.side, (self.curx+1)*self.side, \
                                         (self.cury+1)*self.side, fill="orange")
            self.count += 1
            self.canvas.create_text((self.curx+0.5)*self.side, (self.cury+0.5)*self.side, \
                                    fill="darkblue",font="Times %d italic bold" %(self.side/4), text=str(self.count))
def knightstour(n):
    root = Tk.Tk()
    gui = MainScreen(root, n)
    root.mainloop()

if __name__=='__main__':
    if len(sys.argv)==1:   #pass no argument
        knightstour(5)
    else:
        knightstour(int(sys.argv[1]))   #use the first argument as paremeter to