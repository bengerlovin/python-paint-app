from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.font
from PIL import Image, ImageTK



# ------ Define Class -------------

class PaintApplication:

 # ------ Define Class Variables ---

    draw_tool = "text"

    left_button = "up"

    x_position, y_position = None, None

    x1_line_pt, y1_line_pt, x2_line_pt, y2_line_pt = None, None, None, None


# ------ Mouse Up -----------------
    def left_but_up(self, event=None):

        self.left_button = "up"

        # Track x and y positions for event
        self.x_position = None
        self.y_position = None

        self.x2_line_pt = event.x
        self.y2_line_pt = event.y

        if self.draw_tool == "line":
            self.line_draw(event)
        elif self.draw_tool == "arc":
            self.arc_draw(event)
        elif self.draw_tool == "oval":
            self.oval_draw(event)
        elif self.draw_tool == "rectangle":
            self.rectangle_draw(event)
        elif self.draw_tool == "text":
            self.text_draw(event)



# ------ Drop Down Menu -----------------

clickedOption = StringVar()
clickedOption.set("line")


drop = OptionMenu(root, clickedOption, "text", "line", "oval", "arc", "rectangle")
drop.pack()


# ------ Mouse Down ---------------

    def left_but_down(self, event=None):

        self.left_button = "down"

        # Track x and y positions for event
        self.x1_line_pt = event.x
        self.y1_line_pt = event.y


# ------ Mouse Move ---------------

    def motion(self, event=None):

        if self.draw_tool == "pencil":
            self.pencil_draw(event)

# ------ Draw Pencil ---------------

    def pencil_draw(self, event=None):
        if self.left_button == "down":

            if self.x_position is not None and self.y_position is not None:

                event.widget.create_line(
                    self.x_position, self.y_position, event.x, event.y, smooth=TRUE)

        # update x and y position as function is called
        self.x_position = event.x
        self.y_position = event.y


# ------ Draw Oval -----------------

    def oval_draw(self, event=None):

        if None not in(self.x1_line_pt, self.x2_line_pt, self.y1_line_pt, self.y2_line_pt):

            event.widget.create_oval(self.x1_line_pt, self.x2_line_pt, self.y1_line_pt,
                                     self.y2_line_pt, fill="midnight blue", outline="black", width=2)


# ------ Draw Line -----------------

    def line_draw(self, event=None):

        if None not in(self.x1_line_pt, self.x2_line_pt, self.y1_line_pt, self.y2_line_pt):
            event.widget.create_line(self.x1_line_pt, self.x2_line_pt,
                                     self.y1_line_pt, self.y2_line_pt, smooth=TRUE, fill="green")


# ------ Draw Arc ------------------

    def arc_draw(self, event=None):

        if None not in(self.x1_line_pt, self.x2_line_pt, self.y1_line_pt, self.y2_line_pt):

            # set up coordinates
            coords = self.x1_line_pt, self.x2_line_pt, self.y1_line_pt, self.y2_line_pt
            event.widget.create_arc(
                coords, start=0, extent=150, fill="blue", style=ARC)


# ------ Draw Rectangle ------------

    def rectangle_draw(self, event=None):

        if None not in(self.x1_line_pt, self.x2_line_pt, self.y1_line_pt, self.y2_line_pt):

            event.widget.create_rectangle(self.x1_line_pt, self.x2_line_pt, self.y1_line_pt,
                                          self.y2_line_pt, fill="dark green", outline="azure", width=2)


# ------ Draw Text -----------------
    
    def text_draw(self, event=None):
    
        if None not in(self.x1_line_pt, self.y1_line_pt): 
            
            text_font = tkinter.font.Font(family ="Cambria", size = 20, weight = "bold")

            event.widget.create_text(self.x1_line_pt, self.y1_line_pt, fill = "black", font = text_font, text = "Wow")

# ------ Intialize -----------------

    def __init__(self, root):
        drawing_area = Canvas(root)

        drawing_area.pack()

        #Title
        root.title("It's Time to Paint!")

        menubar = Menu(root)
        file_menu = Menu(root, tearoff = 0)
        file_menu.add_command(label="Open")

        # Bindings
        drawing_area.bind("<Motion>", self.motion)
        drawing_area.bind("<ButtonPress-1>", self.left_but_down)
        drawing_area.bind("<ButtonRelease-1>", self.left_but_up)


root = Tk()
paint_application = PaintApplication(root)
root.mainloop()
