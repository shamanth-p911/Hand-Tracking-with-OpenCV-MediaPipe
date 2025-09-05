import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
w=1280
h=720
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,h)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,w)

while cap.isOpened():
    myhands=[]
    success, frame = cap.read()
    if not success:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            myHand=[]
            #mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            for landmark in hand_landmarks.landmark:
                myHand.append((int(landmark.x*w),int(landmark.y*h)))
                
            cv2.circle(frame,myHand[4],10,(255,255,255),-1)
            cv2.circle(frame,myHand[8],10,(255,255,255),-1)
            cv2.line(frame,myHand[4],myHand[8],(0,0,0),6)
            
            myhands.append(myHand)
            print(myhands)
            print("")
    cv2.imshow("Hand Tracking", frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()