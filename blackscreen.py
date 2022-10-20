#import cv2 & numpy library
import cv2
import numpy as np


#Starting VideoCapture
video = cv2.VideoCapture(0) 
image = cv2.imread("me.jpeg") 

#Read the image which will be shown when the black object will get masked and save it in an “image” variable
while True: 
  
    ret, frame = video.read() 
    print(frame)
    #Use the code block to resize the image and frame.(as shown in the hint1)
    frame=cv2.resize(frame,(640,480))
    image=cv2.resize(image,(640,480))

    #Use the code block to pass the faint shade value and dark shade value of RBG(as shown in the hint2)
    u_black =np.array([104,153,70])
    l_black=np.array([30,30,0])

    #Code block to use inRange() and bitwise_and().(as shown in hint3)
    mask=cv2.inRange(frame,l_black,u_black)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    #Code block to use the where function.(as shown in hint4)
    f=frame - res
    f=np.where(f==0,image,f)

    #Show the real video and masked video.
    cv2.imshow("video", frame) 
    cv2.imshow("mask", f) 
    
    #Break the loop if the user presses “Esc” or “Q”.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 

#Release the video and close the video windows.
video.release() 
cv2.destroyAllWindows()

