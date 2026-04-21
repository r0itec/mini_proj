import turtle
import pygame

pygame.mixer.init()


sound_a = pygame.mixer.Sound("C.wav")
sound_s = pygame.mixer.Sound("D.wav")
sound_d = pygame.mixer.Sound("E.wav")
sound_f = pygame.mixer.Sound("F.wav")
sound_g = pygame.mixer.Sound("G.wav")
sound_h = pygame.mixer.Sound("A.wav")
sound_j = pygame.mixer.Sound("B.wav")


s = turtle.Screen()
s.bgcolor("black")
s.setup(1400, 900)   


t1 = turtle.Turtle()
t1.hideturtle()
t1.penup()
t1.color("white")
t1.goto(-300, 350)
t1.write("Keyboard Based Piano In Turtle", font=("Arial", 40))


t2 = turtle.Turtle()
t2.hideturtle()
t2.penup()
t2.color("white")
t2.goto(-300, 280)
t2.write("A:C  S:D  D:E  F:F  G:G  H:A  J:B", font=("Arial", 30))


d = turtle.Turtle()
d.hideturtle()
d.penup()
d.color("yellow")

s.listen()

s.onkeypress(lambda: (sound_a.play(), d.clear(), d.goto(-80, 0), d.write("C", font=("Arial", 120))), "a")
s.onkeypress(lambda: (sound_s.play(), d.clear(), d.goto(-80, 0), d.write("D", font=("Arial", 120))), "s")
s.onkeypress(lambda: (sound_d.play(), d.clear(), d.goto(-80, 0), d.write("E", font=("Arial", 120))), "d")
s.onkeypress(lambda: (sound_f.play(), d.clear(), d.goto(-80, 0), d.write("F", font=("Arial", 120))), "f")
s.onkeypress(lambda: (sound_g.play(), d.clear(), d.goto(-80, 0), d.write("G", font=("Arial", 120))), "g")
s.onkeypress(lambda: (sound_h.play(), d.clear(), d.goto(-80, 0), d.write("A", font=("Arial", 120))), "h")
s.onkeypress(lambda: (sound_j.play(), d.clear(), d.goto(-80, 0), d.write("B", font=("Arial", 120))), "j")

s.mainloop()