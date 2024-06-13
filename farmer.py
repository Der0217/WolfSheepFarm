import tkinter
from tkinter import messagebox
import random
import os,sys
sheep='L'
wolf='L'
farmer='L'
vegetable='L'
click="NULL"

#----------------------佈景------------------------------
root=tkinter.Tk()

root.geometry('1280x1060')
canvas=tkinter.Canvas(width=1280,height=1060,bg="white")

backgroud=tkinter.PhotoImage(file="backgroud.png")
canvas.create_image(0,0,image=backgroud,anchor='nw')
canvas.pack()

wolf_img=tkinter.PhotoImage(file="wolf.png")
canvas.create_image(60,700,image=wolf_img,tag="wolf")

sheep_img=tkinter.PhotoImage(file="sheep.png")
canvas.create_image(180,700,image=sheep_img,tag="sheep")

vegetable_img=tkinter.PhotoImage(file="vegetable.png")
canvas.create_image(300,700,image=vegetable_img,tag="vegetable")

boat_img=tkinter.PhotoImage(file="boat.png")
canvas.create_image(520,665,image=boat_img,tag="boat")

farmer_img=tkinter.PhotoImage(file="farmer.png")
canvas.create_image(660,620,image=farmer_img,tag="farmer")
#------------------------------------------------------

#遊戲結束判斷是否要重玩or結束程式
def check_decide(decide):
    global sheep,wolf,farmer,vegetable,click
    if(decide=='yes'):
        sheep='L'
        wolf='L'
        farmer='L'
        vegetable='L'
        click="NULL"
        canvas.delete("wolf")
        canvas.delete("sheep")
        canvas.delete("vegetable")
        canvas.delete("boat")
        canvas.delete("farmer")
        canvas.create_image(60,700,image=wolf_img,tag="wolf")
        canvas.create_image(180,700,image=sheep_img,tag="sheep")
        canvas.create_image(300,700,image=vegetable_img,tag="vegetable")
        canvas.create_image(520,665,image=boat_img,tag="boat")
        canvas.create_image(660,620,image=farmer_img,tag="farmer")
    else:
        sys.exit()
#檢查是否勝利
def checkwinorlose(wolf,sheep,vegetable,farmer):
    if(wolf=='R'and vegetable=='R'and sheep=='R'and farmer=='R'):
        decide=tkinter.messagebox.askquestion(title='遊戲結束', message="<成功通關>\n是否重玩or關閉遊戲")
    elif((wolf=='R' and sheep=='R' and farmer=='L')or(wolf=='L' and sheep=='L' and farmer=='R')):
        decide=tkinter.messagebox.askquestion(title='遊戲結束', message='失敗!!<羊被狼吃>\n是否重玩or關閉遊戲')
    elif((sheep=='R' and vegetable=='R' and farmer=='L')or(sheep=='L' and vegetable=='L' and farmer=='R')):
        decide=tkinter.messagebox.askquestion(title='遊戲結束', message='失敗!!<菜被羊吃>\n是否重玩or關閉遊戲')
    check_decide(decide=decide)
#--------click後上船判斷------------        
def wolf_move():
    global click
    if(click=="NULL"):
        if(wolf==farmer):
            canvas.delete("wolf")
            if wolf in ['L'] and farmer=='L':
                canvas.create_image(500,615,image=wolf_img,tag="wolf")
            elif wolf=='R' and farmer=='R':
                canvas.create_image(700,615,image=wolf_img,tag="wolf")
            click="wolf"
    elif(click=="wolf"):
        if (wolf==farmer):
            canvas.delete("wolf")
            if wolf in ['L'] and farmer=='L':
                canvas.create_image(60,700,image=wolf_img,tag="wolf")
                
            elif wolf=='R' and farmer=='R':
                canvas.create_image(1220,700,image=wolf_img,tag="wolf")
        click="NULL"
        
def sheep_move():
    global click
    if click in ["NULL"]:
        if(sheep==farmer):
            canvas.delete("sheep")
            if sheep in ['L'] and farmer=='L':
                canvas.create_image(500,615,image=sheep_img,tag="sheep")
            if sheep in ['R'] and farmer=='R':
                canvas.create_image(700,615,image=sheep_img,tag="sheep")   
            click="sheep"
    elif(click=="sheep"):
        if(sheep==farmer):
            canvas.delete("sheep")
            if sheep in ['L'] and farmer=='L':
                canvas.create_image(180,700,image=sheep_img,tag="sheep")
            if sheep in ['R'] and farmer=='R':
                canvas.create_image(1100,700,image=sheep_img,tag="sheep")
            click="NULL"  
            
