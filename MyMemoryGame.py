#Author
#Date
#Description: Turtle Racing Game
#Revision History
#Name    Date     Desc
#scl    2/12/24   Initial code base



number_list = []

start_pos_x= 0
start_pos_y= 0
level = 3
offset= 100

def drawSquare(x, y) :
     turtle.down()
for x in range(4):
        turtle.forward(100)
        turtle.left(90
                    )
        for x in range(level):
        #data type is integer
    a = random.randint(1,99)
        #data structure
    number_list.appeal(a)
    
    turtle.write(str(a), font=("Verdana", 50," normal"))
    turtle.up()
    save_pos = (x * offset, 0)
    turtle.goto(save_pos)

    drawSquare(x * offset, 0)
    turtle.goto(save_pos)
    time.sleep(3)

    turtle.clear()
    

#please enter the answers
for x in range(level):
    answer = int(input("The numbers were "))
