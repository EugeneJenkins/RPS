from tkinter import *
from random import randint
root = Tk()

root.title('ROCK')
root.minsize(width=1080, height=720)
root.maxsize(width=1080, height=720)

canvas=Canvas(root,width=1080, height=720)

image1 =PhotoImage(file ="images/background.png")
round1=PhotoImage(file ="images/round1.png")
round2=PhotoImage(file ="images/round2.png")
round3=PhotoImage(file ="images/round3.png")
user=PhotoImage(file ="images/user.png")
comp=PhotoImage(file ="images/comp.png")
rock=PhotoImage(file ="images/Rock.png")
paper=PhotoImage(file ="images/Paper.png")
scissors=PhotoImage(file ="images/Scissors.png")


UserName="User"
UserName2="Comp"
Score1=0
Score2=0
result=''




# 1=ROCK 
# 2=Paper
#3=Scissors
def companswer():
    t = [1, 2, 3]
    computer = t[randint(0,2)]
    return computer


def answer(player): 
    global Score1,Score2
    computer= companswer()
    if player == computer:
        result="Tie!"
    elif player == 1:
        if computer == 2:
            result="You lose! Paper covers Rock"
            Score2+=1
        else:
            result="You win!  Rock smashes Scissors"
            Score1+=1
    elif player == 2:
        if computer == 3:
            result="You lose! Scissors cut Paper"
            Score2+=1
        else:
            result="You win! Paper covers Rock"
            Score1+=1
    elif player == 3:
        if computer == 1:
            result="You lose! Rock smashes Scissors"
            Score2+=1
        else:
            result="You win! Scissors cut Paper"
            Score1+=1
    print(result)
    

    canvas.itemconfig(res, text=result)
    canvas.itemconfig(s1, text=Score1)
    canvas.itemconfig(s2, text=Score2)

    print(player)
    print(computer)
    print("\n")




def clicked1(event):
    answer(1)

def clicked2(event):
    answer(2)

def clicked3(event):
    answer(3)



canvas.create_image(0, 0, image=image1, anchor=NW)
canvas.create_image(398, 2, image=round1, anchor=NW)
canvas.create_image(157, 353, image=user, anchor=NW)
canvas.create_image(728, 353, image=comp, anchor=NW)

RockButton=canvas.create_image(30, 584, image=rock, anchor=NW)
PaperkButton=canvas.create_image(157, 584, image=paper, anchor=NW)
ScissorsButton=canvas.create_image(288, 584, image=scissors, anchor=NW)

canvas.create_text(180, 255, fill = '#f3f3f3',font=("Impact", 50),text=UserName, anchor=NW)
canvas.create_text(771, 255, fill = '#f3f3f3',font=("Impact", 50),text=UserName2, anchor=NW)
s1=canvas.create_text(232, 144, fill = '#f3f3f3',font=("Impact", 60),text=Score1, anchor=NW)
s2=canvas.create_text(839, 144, fill = '#f3f3f3',font=("Impact", 60),text=Score2, anchor=NW)
res=canvas.create_text(540, 611, justify='center',fill = '#f3f3f3',font=("Impact", 25),text=result, anchor=NW)

canvas.tag_bind(RockButton, "<Button-1>", clicked1)
canvas.tag_bind(PaperkButton, "<Button-1>", clicked2)
canvas.tag_bind(ScissorsButton, "<Button-1>", clicked3)
canvas.pack()


root.mainloop()