def vegetable_move():
    global click
    if click in ["NULL"]:
        if(vegetable==farmer):
            canvas.delete("vegetable")
            if vegetable in ['L'] and farmer=='L':
                canvas.create_image(500,615,image=vegetable_img,tag="vegetable")
            if vegetable in ['R'] and farmer=='R':               
                canvas.create_image(700,615,image=vegetable_img,tag="vegetable")  
            click="vegetable"
    elif(click=="vegetable"):
        if(vegetable==farmer):
            canvas.delete("vegetable")
            if vegetable in ['L'] and farmer=='L':              
                canvas.create_image(300,700,image=vegetable_img,tag="vegetable")
            if vegetable in ['R'] and farmer=='R':
                canvas.create_image(980,700,image=vegetable_img,tag="vegetable")
            click="NULL" 
#------------------------------------------  
          
#移動判斷
def self_move():
    global click,wolf,sheep,farmer,vegetable
    canvas.delete("boat")
    canvas.delete("farmer")
    match click:
        case "wolf":
            canvas.delete("wolf")
            if(wolf=='L'):
                canvas.create_image(520+280,665,image=boat_img,tag="boat")
                canvas.create_image(660+280,620,image=farmer_img,tag="farmer")
                canvas.create_image(1220,700,image=wolf_img,tag="wolf")
                wolf='R'
                farmer='R'    
            else:
                canvas.create_image(520,665,image=boat_img,tag="boat")
                canvas.create_image(660,620,image=farmer_img,tag="farmer")
                canvas.create_image(60,700,image=wolf_img,tag="wolf")
                wolf='L'
                farmer='L'
        
        case "sheep":
            canvas.delete("sheep")
            if(sheep=='L'):
                canvas.create_image(520+280,665,image=boat_img,tag="boat")
                canvas.create_image(660+280,620,image=farmer_img,tag="farmer")
                canvas.create_image(1100,700,image=sheep_img,tag="sheep")
                sheep='R'
                farmer='R'
            else:
                canvas.create_image(520,665,image=boat_img,tag="boat")
                canvas.create_image(660,620,image=farmer_img,tag="farmer")
                canvas.create_image(180,700,image=sheep_img,tag="sheep")
                sheep='L'
                farmer='L'
        case "vegetable":
            canvas.delete("vegetable")
            if(vegetable=='L'):
                canvas.create_image(520+280,665,image=boat_img,tag="boat")
                canvas.create_image(660+280,620,image=farmer_img,tag="farmer")
                canvas.create_image(980,700,image=vegetable_img,tag="vegetable")
                vegetable='R'
                farmer='R'
            else:
                canvas.create_image(520,665,image=boat_img,tag="boat")
                canvas.create_image(660,620,image=farmer_img,tag="farmer")
                canvas.create_image(300,700,image=vegetable_img,tag="vegetable")
                vegetable='L'
                farmer='L'
        case _:
            if(farmer=='L'):
                canvas.create_image(520+280,665,image=boat_img,tag="boat")
                canvas.create_image(660+280,620,image=farmer_img,tag="farmer")
                farmer='R'
            else:
                canvas.create_image(520,665,image=boat_img,tag="boat")
                canvas.create_image(660,620,image=farmer_img,tag="farmer")
                farmer='L'
    click="NULL"
    checkwinorlose(wolf=wolf,sheep=sheep,vegetable=vegetable,farmer=farmer)          

#按鈕                
vegetable_btn=tkinter.Button(canvas,text="菜",command=vegetable_move,width=10,height=5).place(x=300,y=180)
wolf_btn=tkinter.Button(canvas,text="狼",command=wolf_move,width=10,height=5).place(x=100,y=180)
sheep_btn=tkinter.Button(canvas,text="羊",command=sheep_move,width=10,height=5).place(x=200,y=180)
self_btn=tkinter.Button(canvas,text="搭乘",command=self_move,width=10,height=5).place(x=400,y=180)
root.mainloop()