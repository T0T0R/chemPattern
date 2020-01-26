import turtle as trt;
import random as rd;
from tkinter import *;

from PIL import Image, ImageFilter, ImageGrab;

length = 50;    # Length of a segment.
angles = [60,-60];   # Possible values for an angle.
dotPerc = 0.9;  # Whiteness of dots.



def drawLine(depth):
    trt.down();
    trt.right(rd.choice(angles));
    trt.forward(length);
    trt.up();
    
    if (depth < 11):
        for _ in range(2):
            atomType = rd.randrange(10);
            
            if (atomType < 6):   # If ramification for this nod (not a hydrogen):
                
                    
                nodPos = trt.pos();         # - remember position and orientation at this nod;
                nodAngle = trt.heading();
                drawLine(depth+1);          # - and draw from there.
            
                # Then put the turtle back at the nod.
                trt.goto(nodPos);
                trt.setheading(nodAngle);
                
                if(atomType==0):    # Draw the dot.
                    #trt.dot(length/3, "grey");
                    trt.dot(length/3, (1.0,0.81,0.41));
                else:
                    trt.dot(length/3, (dotPerc, dotPerc, dotPerc));
                 
              
    
    
i=0;
while True:
    trt.reset();    
    trt.speed(1000);   # Drawing speed.
    trt.bgcolor("#7d004d");
    trt.pencolor("white")
    trt.hideturtle();   
    
    drawLine(1);
    
    ts = trt.getscreen();
    cv = ts.getcanvas();
    cv.pack();


    x = cv.winfo_rootx();
    y = cv.winfo_rooty();
    w = cv.winfo_width();
    h = cv.winfo_height();
    img= ImageGrab.grab((x+2, y+2, x+w-2, y+h-2)).save("c"+str(i)+".png", 'png');

    i +=1;
