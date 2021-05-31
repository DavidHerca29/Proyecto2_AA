import tkinter
import turtle

ventana = tkinter.Tk()
ventana.geometry("600x600")
ventana.title("Fractal Trees")

canvas = tkinter.Canvas(ventana, height=300, width=400)
canvas.grid(row=0, columnspan= 6, pady = 3)

TurtleSc = turtle.TurtleScreen(canvas)
maxTugo = turtle.RawTurtle(canvas)
maxTugo.left(90)
maxTugo.backward(100)
maxTugo.speed(400)
def tree(angle, profundidad, grosor, longitud, decremento):
    if profundidad > 0:
        maxTugo.pensize(grosor)
        maxTugo.forward(longitud)
        maxTugo.left(angle)
        tree(angle, profundidad-1, grosor, longitud*4/5-decremento, decremento)
        maxTugo.right(angle*2)
        tree(angle, profundidad-1, grosor, longitud*4/5-decremento, decremento)
        maxTugo.left(angle)
        maxTugo.backward(longitud)

tree(30, 9, 3, 50, 5)
canvas.pack()
ventana.mainloop()