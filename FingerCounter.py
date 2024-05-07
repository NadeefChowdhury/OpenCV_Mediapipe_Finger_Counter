import mediapipe as mp
import cv2
import time
import os
folderPath = 'Fingers'
myList = os.listdir('Fingers')
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    print(f'{folderPath}/{imPath}')
    overlayList.append(image)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)



cy8 = 0
cy6 = 0
cx4 = 0
cx5 = 0
cy12 = 0
cy10 = 0
cy16 = 0
cy14 = 0
cy20 = 0
cy18 = 0


while True:
    success,img = cap.read()
    
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results =  hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for ID, lm in enumerate(handLms.landmark):
                fingers = []
                h,w,c = img.shape
                cx,cy= int(lm.x*w), int(lm.y*h)
                #print(ID, cx, cy)
                if ID == 0:
                    cv2.circle(img,(cx,cy),20,(0,0,0),cv2.FILLED)
                
                #THUMB
                if ID == 4:
                    cx4 = cx
                    
                if ID == 5:
                    cx5 = cx
                if cx4>cx5:
                    fingers.append(1)
                else:
                    fingers.append(0)    
                
                
                
                #INDEX
                if ID == 8:
                    cy8 = cy
                    
                if ID == 6:
                    cy6 = cy
                if cy8<cy6:
                    fingers.append(1)
                else:
                    fingers.append(0)
                    
                #MIDDLE
                if ID == 12:
                    cy12 = cy
                    
                if ID == 10:
                    cy10 = cy
                if cy12<cy10:
                    fingers.append(1)
                else:
                    fingers.append(0)
                
                
                
                #RING
                if ID == 16:
                    cy16 = cy
                    
                if ID == 14:
                    cy14 = cy
                if cy16<cy14:
                    fingers.append(1)
                else:
                    fingers.append(0)
                
                
                
                #LITTLE
                if ID == 20:
                    cy20 = cy
                    
                if ID == 18:
                    cy18 = cy
                if cy20<cy18:
                    fingers.append(1)
                else:
                    fingers.append(0)
                
                
            
                
                totalFingers = fingers.count(1)
                print(totalFingers)
                img[0:overlayList[totalFingers-1].shape[0], 0:overlayList[totalFingers-1].shape[1]] = overlayList[totalFingers-1]
               
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,"FPS: " + str(int(fps)),(300, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,0), 5 )        
    cv2.namedWindow("Video", cv2.WINDOW_NORMAL) 
    cv2.imshow("Video", img)
    
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break

cv2.destroyAllWindows()