'''

RL.py

ReinforcementLearning: use OpenCV for lane following initially to gather
training data. Start slowly, determin circuit, and incrementally improve 
speed and paths. Use RI to improve from there.

'''




import os
import numpy as np

import donkeycar as dk
# from donkeycar.parts.RLOpenCV import HoughBundler, LaneLines
from donkeycar.parts.RLControlPi import ControlPi


class RLPilot():

    def load(self, model_path):
        pass

    def shutdown(self):
        pass

    def train(self, train_gen, val_gen,
              saved_model_path, epochs=100, steps=100, train_split=0.8,
              verbose=1, min_delta=.0005, patience=5, use_early_stop=True):
        pass


class RL(RLPilot):
    def __init__(self, model=None, *args, **kwargs):
        super(RL, self).__init__(*args, **kwargs)
        global steering, throttle, steering_hist, throttle_hist, speed, angle
        global CPi

        self.speed = 0.0
        self.angle = 0.0
        self.steering = 0.0
        self.throttle = 0.0
        # self.top_speed=4.0
        self.top_speed=1.0
        self.top_speed=0.1
        self.steering_hist = []
        self.throttle_hist = []
        print("RL init")
        CPi = ControlPi()

    def run(self, img):
        global CPi
        return CPi.run(img)

        '''
        global steering, throttle, steering_hist, throttle_hist, speed, angle, conf

        MODE_COMPLEX_LANE_FOLLOW = 0 # complex lane follower
        MODE_SIMPLE_LINE_FOLLOW = 1 # simple line follower with complex lane follower fall-back
        mode = MODE_SIMPLE_LINE_FOLLOW 

        ll = LaneLines()
        simplecl, lines, roi = ll.process_img(img)
        if mode == MODE_COMPLEX_LANE_FOLLOW and lines is not None and len(lines) > 0 and roi is not None:
          steering, throttle = ll.lrclines(lines,roi)
        elif mode == MODE_SIMPLE_LINE_FOLLOW:
          # although slower, let's see what happens when we
          # now run complex lrclines to gather global history, extra info 
          complexsteering = 0
          complexthrottle = 0
          # if simplecl is None and lines is not None and roi is not None:
          if lines is not None and roi is not None:
            # discard steering and throttle
            complexsteering, complexthrottle = ll.lrclines(lines,roi)
          if simplecl is not None:
            pos = 4
            conf = 10
            conf, steering, throttle = ll.setSteerThrottle(pos, None, simplecl, None, conf)
          elif complexthrottle > 0:
            # fall back to complex lane following
            steering = complexsteering 
            throttle = complexthrottle
          else:
            steering = 0
            throttle = 0
        else:
          steering = 0
          throttle = 0
        print("STEER %f THROT %f" % (steering, throttle))
        return steering, throttle 

        '''