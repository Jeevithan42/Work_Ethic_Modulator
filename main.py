import time
from tkinter import *
from tkinter import messagebox

box = Tk()
rest = 0


box.geometry("200x300")

box.title("Timer")


def mainloop():
  global rest
  tempr = int(restime.get()) + rest
  n = 0
  for i in range (0, (tempr*60)):
    print(i)
    n = n+1
    if n == 60:
      n = 0
      tempr = tempr-1
      if i == 0 or tempr == -1:
        print("Rest Over!")
        messagebox.showinfo("Rest Over", "Time to get to work!") 
        rest = 0
        timer()
        
        
    box.update()
    time.sleep(1)
    
  
  
    
  



def submit():
  global rest
  temp1 = int(hour.get())
  temp2 = int(minute.get())
  temp3 = int(second.get())
  if temp1 == 00 or temp1 == 0 :
    nuls = 0 
  else:
    nuls = 1
  temp4 = int(temp1)*3600 + int(temp2)*60 + int(temp3)
  for i in range(0, temp4):
    temp1 = int(hour.get())
    temp2 = int(minute.get())
    temp3 = int(second.get())
    temp3 = temp3 - 1
    if temp3 == 0 or temp3 == -1 or temp3 == 00:
      if temp2 == 0 or temp2 == 00:
        if temp1 == 0 or temp1 == 00:
          print("Time Up!") 
          test = messagebox.askquestion("Your Time is Up!", """Would you like to use your rest now (yes) or bank it for later and keep working (no)?""") 
          if test == 'yes':
            mainloop()
          elif test == 'no':
            tempr = int(restime.get())
            rest = rest + tempr
            timer()
          break
        elif int(temp1) > 0:
          temp1 = str(int(int(temp1)-1))
          temp2 = str(60)
          temp3 = str(60)
      elif temp2 > 0:
        temp2 = temp2 - 1
        temp3 = str(60)
    

    hour.set(temp1)
    minute.set(temp2)
    second.set(str(temp3))
    box.update()
    time.sleep(1)




        


        
      
        







def timer():
  hour = StringVar()
  minute = StringVar()
  second = StringVar()

  restime = StringVar()
  hour.set("00")
  minute.set("00")
  second.set("00")

  restime.set("0000")

  hourslot = Entry(box, width = 2, font = ("Arial", 20,""),     textvariable = hour)
  hourslot.place(x=30,y=50)
  minuteslot = Entry(box, width = 2, font = ("Arial", 20,""),   textvariable = minute)
  minuteslot.place(x=80, y=50)
  secondslot = Entry(box, width = 2, font = ("Arial", 20,""), textvariable = second)
  secondslot.place(x=130, y=50)

  restime = Entry(box, width = 4, font= ("Arial", 20, ""), textvariable = restime)
  restime.place(x=60, y=100)

  btn = Button(box, text = "Set times", bd = "5", command = submit)
  btn.place(x=60, y=150)
  
  

  box.mainloop()
  
  
  
hour = StringVar()
minute = StringVar()
second = StringVar()

restime = StringVar()
hour.set("00")
minute.set("00")
second.set("00")

restime.set("0000")

hourslot = Entry(box, width = 2, font = ("Arial", 20,""),     textvariable = hour)
hourslot.place(x=30,y=50)
minuteslot = Entry(box, width = 2, font = ("Arial", 20,""),   textvariable = minute)
minuteslot.place(x=80, y=50)
secondslot = Entry(box, width = 2, font = ("Arial", 20,""), textvariable = second)
secondslot.place(x=130, y=50)

restime = Entry(box, width = 4, font= ("Arial", 20, ""), textvariable = restime)
restime.place(x=60, y=100)

btn = Button(box, text = "Set times", bd = "5", command = submit)
btn.place(x=60, y=150)
  
  

box.mainloop()


timer()
