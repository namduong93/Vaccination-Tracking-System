from tesserocr import PyTessBaseAPI
from VideoStream import *
import re, cv2


def ocr():
    """
[Warning] This function should not be directly called
Use the camera to capture pictures that will used to detect student id.

In detail, it use tesserocr to detech all lettersa nd use regex to find the student id.

============
Parameter
    None

=============
Return
    String
        detect the studentid

    """
    ocr_api = PyTessBaseAPI(path=r'./tessdata') 
    
    captures = 0
    cps = RateCounter().start()
    video_stream = VideoStream(0).start()  
    print("\n[OCR]: Push c to detect Student ID. Push q to exit\n")

    try:
        while True:
            pressed_key = cv2.waitKey(1) & 0xFF
        
            # Quit
            if pressed_key == ord('q'):
                video_stream.stop_process()
                cv2.destroyAllWindows()
                print("OCR stream stopped\n")
                return " "

            # Detect
            frame = video_stream.frame  
            if pressed_key == ord('c'):
                captures = capture_image(frame, captures)
                print('[OCR]: Detecting')
                ocr_api.SetImageFile(r'./target.jpg')
                res = ocr_api.GetUTF8Text()
                res = re.search(r"[\d]{8}[\w]", res)
                if res:
                    print('[OCR]: Detected: ' + res.group(0)[:-1])
                    video_stream.stop_process()
                    cv2.destroyAllWindows() 
                    return str(res.group(0)[:-1])
                else:
                    print('[OCR]: Not Detected, Please Try Again')

            # Show frame
            cv2.imshow("OCR", frame)
            cps.increment()
    except:
        video_stream.stop_process()
        cv2.destroyAllWindows() 
        return ''

def detectCamera():
    """
Detect if there is a avaiable camera

==========
Parameter
    None

==========
Return
    Bool
        Ture means yes, False means no avaiable camera

    """
    try:
        cap = cv2.VideoCapture(0) 
        if cap is None or not cap.isOpened():
            return False
        else:
            return True
    except:
        return False

def ocrStudentID():
    """
Use the camera to capture pictures that will used to detect student id.

It is a wapper for ocr(), which prevent some issue caused by the computer system by while-true loop

==========
Parameter
    None

==========
Return
    String
        detect the studentid

    """

    if detectCamera():
        while True:
            try:
                res = ocr()
                if res:
                    return res
            except:
                pass
    else:
        print("[OCR]: Camera is not avaiable. Please Check!")
        return ''