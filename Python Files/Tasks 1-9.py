import random, time, turtle

loop = True

## june 2007 Birthday_Passed


def T1():
    print("Birthday Date Month Year Calculator Happy Birthday")   
    year = int(input("Birth Year: "))
    year_rn = int(input("Current Year: "))
    passed = input("Has your birthday passed? (Y/N): ").lower()
    ans = year_rn-year
    if passed == "y":
        ans + 1
        print("You are",ans)
    elif passed != "y":
        print("You are",ans)
        
def T2():
    print("Pi Number To Calculator But Only To Fifteen Decimal Places")
    print(22/7)

def T3():
    print("Multiply Two Numbers Then Give Result Of The Answer of The Two Numbers")
    x = int(input("Number 1: "))
    y = int(input("Number 2: "))
    ans = x * y
    print(ans)

def T4():
    print("Square Number Multiply Calculator One Number Only")
    x = int(input("Number: "))
    ans = x*x
    print(ans)

def T5():
    print("Number Bigger Display Calcutalor Only Prints When Number is BIG")
    x = int(input("Number 1: "))
    y = int(input("Number 2: "))
    if x > y:
        print("Bigger Number is,",x)
    elif x < y:
        print("Bigger Number is,",y)
    
def T6():
    print("Volume of Cuboid Shape Swimming Pool Calculator")
    l = int(input("Length: "))
    w = int(input("Width: "))
    h = int(input("Heigth: "))
    ans = l * w * h
    print(ans)

def T7():
    print("Sentence creator Maker Thing But Limited To Only 5 Words Because im Lazy")
    w1 = input("Word 1: ")
    w2 = input("Word 2: ")
    w3 = input("Word 3: ")
    w4 = input("Word 4: ")
    w5 = input("Word 5: ")
    ans = "%s %s %s %s %s" % (w1,w2,w3,w4,w5)
    print(ans)
    
def T8():
    print("rock paper scissors")
    ## 0 = draw, 1 = player, 2 = bot
    player = input("(r)ock, (p)aper, (s)cissors: ").lower()
    choices = ["rock", "paper", "scissors"]
    bot = random.choice(choices)
    if player == bot:
        result = 0
    elif player == "rock":
        if bot == "paper":
            result = 2
        elif bot == "scissors":
            result = 1
    elif player == "paper":
        if bot == "rock":
            result = 1
        elif bot == "scissors":
            result = 2
    elif player == "scissors":        
        if bot == "paper":
            result = 1
        elif bot == "rock":
            result = 2
    if result == 0:
        print("You both chose: ",player)
        print("Draw")
    elif result == 1:
        print("bot chose: ",bot)
        print("You chose: ",player)
        print("You win :)")
    elif result == 2:
        print("bot chose: ",bot)
        print("You chose: ",player)
        print("You lost :(")

def T9():
    delay = 0.19

    # Score
    score = 0
    high_score = 0

    # Set up the screen
    wn = turtle.Screen()
    wn.bgcolor("green")
    wn.setup(width=600, height=600)
    wn.tracer(0) # Turns off the screen updates

    # Snake head
    head = turtle.Turtle()
    head.speed(0)
    head.shape("square")
    head.color("black")
    head.penup()
    head.goto(0,0)
    head.direction = "stop"

    # Snake food
    food = turtle.Turtle()
    food.speed(0)
    food.shape("circle")
    food.color("red")
    food.penup()
    food.goto(0,100)

    segments = []

    # Pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

    # Functions
    def go_up():
        if head.direction != "down":
            head.direction = "up"

    def go_down():
        if head.direction != "up":
            head.direction = "down"

    def go_left():
        if head.direction != "right":
            head.direction = "left"

    def go_right():
        if head.direction != "left":
            head.direction = "right"

    def move():
        if head.direction == "up":
            y = head.ycor()
            head.sety(y + 20)

        if head.direction == "down":
            y = head.ycor()
            head.sety(y - 20)

        if head.direction == "left":
            x = head.xcor()
            head.setx(x - 20)

        if head.direction == "right":
            x = head.xcor()
            head.setx(x + 20)

    # Keyboard bindings
    wn.listen()
    wn.onkeypress(go_up, "w")
    wn.onkeypress(go_down, "s")
    wn.onkeypress(go_left, "a")
    wn.onkeypress(go_right, "d")

    # Main game loop
    while True:
        wn.update()

        # Check for a collision with the border
        if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
            
            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 


        # Check for a collision with the food
        if head.distance(food) < 20:
            # Move the food to a random spot
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x,y)

            # Add a segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("grey")
            new_segment.penup()
            segments.append(new_segment)

            # Shorten the delay
            delay -= 0.001

            # Increase the score
            score += 50

            if score > high_score:
                high_score = score
            
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

        # Move the end segments first in reverse order
        for index in range(len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x, y)

        # Move segment 0 to where the head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x,y)

        move()    

        # Check for head collision with the body segments
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0,0)
                head.direction = "stop"
            
                # Hide the segments
                for segment in segments:
                    segment.goto(1000, 1000)
            
                # Clear the segments list
                segments.clear()

                # Reset the score
                score = 0

                # Reset the delay
                delay = 0.1
            
                # Update the score display
                pen.clear()
                pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        time.sleep(delay)

    wn.mainloop()

while loop == True:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("T1 = Birthday Date Month Year Calculator Happy Birthday")
    print("T2 = Pi Number To Calculator But Only To Fifteen Decimal Places")
    print("T3 = Multiply Two Numbers Then Give Result Of The Answer of The Two Numbers")
    print("T4 = Square Number Multiply Calculator One Number Only")
    print("T5 = Number Bigger Display Calcutalor Only Prints When Number is BIG")
    print("T6 = Volume of Cuboid Shape Swimming Pool Calculator")
    print("T7 = Sentence creator Maker Thing But Limited To Only 5 Words Because Lazy")
    print("T8 = rock paper scissors")
    print("T9 = No")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    choice = int(input("(1-9): "))
    if choice == 1:
        T1()
    elif choice == 2:
        T2()
    elif choice == 3:
        T3()
    elif choice == 4:
        T4()
    elif choice == 5:
        T5()
    elif choice == 6:
        T6()
    elif choice == 7:
        T7()
    elif choice == 8:
        T8()
    elif choice == 9:
        T9()
        
    replay = input("Again? (Y/N) ")
    if replay != "y":
        loop = False
        
        
        
        true_false = None


def theorum (a, b, c):
            if (a*a + b*b == c*c):              
                true_false = True
            elif (b*b + c*c == a*a):
         
                true_false = True
            elif (a*a + c*c == b*b):
           
                true_false = True
            else:
                true_false = False
           
 
    theorum(int(input("Enter Length of the first stick: ")),int(input("Enter Length of the second stick: ")),int(input("Enter Length of the third stick: ")))
   
    if true_false == True:
        print ("This can form a right angle triangle.")
    elif true_false != True:
        print("This cannot form a right angle triangle.")
       
    retry = input("Do you want to try again? Y/N: ").lower()
    if retry != "y":
        break