import cv2 as cv

img = cv.imread('photos/cat1.jpg')
cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    #Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img) 
cv.imshow('Image', resized_image)

def changeRes(width,height):
    #Live Video
    capture.set(3,width)
    capture.set(4,height)

capture = cv.VideoCapture('videos/vcat1.mp4')

while True:
    isTrue, frame = capture.read()

    if frame is None:
        # Handle the end of the video
        break

    frame_resized = rescaleFrame(frame,scale=.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()