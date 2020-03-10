#This python script is designed to take numerosity videos (mp4?) and put grids on them using the following parameters:
# -i: the inpit video
# -t: the tank the video was in (e.g. earth)
# for example running the script would look like this:
# python make_a_grid.py -i /media/jenkins/DOBBY/TO_BE_GRIDDED/gambusia_18_TBD_male_Gary_9_1_9_12_75_none_L.mp4 -t earth

import cv2
import numpy as np
import sys
import argparse
import os
#import pdb


def check(video):
    """Check to make sure the files are as expected."""
    # check to make sure you can read the video
    cap = cv2.VideoCapture(video)
    ret, frame = cap.read()
    # if cap.get(3) != 2048.0 or cap.get(4) != 1536.0:
    # note numerosity videos are 1280 X 720
    #     sys.exit("video is of the wrong dimenisons")
    #     return False
    if ret == False:
        sys.exit("Problem reading the video.")
        return False


#Here's a diagram of the tank, and which lines represent line1, line2 etc.
#     --------1--------------------------------------------------
#     |				|	|			|
#     |				11	12			|
#     |				|	|			|
#     --------2--------------------------------------------------
#     |			|			|		|
#     |			|			|		|
#     |			|			|		|
#     5			6			7		8
#     |			|			|		|
#     | 		|			|		|
#     |			|			|		|
#     |			|			|		|
#     |			|			|		|
#     |			|			|		|
#     |			|			|		|
#     ---------3-------------------------------------------------
#     |				|	|			|
#     |				9	10			|
#     |				|	|			|
#     ---------4-------------------------------------------------

def draw_lines(img): 
	cv2.line(img,line1[0],line1[1],color,linewidth)   #1
	cv2.line(img,line2[0],line2[1],color,linewidth)   #2		
	cv2.line(img,line3[0],line3[1],color,linewidth)   #3
	cv2.line(img,line4[0],line4[1],color,linewidth)   #4
	cv2.line(img,line5[0],line5[1],color,linewidth)   #5
	cv2.line(img,line6[0],line6[1],color,linewidth)   #6
	cv2.line(img,line7[0],line7[1],color,linewidth)   #7
	cv2.line(img,line8[0],line8[1],color,linewidth)   #8
	cv2.line(img,line9[0],line9[1],color,linewidth)   #9
	cv2.line(img,line10[0],line10[1],color,linewidth)  #10
	cv2.line(img,line11[0],line11[1],color,linewidth)  #11
	cv2.line(img,line12[0],line12[1],color,linewidth)  #12
	return img



