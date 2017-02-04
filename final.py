import cv2
import numpy as np
import math
import sys
import pygame
import time 
import os 
import subprocess
import pyglet
import Tkinter
from Tkinter import *
from os import path
from Tkinter import Tk, Frame, BOTH
from PIL import Image, ImageTk

k = cv2.waitKey(10) & 0xFF


song = pyglet.media.load('instructions.mp3')



root = Tk()
root.title("ASL Translator Application")






im = Image.open('ASL.jpg')
tkimage = ImageTk.PhotoImage(im)
myvar=Tkinter.Label(root,image = tkimage)
myvar.place(relx=0.5, rely=0.735, anchor=CENTER)




# Shell Scripting Command Execution --------------------------------------------------------------------------------
cmd = "ultimate.sh"




def call_back():
	print "Button Pressed!"
	song.play()
	#pyglet.app.run()


def final_callback():

	"""
	"""

	

def exit():

	
		root.destroy()
			
			

def main():
	#subprocess.Popen(["bash", "ultimate.sh"])
	

	

	pygame.init()
	song = pygame.mixer.Sound('A.wav')
	clock = pygame.time.Clock()

	sound_tick = 0

	var_A = 0


	# Testing Bash Script in python 

	#subprocess.call("test_bash.sh")

	
	def createFile(dest):
	    name = letter_correspond
	    if not(path.isfile(dest + name)):
		f = open(dest + name,'w')
		f.write('\n'*5)
		f.close()






	co_ordinates_for_CONVEX_HULL = [[]]
	abc = []




	font = cv2.FONT_HERSHEY_SIMPLEX
	put_text_color = (18,0,255)
	put_text_pos = (60,50)



	lower_thresh1 = 129 
	upper_thresh1 = 255

	j = 0
	PI = math.pi


	"""img_test = cv2.imread("1.jpg",0)
	ret_1,thresh_test = cv2.threshold(img_test,125,255,0)
	xyz_test,contours_test,hierarchy_test = cv2.findContours(thresh_test,2,1)
	cnt_test_yo = [4]
	ret_1 = cv2.matchShapes(cnt_test_yo,cnt,1,0.0)
	print ret_1"""


	#letter_I_match_shape = cv2.imread('I.jpg',0)

	camera_index = int(sys.argv[1]) 
	cap = cv2.VideoCapture(camera_index)


	



	while(cap.isOpened()):




	    img_dofh = cv2.imread("D.png",0)
	    ret, img = cap.read()
	    cv2.rectangle(img,(60,60),(300,300),(255,255,2),4) #outer most rectangle 
	    crop_img = img[70:300, 70:300]
	    crop_img_2 = img[70:300, 70:300]

	    grey = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)

	    #edges = cv2.Canny(crop_img,100,200)



	    ############################### Corners Detection 


	    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	    
	    lower_red = np.array([0,150,50])
	    

	    upper_red = np.array([195,255,255])
	    
	    


	    
	    mask = cv2.inRange(hsv, lower_red, upper_red)
	    res = cv2.bitwise_and(img,img, mask= mask)




	    value = (35, 35)
	    blurred = cv2.GaussianBlur(grey, value, 0)
	    _, thresh1 = cv2.threshold(blurred, lower_thresh1, upper_thresh1, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
	    _, thresh_dofh = cv2.threshold(img_dofh, lower_thresh1, upper_thresh1, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
	    #defrt,thresh_for_I = cv2.threshold(letter_I_match_shape,125,255,0)



	    xyz,contours, hierarchy = cv2.findContours(thresh1.copy(),cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
	    xyz,contours_dofh, hierarchy_dofh = cv2.findContours(thresh_dofh,2,1)
	    #cnt_dofh = contours_dofh[1]

	    cnt = max(contours, key = lambda x: cv2.contourArea(x))
	    #cnt_m = contours[0]
	    #print cnt_m
	    area_of_contour = cv2.contourArea(cnt)
	    
	    x,y,w,h = cv2.boundingRect(cnt)
	    cv2.rectangle(crop_img,(x,y),(x+w,y+h),(0,0,255),1) # Red Rectangle 
	    #ratio_of_red_rect = h/w
	    #print ratio_of_red_rect

	    hull = cv2.convexHull(cnt)
	    drawing = np.zeros(crop_img.shape,np.uint8)

	    cv2.drawContours(drawing,[cnt],0,(0,255,0),0)
	    cv2.drawContours(drawing,[hull],0,(0,255,255),0)

	    hull  = cv2.convexHull(cnt,returnPoints = False)
	    #co_ordinates_for_CONVEX_HULL = cv2.convexHull(cnt,returnPoints = True)
	    defects = cv2.convexityDefects(cnt,hull)

	    

	    count_defects = 0
	    cv2.drawContours(thresh1, contours, -1, (0,255,0), 3)

	    for i in range(defects.shape[0]):
		s,e,f,d = defects[i,0]
		start = tuple(cnt[s][0])
		end = tuple(cnt[e][0])
		far = tuple(cnt[f][0])
		

		a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
		b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
		c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)

		

		angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 60
		cv2.circle(crop_img,far,4,[0,0,255],-1)                 # Red Circles###########################3
		#cv2.line(crop_img,start,end,[255,255,0],2)


		if angle <= 90:
		    count_defects += 1
		    #yeyo = cv2.circle(crop_img,far,1,[255,0,0],-1)
		

		cv2.line(crop_img,start,end,[0,255,0],3)


	    moment = cv2.moments(cnt)   
	    perimeter = cv2.arcLength(cnt,True)
	    area = cv2.contourArea(cnt)


	    (x,y),radius = cv2.minEnclosingCircle(cnt)
	    center = (int(x),int(y))
	    radius = int(radius)
	    cv2.circle(crop_img,center,radius,(255,0,0),2)

	    area_of_circle=PI*radius*radius



	    hull_test = cv2.convexHull(cnt)
	    hull_area = cv2.contourArea(hull_test)
	    solidity = float(area)/hull_area


	    aspect_ratio = float(w)/h

	    rect_area = w*h
	    extent = float(area)/rect_area

	    (x,y),(MA,ma),angle_t = cv2.fitEllipse(cnt)

	    #ret_1 = cv2.matchShapes(cnt,contours_dofh,1,0.0)
	    #print ret_1


	    
	    if area_of_circle - area < 5000:



		

		letter_correspond = "A.txt"

		destination ='Letters_stash_for_sounds/'
		createFile(destination)
		#raw_input("done!!!")

		output = "A"
		outFile = open('Letters_stash_for_sounds/A.txt', 'w')
		outFile.write(output)

	    	cv2.putText(img, "The Letter is :  A (CALIBRATED)", put_text_pos, font, 1 , put_text_color, 2, cv2.LINE_AA) 
		#cv2.putText(img, "The letter is :", (60,50), font, 1 , put_text_color, 2, cv2.LINE_AA)
		#cv2.putText(img, "A", (320,55), font, 2 , (50,100,190), 3, cv2.LINE_AA)

	    elif count_defects ==1:

		if angle_t < 10:


		    letter_correspond = "V.txt"

		    destination ='Letters_stash_for_sounds/'
		    createFile(destination)
		    #raw_input("done!!!")

		    output = "V"
		    outFile = open('Letters_stash_for_sounds/V.txt', 'w')
		    outFile.write(output)

		    #letter_correspond = "V.txt"


		    cv2.putText(img, "The Letter is :  V", put_text_pos, font, 1, put_text_color, 2, cv2.LINE_AA) 

		elif 40 < angle_t < 66:



		    letter_correspond = "C.txt"

		    destination ='Letters_stash_for_sounds/'
		    createFile(destination)
		    #raw_input("done!!!")

		    output = "C"
		    outFile = open('Letters_stash_for_sounds/C.txt', 'w')
		    outFile.write(output)


		    cv2.putText(img, "The Letter is :   C", put_text_pos, font, 1, put_text_color, 2, cv2.LINE_AA) 

		elif 20 < angle_t < 35:
			

			letter_correspond = "L.txt"

			destination ='Letters_stash_for_sounds/'
			createFile(destination)
			    #raw_input("done!!!")

			output = "L"
			outFile = open('Letters_stash_for_sounds/L.txt', 'w')
			outFile.write(output)


			cv2.putText(img, "The Letter is :   L", put_text_pos, font, 1, put_text_color, 2, cv2.LINE_AA)



		else:





		    letter_correspond = "Y.txt"

		    destination ='Letters_stash_for_sounds/'
		    createFile(destination)
		    #raw_input("done!!!")

		    output = "Y"
		    outFile = open('Letters_stash_for_sounds/Y.txt', 'w')
		    outFile.write(output)

		    cv2.putText(img,"The Letter is :  Y", put_text_pos, font, 1, put_text_color, 2, cv2.LINE_AA)
		

		

		#print "Its 2"
	    elif count_defects == 2:  # Its either W or F

		if angle_t > 100:

		    letter_correspond = "F.txt"

		    destination ='Letters_stash_for_sounds/'
		    createFile(destination)
		    #raw_input("done!!!")

		    output = "F"
		    outFile = open('Letters_stash_for_sounds/F.txt', 'w')
		    outFile.write(output)

		    cv2.putText(img, "The Letter is :  F", put_text_pos, font, 1, put_text_color, 2, cv2.LINE_AA)

		else:

		    letter_correspond = "W.txt"

		    destination ='Letters_stash_for_sounds/'
		    createFile(destination)
		    #raw_input("done!!!")

		    output = "W"
		    outFile = open('Letters_stash_for_sounds/W.txt', 'w')
		    outFile.write(output)

		    cv2.putText(img, "The Letter is :  W", put_text_pos, font, 1, put_text_color, 2, cv2.LINE_AA) 
	    
	    elif count_defects == 4:





		letter_correspond = "CALIBRATE.txt"

		destination ='Letters_stash_for_sounds/'
		createFile(destination)
		#raw_input("done!!!")

		output = "CALIBRATE"
		outFile = open('Letters_stash_for_sounds/CALIBRATE.txt', 'w')
		outFile.write(output)


		cv2.putText(img,"Hello There ! Callibrate by letter A", put_text_pos, font,1, put_text_color, 2, cv2.LINE_AA) 
		


	    else:
	    	if area > 12000:

	    	    
		    letter_correspond = " B.txt"

		    destination ='Letters_stash_for_sounds/'
		    createFile(destination)
		    #raw_input("done!!!")

		    output = "B"
		    outFile = open('Letters_stash_for_sounds/B.txt', 'w')
		    outFile.write(output)

	    	    cv2.putText(img,"The Letter is :  B", put_text_pos, font, 1, put_text_color, 2, cv2.LINE_AA) 
		    
	    	else:

		    if solidity < 0.85:


		        if aspect_ratio < 1:

		            if angle_t < 20:

		                letter_correspond = " D.txt"

		                destination ='Letters_stash_for_sounds/'
		                createFile(destination)
		                #raw_input("done!!!")

		                output = "D"
		                outFile = open('Letters_stash_for_sounds/D.txt', 'w')
		                outFile.write(output)

		                cv2.putText(img,"The Letter is :  D", put_text_pos, font, 1, put_text_color, 2, cv2.LINE_AA)

		            elif 169<angle_t <180:

		                letter_correspond = " I.txt"

		                destination ='Letters_stash_for_sounds/'
		                createFile(destination)
		                #raw_input("done!!!")

		                output = "I"
		                outFile = open('Letters_stash_for_sounds/I.txt', 'w')
		                outFile.write(output)

		                cv2.putText(img,"The Letter is :  I", put_text_pos, font, 1, put_text_color, 2, cv2.LINE_AA)

		            elif angle_t < 168:
			    
		            	letter_correspond = " J.txt"

		                destination ='Letters_stash_for_sounds/'
		                createFile(destination)
		                #raw_input("done!!!")

		                output = "J"
		                outFile = open('Letters_stash_for_sounds/J.txt', 'w')
		                outFile.write(output)

		                cv2.putText(img,"The Letter is :  J", put_text_pos, font, 1, put_text_color, 2, cv2.LINE_AA)







		        elif aspect_ratio > 1.01:

		            letter_correspond = " Y.txt"

		            destination ='Letters_stash_for_sounds/'
		            createFile(destination)
		            #raw_input("done!!!")

		            output = "Y"
		            outFile = open('Letters_stash_for_sounds/Y.txt', 'w')
		            outFile.write(output)

		            cv2.putText(img,"The Letter is :  Y", put_text_pos, font, 1, put_text_color, 2, cv2.LINE_AA) 

		    
		    else:

		        if angle_t > 30 and angle_t < 100:

		            letter_correspond = " H.txt"

		            destination ='Letters_stash_for_sounds/'
		            createFile(destination)
		            #raw_input("done!!!")

		            output = "H"
		            outFile = open('Letters_stash_for_sounds/H.txt', 'w')
		            outFile.write(output)

		            cv2.putText(img,"The Letter is :  H", put_text_pos, font, 1, put_text_color, 2, cv2.LINE_AA) 




		           
		        elif angle_t > 120:
				
				



		            letter_correspond = " I.txt"

		            destination ='Letters_stash_for_sounds/'
		            createFile(destination)
		            #raw_input("done!!!")

		            output = "I"
		            outFile = open('Letters_stash_for_sounds/I.txt', 'w')
		            outFile.write(output)

		            cv2.putText(img,"The Letter is :  I", put_text_pos, font, 1, put_text_color, 2, cv2.LINE_AA)



		        else:

		            letter_correspond = " U.txt"

		            destination ='Letters_stash_for_sounds/'
		            createFile(destination)
		            #raw_input("done!!!")

		            output = "U"
		            outFile = open('Letters_stash_for_sounds/U.txt', 'w')
		            outFile.write(output)

		            cv2.putText(img,"The Letter is :  U", put_text_pos, font, 1, put_text_color, 2, cv2.LINE_AA) # 

		

	    #crop_img[dst>0.01*dst.max()]=[255,0,0]
	    cv2.imshow('Gesture', img)
	    cv2.imshow('Contours', drawing)
	    cv2.imshow('Defects', crop_img)
	    cv2.imshow('Binary Image', thresh1)
	   


	    

	    # Testing Parameters :

	    #print co_ordinates_for_CONVEX_HULL
	    #print abc
	    #cv2.imshow('something',yeyo)
	    #print area_of_contour,co_ordinates_for_CONVEX_HULL
	    #print moment
	    print "Perimeter is :" ,perimeter
	    #print "The area is:", area
	    #print defects
	    #print crop_img.shape
	    #print defects.shape
	    #print dist_from_farthest
	    #print count_defectsd
	    #print hull 
	    #print far      
	    #print equi_diameter
	    print 'Radius:',PI*radius*radius ,"Area:", area
	    print area_of_circle - area
	    print "The solidity is:" ,solidity 
	    print "The aspect ratio is :", aspect_ratio 
	    print "The number of convexity defects are :",count_defects
	    print "The extent is :",extent
	    print "the angle is:", angle_t
	    print '\033[91m'+"The area of effective circle is " +'\033[0m',area_of_circle - area




	    """
	    img1 = cv2.imread('match_shapes_test.png',0)
	    #img2 = cv2.imread(thresh1,0)

	    ret, thresh_8 = cv2.threshold(img1, 127, 255,0)
	    ret, thresh_9 = cv2.threshold(thresh1, 127, 255,0)
	    xcv,contours_8,hierarchy = cv2.findContours(thresh_8,2,1)
	    cnt1 = contours_8[0]
	    vbgf,contours_9,hierarchy = cv2.findContours(thresh_9,2,1)
	    cnt_9 = max(contours_9, key = lambda s: cv2.contourArea(s))

	    ret = cv2.matchShapes(cnt1,cnt_9,1,0.0)
	    print "The probability is :",ret """

	    
	    k = cv2.waitKey(10) & 0xFF 



	    #if k == ord('s'):
	    #    cv2.imwrite('testing_match.png',crop_img_2)

	    if k == ord('s'):

	    	os.system("gnome-terminal -e 'bash -c \"bash ultimate.sh; exec bash\"'")
	    	pid = os.getpid()


	    elif k == 27 or k == ord('q')  :


			break


		




  
######################################################################################################################################
w = Label(root,text="Press the button below if you want to Listen to the instructions.")
w.config(width=75)
w.config(font=("Helvetica", 30))
w.pack()


b1 = Button(root, text="Instructions",command=call_back,bg="lightgreen")
b1.config(font=("Times New Roman", 35,"bold"))
b1.pack()

x = Label(root,text="Press the button below to run the application (Then,press s for sound).")
x.config(width=75)
x.config(font=("Helvetica", 30))
x.pack()


b2 = Button(root, text="Run",command=main,bg="gold1")
b2.config(font=("Times New Roman", 35,"bold"))
b2.pack()



z = Label(root,text="Press ESCAPE and then the button below to exit.")
z.config(width=75)
z.config(font=("Helvetica", 30))
z.pack()


b3 = Button(root, text="Exit",command=exit,bg="salmon")
b3.config(font=("Raavi", 35,"bold"))
b3.pack()







root.mainloop()
