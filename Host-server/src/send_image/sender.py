import cv2
import pickle
import socket
import time
import struct
import numpy as np


class Streamer():
    def __init__(self, host, port) -> None:
        self.vs = cv2.VideoCapture(0)
        self.host = host
        self.port = port
        self.frame = np.zeros((480,480,3))

    def stream(self):
        while 1:
            cap, fr = self.vs.read()
            self.frame = cv2.resize(fr, (480,480))
            time.sleep(0.05)

