# Import 
import pgzrun

#Screen
WEIGHT = 860
HEIGHT = 650

# Boxes UI
Welcome_Box = Rect(0,0 , 860,85)
Question_Box = Rect(0,0 ,430 ,180)
Answer_Box1 = Rect (0,0 , 340 , 80)
Answer_Box2 = Rect (1,0 , 340 , 80)
Answer_Box3 = Rect (0,0 , 340 , 80)
Answer_Box4 = Rect (0,0 , 340 , 80)
Timer_Box = Rect (0,0 , 100 , 70)
Skip_Box = Rect (0,0 , 100 , 300)

# Game UI
Score = 0
Time = 10
Welcome_Message = ""
Game_Over = False
Answer_Boxes = [Answer_Box1,Answer_Box2,Answer_Box3,Answer_Box4]
Question_Count = 0
Questions = []
Current_Question = []
Questions_index = 0

# Placing the boxes

Welcome_Box.move_ip(0,0)
Question_Box.move_ip(13,100)
Answer_Box1.move_ip(13,200)
Answer_Box2.move_ip(370,270)
Answer_Box3.move_ip(20,450)
Answer_Box4.move_ip(370,450)
Timer_Box.move_ip(700,100)
Skip_Box.move_ip(700,270)

# Game Setup

def Load_Question(QandA = "questions.txt"):
    global Question_Count , Questions
    with open(QandA,"r") as file:
       for line in file:
           Questions.append(line)
           Question_Count = Question_Count+1
def read_nextquestion():
    global Questions_index
    Questions_index = Questions_index+1
    return Questions.pop(0).split(",")

def draw():
    screen.clear()
    screen.fill("black")
    screen.draw.filled_rect(Welcome_Box,"yellow")
    screen.draw.filled_rect(Question_Box,"yellow")
    screen.draw.filled_rect(Timer_Box,"yellow")
    screen.draw.filled_rect(Skip_Box,"yellow")
    for Answer in Answer_Boxes:
        screen.draw.filled_rect(Answer,"green")
    Welcome_Message = f"Welcome to Quiz Master...Q.{Questions_index+1}of{len(Questions)}"
    screen.draw.textbox(Welcome_Message,Welcome_Box,color ="white")
    screen.draw.textbox(str(Time),Timer_Box,color ="white")
    screen.draw.textbox("skip",Skip_Box,color ="white",angle=-90)
    if Current_Question:
        screen.draw.textbox(Current_Question[0],Question_Box,color ="white")
        for i ,box in enumerate(Answer_Boxes):
            screen.draw.textbox(Current_Question[i+1],box,color ="white")
def update():
    pass

# End game
def Endgame():
    global Current_Question , Time , Game_Over
    Game_Over = True
    Current_Question = f"Game over and you got {Score}"
    Time = 0

def on_mouse_down(pos):
    global Score , Time , Current_Question , Game_Over
    index = 1
    for i in Answer_Boxes:
        if i.collidepoint(pos):
            if index is int(Current_Question[5]):
                Score = Score+1
                if Questions:
                    Current_Question = Questions.pop(0)
                    Time = 10 
                else:
                    Endgame()

    if Skip_Box.collidepoint(pos):
      if Questions:
        Current_Question = Questions.pop(0)
        Time = 10 
      else:
        Endgame()

def update_Time():
   global Time 
   if Time:
       Time = Time-1
   else:
       Endgame()

Load_Question()
Question = read_nextquestion()

clock.schedule_interval(update_Time,1)


pgzrun.go()