import cv2, time

video=cv2.VideoCapture("D:\TORRENTS\CACHE\El caso Winslow (1999).avi")

a=0

while True:
    a=a+1
    check, frame = video.read()


    print(check)
    print(frame)

    cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #time.sleep(3)
    cv2.imshow("Capturing",frame)

    key=cv2.waitKey(40)

    if key==ord('q'):
        break

print(a)
video.release()
cv2.destroyAllWindows()
