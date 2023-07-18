import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

#img_core = cv.imread('photos/core.jpg')
#cv.imshow('Core Image', img_core)

#cv.waitKey(0)

capture_earth = cv.VideoCapture('videos/vearth.mp4')

while True:
    isTrue, frame = capture_earth.read()

    if frame is None:
        break
    
    frame_resized = rescaleFrame(frame,scale=.2)

    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture_earth.release()
cv.destroyAllWindows()