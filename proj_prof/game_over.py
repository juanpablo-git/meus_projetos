import turtle
import random

jogo_runing = True

window = turtle.Screen()
window.bgcolor("green")
window.title("Space Invaders")
turtle.bgpic("background.gif")

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
setposition = border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)



# Set the score to 0
score = 0

# Draw the pen
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("red")
score_pen.penup()
score_pen.setposition(-290, 270)
scorestring = "SCORE: %s" % score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)

border_pen.hideturtle()

turtle.register_shape("player.gif")
turtle.register_shape("invader.gif")
turtle.register_shape("reload.gif")

player = turtle.Turtle()
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -200)

numbers_of_invaders = 11
invaders = []

for i in range(numbers_of_invaders):
    invaders.append(turtle.Turtle())

for enemy in invaders:
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    pos_x = random.randint(-200, 200)
    pos_y = random.randint(100, 250)
    enemy.setposition(pos_x, pos_y)


enemy.hideturtle()

fire = turtle.Turtle()
fire.color("yellow")
fire.shape("triangle")
fire.penup()
fire.speed(0)
fire.setheading(90)
fire.shapesize(0.5, 0.5)
fire.setposition(0, -185)

firespeed = 40
playerspeed = 15
fire_on = False
x_fire = 0
y_fire = 0

def move_fire():
    global fire_on, x_fire, y_fire,score,jogo_runing
    if fire_on == False and jogo_runing:
        fire_on = True
        y_fire =fire.ycor()
        x_fire = fire.xcor()

        while y_fire < 300:
            for inimigo in invaders:
                x_ini = inimigo.xcor()
                y_ini = inimigo.ycor()
                if x_fire >= x_ini -20 and x_fire <= x_ini + 20:
                    if y_fire >= y_ini:
                        global left_index, right_index, down_index
                        inimigo.setx(random.randint(-280, 280))
                        inimigo.sety(random.randint(100, 250))
                        y_fire = 400
                        left_index, right_index, down_index = init_pos()
                        score_pen.clear()
                        score+=1
                        score_pen.write("Score: "+str(score), False, align="left", font=("Arial", 14, "normal"))
                        break
            y_fire += firespeed
            fire.sety(y_fire)
            refresh()

        fire.hideturtle()
        fire.sety(-185)
        fire.setx(player.xcor())
        fire.showturtle()
        fire_on = False

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)
    if not fire_on:
        fire.setx(x)

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)
    if not fire_on:
        fire.setx(x)

turtle.listen()
turtle.onkey(move_fire, "space")
turtle.onkey(move_right, "Right")
turtle.onkey(move_left, "Left")

def init_pos():
    x_positions = []
    y_positions = []
    for pos_invaders in invaders:
        x_position = pos_invaders.xcor()
        y_position = pos_invaders.ycor()
        x_positions.append(x_position)
        y_positions.append(y_position)

    left_pos = min(x_positions)
    right_pos = max(x_positions)

    down_pos = min(y_positions)

    left_id = x_positions.index(left_pos)
    right_id = x_positions.index(right_pos)
    down_id = y_positions.index(down_pos)

    return left_id, right_id, down_id

left_index, right_index, down_index = init_pos()


speedinvaders = 10
direction = "left"
def write(x,y,text):
    game_over = turtle.Turtle()
    game_over.speed(0)
    game_over.color("red")
    game_over.penup()
    game_over.setposition(x, y)
    game_over.write(text, False, align="center", font=("Arial", 30, "normal"))
    game_over.hideturtle()
    return game_over
