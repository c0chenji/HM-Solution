from pathlib import Path
# home = str(Path.home())
from django.conf import settings
from PIL import Image, ImageDraw, ImageFont
from random import choice
import numpy as np  
import webcolors
import time
import math
import os
import sys
import cv2
import uuid
import datetime
from pathlib import Path
# home = str(Path.home())


#colorname_to_rgb = {"red": (220, 20, 60), "green": (0, 128, 0), "blue": (0, 0, 255), "yellow": (255, 255, 0), "purple": (128, 128, 0), "orange": (255, 165, 0), "black": (0, 0, 0), "white": (255, 255, 255), "gray": (128, 128, 128), "brown": (165, 42, 42), "pink": (255, 192, 203), "lime": (0, 255, 0), "navy": (0, 0, 128), "beige": (245, 245, 220), "maroon": (128, 0, 0)}
colorname_to_rgb = {"red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 0, 255), "yellow": (255, 255, 0), "purple": (255, 0, 255), "cyan": (0, 255, 255), "black": (-16, -16, -16), "white": (255, 255, 255)}
color_to_opposite = {"red": "cyan", "green": "purple", "blue": "yellow", "yellow": "blue", "purple": "green", "cyan": "red", "black": "white", "white": "black"}                                
        
class ForensicColor():
    #def __init__(self, execution_path=os.getcwd(), speed="faster", person=True, car=False, bicycle=False, motorcycle=False, bus=False, truck=False):
    #def __init__(self, execution_path=os.getcwd(), speed="faster", person=True):#, car=False, bicycle=False, motorcycle=False, bus=False, truck=False):
    def __init__(self, execution_path=os.getcwd(), speed="faster", person=True):
        
        stime1=datetime.datetime.now()
        # 1. Load the nerual net
        #self.execution_path = execution_path+"/FaceRec/"
        self.execution_path = home+"/FacialStats/FaceRec/"
        self.fc_detector = ObjectDetection()
        self.fc_detector.setModelTypeAsRetinaNet()
        self.fc_detector.setModelPath(os.path.join(self.execution_path, "resnet50_coco_best_v2.0.1.h5"))
        # 2. Choose between "faster" and "fastest"
        self.fc_detector.loadModel(speed)
        # 3. Retrieve a list of custom objects (Person, Car, Bicycle, Motorcycle, Bus, Truck)
        #--self.custom_objects = self.detector.CustomObjects(person, car, bicycle, motorcycle, bus, truck)
        self.custom_objects = self.fc_detector.CustomObjects(person)   #--Only Person Detction--#
        self.index = 0
        
        print("ForensicColor detector LOADED")
        etime1=datetime.datetime.now()
        t_seconds1 = abs((etime1-stime1).total_seconds())
        print("in ForensicColor init t_seconds: "+str(t_seconds1))        

    #--def process(self, fileName):
    def process(self, image, detection_threshold):
        
        #print("in ForensicColorSimple process")
        #print("self.execution_path : "+self.execution_path)
        
        # 4. Detect a list of custom objects from the image based on the model and save an output image
        #--detections = self.detector.detectCustomObjectsFromImage(custom_objects=self.custom_objects, input_image=os.path.join(self.execution_path , fileName), minimum_percentage_probability=70)
        detections = self.fc_detector.detectCustomObjectsFromImage(custom_objects=self.custom_objects, input_image=image, input_type="array", minimum_percentage_probability=detection_threshold, thread_safe=True)
      
        #--return pic
        return detections               

# A class for the color detection for use in Forensic Search
class ForensicColorFrame():
    # Initialize the class based on a given filename or open image
    def __init__(self, f):
        # Get an image
        self.f = None
        self.pic = None
        if type(f) is str:
            self.filename = f
            self.pic = Image.open(f).convert('RGB')
        else:
            #--with PIL--#
            #--self.pic = f.convert('RGB')
            #--with CV2--#
            self.pic = cv2.cvtColor(f, cv2.COLOR_BGR2RGB)
            self.pic = Image.fromarray(self.pic)
            self.pixels = self.pic.load()
            self.base = self.pic.convert('RGBA')
            # Get a font
            # self.fnt = ImageFont.truetype(home+'/FacialStats/fmEnv/lib/python3.5/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSans-Bold.ttf', int(self.pic.size[1]*1/40))
            self.fnt = ImageFont.truetype(settings.INTERFACE_ROOT+'/utils/DejaVu_Sans/DejaVuSans-Bold.ttf', int(self.pic.size[1]*1/40))

            # Make a blank image for the text, initialized to transparent text color
            self.txt = Image.new('RGBA', self.base.size, (255,255,255,0))
            # Get a drawing context
            self.d = ImageDraw.Draw(self.txt)
            self.topList = []
            self.botList = []
            self.carList = []
            self.bicycleList = []
            self.motorcycleList = []
            self.busList = []
            self.truckList = []

    # Find the closest color to the given color of format (R, G, B)
    @staticmethod
    def closest_color(requested_color):
        min_dist = math.sqrt(255 ** 2 * 3)
        ret_name = "black"
        for name, rgb in colorname_to_rgb.items():
            rd = (rgb[0] - requested_color[0]) ** 2
            gd = (rgb[1] - requested_color[1]) ** 2
            bd = (rgb[2] - requested_color[2]) ** 2
            dist = math.sqrt(rd + gd + bd)
            if min_dist > dist:
                min_dist = dist
                ret_name = name
        return ret_name

    # Get the color based on the bounding box, taking a given sample percentage of the box
    def get_color_in_box(self, top_left_x, top_left_y, bottom_right_x, bottom_right_y, percentage, width, height):
        try:
            
            total_red = float(0)
            total_green = float(0)
            total_blue = float(0)

            x_dim = bottom_right_x - top_left_x
            y_dim = bottom_right_y - top_left_y
            total = int(x_dim * y_dim * percentage) 
            x_range = range(top_left_x, bottom_right_x)
            y_range = range(top_left_y, bottom_right_y)

            color_to_count = {"red": 0, "green": 0, "blue": 0, "yellow": 0, "purple": 0, "cyan": 0, "black": 0, "white": 0}

            for i in range(0, total):
                x = choice(x_range)
                y = choice(y_range)
                
                if x < 1:
                    x = 1
                elif x > (int(width)-1):
                    x=int(width)-1
                    
                if y < 1:
                    y = 1
                elif y > (int(height)-1):
                    y=int(height)-1
                                        
                #print("color x: "+str(x))
                #print("color y: "+str(y))
                red, green, blue = self.pixels[x, y]
                color_to_count[ForensicColorFrame.closest_color((red, green, blue))] += 1
                if total_red > sys.float_info.max - red:
                    raise OverflowError("Too many red pixels!")
                else:
                    total_red += red
                if total_green > sys.float_info.max - green:
                    raise OverflowError("Too many green pixels!")
                else:
                    total_green += green
                if total_blue > sys.float_info.max - blue:
                    raise OverflowError("Too many blue pixels!")
                else:
                    total_blue += blue
            avg_red = int(total_red/total)
            avg_green = int(total_green/total)
            avg_blue = int(total_blue/total)
            # Return a list of decreasing percentages of commonality of colors
            counts = []
            colors = []
            # Insertion sort is used here because on this small set, it is just as fast as more efficient searches
            for color, count in color_to_count.items():
                i = 0
                while i < len(counts) and counts[i] > count:
                    i += 1
                counts.insert(i, count)
                colors.insert(i, color)
            return ForensicColorFrame.closest_color((avg_red, avg_green, avg_blue)), colors, counts, total       
        except Exception as e:
            print(e)
            print("Exception: in ForensicColorSimple get_color_in_box")
	
