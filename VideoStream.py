import cv2
import time
from threading import Thread

"""
This functions are copied from a project, which will offer some api to handle cv2

Reference
https://github.com/nathanaday/RealTime-OCR
"""

class VideoStream:
    """
    Class for grabbing frames from CV2 video capture.

    `Attributes:`
        stream: CV2 VideoCapture object
        grabbed: bool indication whether the frame from VideoCapture() was read correctly
        frame: the frame from VideoCapture()
        stopped: bool indicating whether the process has been stopped

    `Methods:`
        start()
            Creates a thread targeted at get(), which reads frames from CV2 VideoCapture
        get()
            Continuously gets frames from CV2 VideoCapture and sets them as self.frame attribute
        get_video_dimensions():
            Gets the width and height of the video stream frames
        stop_process()
            Sets the self.stopped attribute as True and kills the VideoCapture stream read
    """

    def __init__(self, src=0):
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False

    def start(self):
        """
        Creates a thread targeted at get(), which reads frames from CV2 VideoCapture

        :return: self
        """
        Thread(target=self.get, args=()).start()
        return self

    def get(self):
        """
        Continuously gets frames from CV2 VideoCapture and sets them as self.frame attribute
        """
        while not self.stopped:
            (self.grabbed, self.frame) = self.stream.read()

    def get_video_dimensions(self):
        """
        Gets the width and height of the video stream frames

        :return: height `int` and width `int` of VideoCapture
        """
        width = self.stream.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = self.stream.get(cv2.CAP_PROP_FRAME_HEIGHT)
        return int(width), int(height)

    def stop_process(self):
        """
        Sets the self.stopped attribute as True and kills the VideoCapture stream read
        """
        self.stopped = True

def capture_image(frame, captures=0):
    """
    Capture a .jpg during CV2 video stream. Saves to a folder /images in working directory.

    :param frame: CV2 frame to save
    :param captures: (optional) Number of existing captures to append to filename

    :return: Updated number of captures. If capture param not used, returns 1 by default
    """
    cv2.imwrite(r'./target.jpg', frame)
    captures += 1
    return captures


class RateCounter:
    """
    Class for finding the iterations/second of a process

    `Attributes:`
        start_time: indicates when the time.perf_counter() began
        iterations: determines number of iterations in the process

    `Methods:`
        start(): Starts a time.perf_counter() and sets it in the self.start_time attribute
        increment(): Increases the self.iterations attribute
        rate(): Returns the iterations/seconds
    """

    def __init__(self):
        self.start_time = None
        self.iterations = 0

    def start(self):
        """
        Starts a time.perf_counter() and sets it in the self.start_time attribute

        :return: self
        """
        self.start_time = time.perf_counter()
        return self

    def increment(self):
        """
        Increases the self.iterations attribute
        """
        self.iterations += 1

    def rate(self):
        """
        Returns the iterations/seconds
        """
        elapsed_time = (time.perf_counter() - self.start_time)
        return self.iterations / elapsed_time