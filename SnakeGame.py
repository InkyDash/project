import pygame
import time
import turtle
from random import randrange

Break_Flag = False

#создаем фон игры
screen = turtle.Screen()
screen.title('Змейка')
screen.bgcolor('green')
screen.setup(650, 650)
screen.tracer(0)

#создаем поле для змейки
border = turtle.Turtle()
border.hideturtle()
border.penup()
border.goto(-311, 311)
border.pendown()
border.goto(311, 311)
border.goto(311, -311)
border.goto(-311, -311)
border.goto(-311, 311)

score = 0

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

    draw_text(screen, str(score), 18, WIDTH / 2, 10)
    
#создаем змейку в 3 сегмента, красим
snake = []
for i in range(3):
    snake_segment = turtle.Turtle()
    snake_segment.shape('square')
    snake_segment.penup()
    if i > 0:
        snake_segment.color('gray')
    snake.append(snake_segment)

#яблоки...
food = turtle.Turtle()
food.shape('circle')
food.color('yellow')
food.penup()
food.goto(randrange(-300, 300, 20), randrange(-300, 300, 20))

#управление
screen.onkeypress(lambda: snake[0].setheading(90), 'Up')
screen.onkeypress(lambda: snake[0].setheading(270), 'Down')
screen.onkeypress(lambda: snake[0].setheading(180), 'Left')
screen.onkeypress(lambda: snake[0].setheading(0), 'Right')
screen.listen()


while True:
    if snake[0].distance(food) < 10:
        food.goto(randrange(-300, 300, 20), randrange(-300, 300, 20))
        snake_segment = turtle.Turtle()
        snake_segment.shape('square')
        snake_segment.color('gray')
        snake_segment.penup()
        snake.append(snake_segment)
        score += 1

    for i in range(len(snake)-1, 0, -1):
        x = snake[i-1].xcor()
        y = snake[i-1].ycor()
        snake[i].goto(x, y)

    snake[0].forward(20)
    screen.update()

    x_cor = snake[0].xcor()
    y_cor = snake[0].ycor()

    #смерть при касании края поля
    if x_cor > 300 or x_cor < -300:
        screen.bgcolor('red')
        break
    if y_cor > 300 or y_cor < -300:
        screen.bgcolor('red')
        break
    #смерть при касании себя
    for i in snake[1:]:
        i = i.position()
        if snake[0].distance(i) < 10:
            Break_Flag = True
    if Break_Flag:
        screen.bgcolor('red')
        break

    #скорость змейки
    time.sleep(0.2)
screen.mainloop()