import tkinter
import turtle

ventana = tkinter.Tk()
ventana.geometry("1200x650")
ventana.title("Fractal Trees")
HEIGHT = 650
WIDTH = 800

canvas = tkinter.Canvas(ventana)
canvas.config(width=WIDTH, height=HEIGHT)
#canvas.grid(row=0, columnspan=1, padx=10, pady=20)
canvas.pack(side=tkinter.RIGHT)

TurtleSc = turtle.TurtleScreen(canvas)
TurtleSc.tracer(0, 0)
maxTugo = turtle.RawTurtle(TurtleSc)
maxTugo.speed(0)
maxTugo.ht()
maxTugo.up()
maxTugo.left(90)

maxTugo.backward(HEIGHT*4/9)
maxTugo.down()


def tree(angle, profundidad, grosor, longitud, decremento):
    if profundidad > 0:
        maxTugo.pensize(grosor)
        maxTugo.forward(longitud)
        maxTugo.left(angle)
        tree(angle, profundidad - 1, grosor, longitud * 4 / 5 - decremento, decremento)
        maxTugo.right(angle * 2)
        tree(angle, profundidad - 1, grosor, longitud * 4 / 5 - decremento, decremento)
        maxTugo.left(angle)
        maxTugo.backward(longitud)




tree(30, 9, 3, 150, 5)

TurtleSc.update()

ventana.mainloop()
