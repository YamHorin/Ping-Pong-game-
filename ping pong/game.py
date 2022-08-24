import turtle
import winsound


freq = 450


dur = 8


window = turtle.Screen()
window.title('Pong by Yam_Horin')
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)
# score ver
player_1_score = int(0)
player_2_score = int(0)

# player1:
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=4.5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# player2:
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=4.5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)
# ball:
hit_ball = turtle.Turtle()
hit_ball.speed(1)
hit_ball.shape("circle")
hit_ball.color("blue")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = -0.2
hit_ball.dy = -0.2

# pen
pen = turtle.Turtle()
pen.color("white")
pen.speed(0)
pen.penup()
pen.goto(0, 260)
pen.hideturtle()
pen.write(f"player 1 = {player_1_score}  player 2  = {player_2_score} ",
          align="center", font=("Courier", 24, "normal"))

# up


def paddle_a_up():
    y = paddle_a.ycor()
    y += 22.5
    paddle_a.sety(y)

# down


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 22.5
    paddle_a.sety(y)

# up


def paddle_b_up():
    y = paddle_b.ycor()
    y += 22.5
    paddle_b.sety(y)

# down


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 22.5
    paddle_b.sety(y)


window.listen()
window.onkeypress(paddle_a_down, 's')
window.onkeypress(paddle_a_up, 'w')
window.onkeypress(paddle_b_down, 'Down')
window.onkeypress(paddle_b_up, 'Up')
window
# main loop
while True:
    window.update()
    hit_ball.setx(hit_ball.xcor()+hit_ball.dx)
    hit_ball.sety(hit_ball.ycor()+hit_ball.dy)

    if hit_ball.ycor() > 280:
        hit_ball.sety(280)
        hit_ball.dy *= -1
        winsound.Beep(freq, dur)

    if hit_ball.ycor() < -280:
        hit_ball.sety(-280)
        hit_ball.dy *= -1
        winsound.Beep(freq, dur)

    if hit_ball.xcor() > 450:
        hit_ball.dx *= -1
        hit_ball.goto(0, 0)
        winsound.Beep(freq, dur)
        pen.clear()
        player_1_score = player_1_score+1
        pen.write(f"player 1 = {player_1_score}  player 2  = {player_2_score} ",
                  align="center", font=("Courier", 24, "normal"))

    if hit_ball.xcor() < -450:
        hit_ball.dx *= -1
        player_2_score = player_2_score+1
        winsound.Beep(freq, dur)
        hit_ball.goto(0, 0)
        pen.clear()
        pen.write(f"player 1 = {player_1_score}  player 2  = {player_2_score} ",
                  align="center", font=("Courier", 24, "normal"))
     # Paddle and ball collisions
    if hit_ball.xcor() < -340 and hit_ball.ycor() < paddle_a.ycor() + 50 and hit_ball.ycor() > paddle_a.ycor() - 50:
        hit_ball.dx *= -1
        winsound.Beep(freq, dur)

    if hit_ball.xcor() > 340 and hit_ball.ycor() < paddle_b.ycor() + 50 and hit_ball.ycor() > paddle_b.ycor() - 50:
        hit_ball.dx *= -1
        winsound.Beep(freq, dur)
