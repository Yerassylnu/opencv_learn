import cv2 as cv

#img = cv.imread('photos/cat1 .jpg')

#cv.imshow('Cat', img)

#cv.waitKey(0)

capture = cv.VideoCapture('videos/vcat1.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