if __name__ == '__main__':

	"""Parse arguments."""
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--inputVideo", required = True, help = "path to the video")
	ap.add_argument("-t", "--tank", required = True, help = "tank in which video was taken")
	args = vars(ap.parse_args())
	video_path = args["inputVideo"]
	print ' '
	print ' '
	print ' '
	print 'video path'
	print video_path
	tank = args["tank"]
	print 'tank'
	print tank

	ret = check(video_path)
	if ret == False:
		sys.exit("")	

	color = (66,65,172)
	linewidth = 5
        if tank == "uranus":#~~paper
                line1 =[(69,220),(1236,220)]
                line2 =[(69,283),(1236,283)]
                line3 =[(69,731),(1236,731)]
                line4 =[(69,795),(1236,795)]
                line5 =[(69,220),(69,795)]
                line6 =[(371,288),(371,726)]
                line7 =[(949,288),(949,726)]
                line8 =[(1236,220),(1236,795)]
                line9 =[(571,726),(571,795)]
                line10 =[(710,726),(710,795)]
                line11 =[(587,220),(587,288)]
                line12 =[(729,220),(729,288)]
        if tank == "jupiter":#~~paper
                line1 =[(69,212),(1236,212)]
                line2 =[(69,268),(1236,268)]
                line3 =[(69,696),(1236,716)]
                line4 =[(69,759),(1236,779)]
                line5 =[(69,212),(69,759)]
                line6 =[(363,268),(363,695)]
                line7 =[(937,268),(937,705)]
                line8 =[(1236,212),(1236,779)]
                line9 =[(595,700),(595,769)]
                line10 =[(733,700),(733,769)]
                line11 =[(581,212),(581,268)]
                line12 =[(720,212),(720,268)]
        elif tank == "mercury":#~~paper
                line1 =[(66,201),(1218,201)]
		line2 =[(66,270),(1218,270)]
		line3 =[(66,698),(1218,690)]
		line4 =[(66,763),(1218,763)]
		line5 =[(66,201),(66,763)]
		line6 =[(366,270),(366,690)]
		line7 =[(931,270),(931,690)]
		line8 =[(1218,201),(1218,763)]
		line9 =[(568,690),(568,763)]
		line10 =[(708,690),(708,763)]
		line11 =[(583,201),(583,270)]
		line12 =[(716,201),(716,270)]
        elif tank == "earth":#~~paper
                line1 =[(66,231),(1228,231)]
		line2 =[(66,292),(1228,292)]
		line3 =[(66,728),(1228,738)]
		line4 =[(66,793),(1228,803)]
		line5 =[(66,231),(66,793)]
		line6 =[(357,292),(357,728)]
		line7 =[(931,292),(931,730)]
		line8 =[(1228,231),(1228,803)]
		line9 =[(575,735),(575,794)]
		line10 =[(718,735),(718,799)]
		line11 =[(575,231),(575,292)]
		line12 =[(711,231),(711,292)]

	elif tank == "albatross":#~~paper
		line1 =[(73,217),(1184,217)]
		line2 =[(73,279),(1184,279)]
		line3 =[(73,707),(1184,697)]
		line4 =[(73,767),(1184,757)]
		line5 =[(73,217),(73,767)]
		line6 =[(359,279),(359,707)]
		line7 =[(892,279),(892,697)]
		line8 =[(1184,217),(1184,757)]
		line9 =[(547,707),(547,762)]
		line10 =[(683,702),(683,762)]
		line11 =[(570,217),(570,279)]
		line12 =[(713,217),(713,279)]
	elif tank == "cougar":#~~paper
		line1 =[(73,247),(1214,217)]
		line2 =[(73,302),(1214,272)]
		line3 =[(73,748),(1214,718)]
		line4 =[(73,807),(1214,777)]
		line5 =[(73,249),(73,807)]
		line6 =[(361,301),(361,737)]
		line7 =[(925,286),(925,725)]
		line8 =[(1214,217),(1214,777)]
		line9 =[(587,737),(587,795)]
		line10 =[(733,733),(733,788)]
		line11 =[(570,237),(570,291)]
		line12 =[(720,232),(720,287)]
	elif tank == "eagle":#~~paper
		line1 =[(73,197),(1230,197)]
		line2 =[(73,255),(1230,255)]
		line3 =[(73,714),(1230,714)]
		line4 =[(73,777),(1230,777)]
		line5 =[(73,197),(73,777)]
		line6 =[(361,255),(361,714)]
		line7 =[(933,255),(933,714)]
		line8 =[(1230,197),(1230,777)]
		line9 =[(573,714),(573,772)]
		line10 =[(710,714),(710,772)]
		line11 =[(570,197),(570,255)]
		line12 =[(710,197),(710,255)]
	elif tank == "new_gorilla":#~~paper
		#use for rounds 23 and up! made using cc6 wes video 
		line1 =[(40,225),(1205,217)]
		line2 =[(40,287),(1206,279)]
		line3 =[(40,738),(1211,725)]
		line4 =[(40,796),(1211,783)]
		line5 =[(40,225),(40,796)]
		line6 =[(332,285),(332,733)]
		line7 =[(914,282),(920,726)]
		line8 =[(1205,217),(1211,783)] 
		line9 =[(533,733),(533,788)]
		line10 =[(669,733),(669,788)] 
		line11 =[(544,225),(544,283)]
		line12 =[(681,225),(681,277)]
	elif tank == "impala":#~~paper
		line1 =[(75,233),(1227,233)]
		line2 =[(75,293),(1227,293)]
		line3 =[(73,748),(1237,748)]
		line4 =[(70,808),(1241,808)]
		line5 =[(75,233),(70,808)] 
		line6 =[(368,293),(368,748)]
		line7 =[(939,293),(953,748)]
		line8 =[(1227,233),(1241,808)]
		line9 =[(584,748),(584,808)]
		line10 =[(721,748),(721,808)]
		line11 =[(572,233),(572,293)]
		line12 =[(716,233),(716,293)]
	elif tank == "kiwi":
		#~~paper
		line1 =[(59,254),(1226,236)]
		line2 =[(59,317),(1226,299)]
		line3 =[(69,762),(1256,742)]
		line4 =[(69,825),(1258,805)]
		line5 =[(59,260),(69,820)]
		line6 =[(363,313),(373,756)]
		line7 =[(919,302),(952,745)]
		line8 =[(1225,235),(1258,800)]
		line9 =[(587,755),(587,815)]
		line10 =[(730,753),(730,815)]
		line11 =[(564,248),(564,304)]
		line12 =[(702,244),(702,304)]
	elif tank == "old_gorilla":#~~paper based on wyatt 
		line1 =[(40,217),(1241,217)]
                line2 =[(40,280),(1241,280)]
                line3 =[(40,733),(1241,733)]
                line4 =[(40,791),(1241,791)]
                line5 =[(40,217),(40,791)]
                line6 =[(341,281),(341,727)]
                line7 =[(942,281),(942,727)]
                line8 =[(1241,217),(1241,791)]
                line9 =[(563,733),(563,791)]
                line10 =[(705,733),(705,791)]
                line11 =[(564,217),(564,281)]
                line12 =[(697,217),(697,281)]
	elif tank == "pluto":#~~paper
		line1 =[(50,205),(1205,197)]
                line2 =[(50,269),(1206,261)]
                line3 =[(60,717),(1211,704)]
                line4 =[(60,776),(1211,763)]
                line5 =[(50,205),(60,777)]
                line6 =[(341,269),(351,714)]
                line7 =[(912,269),(917,708)]
                line8 =[(1205,197),(1211,763)]
                line9 =[(564,717),(564,770)]
                line10 =[(699,714),(699,768)]
                line11 =[(562,205),(562,264)]
                line12 =[(698,205),(698,264)]
	elif tank =="haumea":#~~paper
		line1 =[(60,225),(1227,217)]
                line2 =[(60,291),(1227,283)]
                line3 =[(60,731),(1241,718)]
                line4 =[(60,796),(1241,783)]
                line5 =[(60,225),(60,796)]
                line6 =[(356,291),(356,731)]
                line7 =[(919,291),(935,723)]
                line8 =[(1225,217),(1241,783)]
                line9 =[(578,724),(578,793)]
                line10 =[(701,726),(701,788)]
                line11 =[(584,225),(584,285)]
                line12 =[(717,225),(717,283)]



	cap = cv2.VideoCapture(video_path)

	#set up video writer
	video_name = os.path.basename(video_path)
	name = "processed_" + video_name.split('.')[0] + '.avi'
	print("name of output file {}".format(name))
	#get size of video
	width = cap.get(3)
	print 'width'
	print width
	height = cap.get(4)
	print 'height'
	print height
	fourcc = cv2.cv.CV_FOURCC('M', 'J', 'P', 'G')
	out = cv2.VideoWriter(name, fourcc, cap.get(5), (int(width),int(height)))
	#read that mjpg is default and should work with avi types?
	print "starting loop"

	counter = 0
	ret = True
	while ret == True:
		ret, frame = cap.read()
        	frame = draw_lines(frame)
        	out.write(frame)
        	counter += 1
        	if counter % 100 == 0:
        		print "on frame {}".format(counter)

	out.release()
	cap.release()

print "video with boxes saved @ {}".format(name)
