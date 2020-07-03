from tkinter import *

# a subclass of Canvas for dealing with resizing of windows
class ResizingCanvas(Canvas):
    def __init__(self, parent, **kwargs):
        Canvas.__init__(self, parent, **kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self, event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas 
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all", 0, 0, wscale, hscale)

def main():
    root = Tk()
    myframe = Frame(root)
    myframe.pack(fill=BOTH, expand=YES)
    mycanvas = ResizingCanvas(myframe, width=1000, height=1000, bg="black", highlightthickness=0)
    mycanvas.pack(fill=BOTH, expand=YES)

    # add some widgets to the canvas
    mycanvas.create_line(500, 0, 500, 1000, fill="white")
    mycanvas.create_line(0, 500, 1000, 500, fill="white")
    mycanvas.create_line(0, 100, 200, 0, fill="blue", dash=(4, 4))

    # objects
    mycanvas.create_rectangle(0, 0, 150, 50, fill="black")
    mycanvas.create_rectangle(0, 500, 50, 650, fill="black")
    mycanvas.create_rectangle(850, 950, 1000, 1000, fill="black")
    mycanvas.create_rectangle(950, 450, 1000, 600, fill="black")

    # tag all of the drawn widgets
    mycanvas.addtag_all("all")
    root.mainloop()

if __name__ == "__main__":
    main()



