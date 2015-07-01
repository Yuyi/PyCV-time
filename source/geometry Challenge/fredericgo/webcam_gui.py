import cv2


def nothing(x):
    pass

def webcam_gui(filter_func, video_src=0):

    cap = cv2.VideoCapture(video_src)
    key_code = -1
    
    while(key_code == -1):
        # read a frame
        ret, frame = cap.read()
        
        # run filter with the arguments
        frame_out = filter_func(frame)
        
        # show the image
        cv2.imshow('Press any key to exit', frame_out)
        
        # wait for the key
        key_code = cv2.waitKey(10)

    cap.release()
    cv2.destroyAllWindows()


def trackbar_gui(filter_func, video_src=0):
    cap = cv2.VideoCapture(video_src)
    cv2.namedWindow('window')
    cv2.createTrackbar('aa', 'window', 0, 255, nothing)
    key_code = -1
    
    while(key_code == -1):
        aa = cv2.getTrackbarPos('aa','window')
        print aa
        # read a frame
        ret, frame = cap.read()
        
        # run filter with the arguments
        frame_out = filter_func(frame)
        
        # show the image
        cv2.imshow('window', frame_out)
        
        # wait for the key
        key_code = cv2.waitKey(10)

    cap.release()
    cv2.destroyAllWindows()

def edge_filter(frame_in):
    # convert into gray scale
    frame_gray = cv2.cvtColor(frame_in, cv2.COLOR_BGR2GRAY)
    # blur the image to reduce noise
    frame_blur = cv2.blur(frame_gray, (3,3))
    # Canny edge detection
    frame_out = cv2.Canny(frame_blur, 30, 120)
    
    return frame_out

    
    
def gray_filter(frame_in):
    # convert into gray scale
    frame_out = cv2.cvtColor(frame_in, cv2.COLOR_BGR2GRAY)
    
    return frame_out
    
    
    
if __name__ == "__main__":
    webcam_gui(edge_filter)