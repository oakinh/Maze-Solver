from graphics import Window, Line, Point

def main():
    win = Window(800, 600)
    Line_1 = Line(Point(50, 50), Point(100, 50))

    win.draw_line(Line_1, "Black")
    
    
    win.wait_for_close()

    


main()
