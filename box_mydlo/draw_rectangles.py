import tkinter as tk
import math

class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.x = self.y = 0
        self.canvas = tk.Canvas(self, width=1000, height=1000, cursor="cross", bg="black")
        self.canvas.create_line(500, 0, 500, 1000, fill="white")
        self.canvas.create_line(0, 500, 1000, 500, fill="white")

        self.canvas.pack(side="top", fill="both", expand=True)
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

        self.center_box_x = 500
        self.center_box_y = 500
        self.length_vector = 50


    def on_button_press(self, event):
        self.x = event.x
        self.y = event.y

    # zones of box are separated into 4 regions:
    # |-----|-----|
    # |  4  |  1  |
    # |-----|-----|
    # |  3  |  2  |
    # |_____|_____|
    def compute_vector(self, obj_x0, obj_y0, obj_x1, obj_y1, box_width, box_height):
        center_object_x = ((obj_x1 - obj_x0) / 2) + obj_x0
        center_object_y = ((obj_y1 - obj_y0) / 2) + obj_y0

        if center_object_x >= (box_width / 2):
            if center_object_y <= (box_height / 2):
                zone = 1
                print("Object is in a zone: {}".format(zone))
                vector_x_start, vector_y_start = center_object_x, center_object_y

                a = vector_y_start - self.center_box_y
                b = vector_x_start - self.center_box_x
                c = math.sqrt((a * a) + (b * b))  # Pytagoras
                alpha = 1 / math.sin(a / c)  # angle of vector from center of object into center of box

                # a, b, c are lines of triangle = vector
                a_vector = math.sin(alpha) * self.length_vector
                b_vector = math.cos(alpha) * self.length_vector

                # coordinates of point of triangle where vector ends
                y = vector_y_start - a_vector
                x = vector_x_start - b_vector

                vector_x_end, vector_y_end = x, y

            if center_object_y > (box_height / 2):
                zone = 2
                print("Object is in a zone: {}".format(zone))
                vector_x_start, vector_y_start = center_object_x, center_object_y

                a = self.center_box_y - vector_y_start
                b = vector_x_start - self.center_box_x
                c = math.sqrt((a*a)+(b*b))  # Pytagoras
                alpha = 1 / math.sin(b / c)  # angle of vector from center of object into center of box

                # a, b, c are lines of triangle = vector
                b_vector = math.sin(alpha) * self.length_vector
                a_vector = math.cos(alpha) * self.length_vector

                # coordinates of point of triangle where vector ends
                y = vector_y_start + a_vector
                x = vector_x_start - b_vector

                vector_x_end, vector_y_end = x, y

        if center_object_x < (box_width / 2):
            if center_object_y > (box_height / 2):
                zone = 3
                print("Object is in a zone: {}".format(zone))
                vector_x_start, vector_y_start = center_object_x, center_object_y

                a = vector_y_start - self.center_box_y
                b = vector_x_start - self.center_box_x
                c = math.sqrt((a * a) + (b * b))  # Pytagoras
                alpha = 1 / math.sin(b / c)  # angle of vector from center of object into center of box

                # a, b, c are lines of triangle = vector
                b_vector = math.sin(alpha) * self.length_vector
                a_vector = math.cos(alpha) * self.length_vector

                # coordinates of point of triangle where vector ends
                y = vector_y_start + a_vector
                x = vector_x_start + b_vector

                vector_x_end, vector_y_end = x, y

            if center_object_y <= (box_height / 2):
                zone = 4
                print("Object is in a zone: {}".format(zone))
                vector_x_start, vector_y_start = center_object_x, center_object_y

                a = self.center_box_y - vector_y_start
                b = self.center_box_x - vector_x_start
                c = math.sqrt((a * a) + (b * b))  # Pytagoras
                alpha = 1 / math.sin(b / c)  # angle of vector from center of object into center of box

                # a, b, c are lines of triangle = vector
                b_vector = math.sin(alpha) * self.length_vector
                a_vector = math.cos(alpha) * self.length_vector

                # coordinates of point of triangle where vector ends
                y = vector_y_start - a_vector
                x = vector_x_start + b_vector

                vector_x_end, vector_y_end = x, y

        return (vector_x_start, vector_y_start, vector_x_end, vector_y_end)

        self.canvas.create_line(self.center_x, self.center_y, self.center_x+100, self.center_y+100, fill="blue")

    def on_button_release(self, event):
        x0, y0 = (self.x, self.y)
        x1, y1 = (event.x, event.y)

        if (x0 < x1) and (y0 < y1):
            x_start, y_start = x0, y0
            x_end, y_end = x1, y1
        elif (x0 > x1) and (y0 < y1):
            x_start, y_start = x1, y0
            x_end, y_end = x0, y1
        elif (x0 < x1) and (y0 > y1):
            x_start, y_start = x0, y1
            x_end, y_end = x1, y0
        elif (x0 > x1) and (y0 > y1):
            x_start, y_start = x1, y1
            x_end, y_end = x0, y0

        print("Start x, y: {}, {}".format(x_start, y_start))
        print("End   x, y: {}, {}".format(x_end, y_end))
        print()
        self.canvas.create_rectangle(x0, y0, x1, y1, fill="red")
        line_start_x, line_start_y, line_end_x, line_end_y = self.compute_vector(x_start, y_start, x_end, y_end, 1000, 1000)
        self.canvas.create_line(line_start_x, line_start_y, self.center_box_x, self.center_box_y, fill="white")


if __name__ == "__main__":
    app = ExampleApp()
    app.mainloop()