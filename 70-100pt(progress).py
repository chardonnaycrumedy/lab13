#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.



from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1) #tester
player = drawpad.create_oval(390,580,410,600, fill="red")

# Create your "enemies" here, before the class
enemy1 = drawpad.create_oval(20, 20, 100, 100, fill='green')
enemy2 = drawpad.create_oval(100, 100, 180, 180,fill='magenta')
enemy3 = drawpad.create_oval(300, 300,380, 380, fill='blue')
direction = 1

def animate():
    global direction
    x1, y1, x2, y2 = drawpad.coords(enemy1)
    if y2 > drawpad.winfo_height(): 
        direction = - 5
    elif y1 < 0:
        direction = 5
drawpad.move(enemy1,direction,0)
drawpad.after(1, animate)

class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="up", background= "green")
       	    self.up.grid(row=0,column=0)
       	    # Bind an event to the first button
       	    self.up.bind("<Button-1>", self.upClicked)
       	    
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=BOTTOM)
	
	def animate(self):
	    global drawpad
	    global player
	    # Remember to include your "enemies" with "global"
	    global enemy1
	    global enemy2
	    global enemy3	
	    			
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
	   
	def leftClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
	   
	def rightClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
	   
	def downClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
		
		
app = MyApp(root)
root.mainloop()