def refresh():
    global direction,invaders
    left_index, right_index, down_index = init_pos()
    y = invaders[left_index].ycor()
    if direction == "left":
        x_left = invaders[left_index].xcor()

        if x_left >= -280:
            for pos_invaders in invaders:
                position = pos_invaders.xcor()
                position -= speedinvaders
                pos_invaders.setx(position)
            x_left -= speedinvaders
        else:
            y -= 40
            direction = "right"
            for pos_invaders in invaders:
                position = pos_invaders.ycor()
                position -= 40
                pos_invaders.sety(position)

    elif direction == "right":
        x_right = invaders[right_index].xcor()
        if x_right < 280:
            for pos_invaders in invaders:
                position = pos_invaders.xcor()
                position += speedinvaders
                pos_invaders.setx(position)
            x_right += speedinvaders
        else:
            y -= 40
            direction = "left"
            for pos_invaders in invaders:
                position = pos_invaders.ycor()
                position -= 40
                pos_invaders.sety(position)

    # y_down = invaders[down_index].ycor()
    # if y_down <= -280:
    #     break
def game_breack():
    global inviders_loop,score,jogo_runing
    jogo_runing = False
    score = 0
    score_pen.clear()
    score_pen.write("Score: "+str(score), False, align="left", font=("Arial", 14, "normal"))
    inviders_loop = False
    game_over = turtle.Turtle()
    game_over.speed(0)
    game_over.color("red")
    game_over.penup()
    game_over.setposition(0, 0)
    game_over.write("Game Over", False, align="center", font=("Arial", 30, "normal"))
    game_over.hideturtle()
    reload = write(0,100,"")
    reload.showturtle()
    reload.shape("reload.gif")
    def reload_game(x,y):
        global invaders,inviders_loop,move_inimigos,jogo_runing
        inviders_loop = True
        jogo_runing = True
        for enemy in invaders:
            enemy.shape("invader.gif")
            enemy.penup()
            enemy.speed(0)
            pos_x = random.randint(-200, 200)
            pos_y = random.randint(100, 250)
            enemy.setposition(pos_x, pos_y)
        reload.clear()
        reload.hideturtle()
        game_over.clear()
        move_inimigos()
    reload.onclick(reload_game)



    

def move_inimigos ():
    global left_index, right_index, down_index,direction,invaders
    inviders_loop = True
    while inviders_loop:
        left_index, right_index, down_index = init_pos()
        y = invaders[left_index].ycor()
        if direction == "left":
            x_left = invaders[left_index].xcor()
            if x_left >= -280:
                for pos_invaders in invaders:
                    position = pos_invaders.xcor()
                    position -= speedinvaders
                    pos_invaders.setx(position)
                x_left -= speedinvaders
            else:
                y -= 40
                direction = "right"
                for pos_invaders in invaders:
                    position = pos_invaders.ycor()
                    position -= 40
                    pos_invaders.sety(position)

        elif direction == "right":
            x_right = invaders[right_index].xcor()
            if x_right < 280:
                for pos_invaders in invaders:
                    position = pos_invaders.xcor()
                    position += speedinvaders
                    pos_invaders.setx(position)
                x_right += speedinvaders
            else:
                y -= 40
                direction = "left"
                for pos_invaders in invaders:
                    position = pos_invaders.ycor()
                    position -= 40
                    pos_invaders.sety(position)

        y_down = invaders[down_index].ycor()
        if y_down <= -280:
            game_breack()
            inviders_loop = False

inviders_loop = True
while inviders_loop:
    if direction == "left":
        x_left = invaders[left_index].xcor()
        y = invaders[left_index].ycor()
        if x_left >= -280:
            for pos_invaders in invaders:
                position = pos_invaders.xcor()
                position -= speedinvaders
                pos_invaders.setx(position)
            x_left -= speedinvaders
        else:
            y -= 40
            direction = "right"
            for pos_invaders in invaders:
                position = pos_invaders.ycor()
                position -= 40
                pos_invaders.sety(position)

    elif direction == "right":
        x_right = invaders[right_index].xcor()
        if x_right < 280:
            for pos_invaders in invaders:
                position = pos_invaders.xcor()
                position += speedinvaders
                pos_invaders.setx(position)
            x_right += speedinvaders
        else:
            y -= 40
            direction = "left"
            for pos_invaders in invaders:
                position = pos_invaders.ycor()
                position -= 40
                pos_invaders.sety(position)

    y_down = invaders[down_index].ycor()
    if y_down <= -280:
        game_breack()
        inviders_loop = False
        # break



turtle.done()
