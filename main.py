from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.font


# ------ Define Class -------------

class PaintApplication:

 
 # ------ Define Class Variables ---


    draw_tool = "line"

    left_button = "up"

    x_position, y_position = None, None

    x1_line_pt, y1_line_pt, x2_line_pt, y2_line_pt = None, None, None, None


# ------ Mouse Up -----------------
    def left_but_up(self, event=None):

            self.left_button = "up"

            #Track x and y positions for event
            self.x_position = None
            self.y_position = None

            self.x2_line_pt = event.x
            self.y2_line_pt = event.y

            if self.draw_tool == "line":
                self.line_draw(event)

# ------ Mouse Down ---------------


    def left_but_down(self, event=None):

            self.left_button = "down"

            #Track x and y positions for event
            self.x1_line_pt = event.x
            self.y1_line_pt = event.y


# ------ Mouse Move ---------------

    def motion(self, event=None):

        if self.draw_tool == "pencil":
            self.pencil_draw(event)

# ------ Draw Pencil ---------------


    def pencil_draw(self, event=None):
        if self.left_button == "down":

            if self.x_pos is not None and self.y_pos is not None:

                event.widget.create_line(
                    self.x_pos, self.y_pos, event.x, event.y, smooth=TRUE)

            #update x and y position as function is called
            self.x_pos = event.x
            self.y_pos = event.y


# ------ Draw Oval -----------------

# ------ Draw Line -----------------

    def line_draw(self, event=None):

        if None not in(self.x1_line, self.x2_line_pt, self.y1_line_pt, self.y2_line_pt):
            event.widget.create_line(self.x1_line, self.x2_line_pt, self.y1_line_pt, self.y2_line_pt
                    , smooth=TRUE, fill = "green")



    


# ------ Draw Arc ------------------

# ------ Draw Rectangle ------------

# ------ Draw Text -----------------


# ------ Intialize -----------------

    def __init__(self, root):
            drawing_area = Canvas(root)

            drawing_area.pack()

            # Bindings
            drawing_area.bind("<Motion>", self.motion)
            drawing_area.bind("<ButtonPress-1>", self.left_but_down)
            drawing_area.bind("<ButtonRelease-1>", self.left_but_up)


root = Tk()
paint_application = PaintApplication(root)
root.mainloop()
