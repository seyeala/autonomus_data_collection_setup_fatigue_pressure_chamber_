import cv2
import time
import pendulum

img_counter = 0

foldername = "C:\\jpg"

samplename = input("Enter_sample_name:")
maxpressure = input("Entermaxpress in pka:")
period = int(input("cycle period in s:"))
rateofstorage = int(input("Store every x second:"))
camnum = int(input("camnumer:"))
currentcycle = int(input("current cycle:"))

cam = cv2.VideoCapture(camnum)

cv2.namedWindow("test")

test = 1
while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)
    if test == 1:
        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:
            # SPACE pressed
            img_name = "C:\\jpg\\opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
        test = 1

count = 0
while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)
    timenow = pendulum.now()
    slash = "\\"
    formatstr = ".png"
    cycles = str(int(currentcycle + count * rateofstorage / period))
    filepath = (
        foldername
        + slash
        + "name="
        + samplename
        + "pressure="
        + maxpressure
        + "cycle="
        + cycles
        + formatstr
    )
    print(filepath)
    cv2.imwrite(filepath, frame)
    print(filepath)
    time.sleep(rateofstorage)
    count = count + 1

cam.release()
cv2.destroyAllWindows()

cam.release()
cv2.destroyAllWindows()
