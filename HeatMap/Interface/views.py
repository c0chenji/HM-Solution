from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.loader import render_to_string
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic.edit import ModelFormMixin
from django.urls import reverse_lazy
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext as _
from django.views.decorators import gzip
from django.http import HttpResponse, StreamingHttpResponse
from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory
from django.utils.translation import ugettext_lazy as _
from PIL import Image, ImageDraw
from shapely.geometry import Point, Polygon, box
from .forms import (ZoneEdit,
                    ListForm,
                    ChannelEditForm,
                    ChannelCreateForm,
                    ChannelUSBForm,
                    USBchannelEditForm,
                    CameraForm)
from .models import *
from django.contrib.auth.hashers import check_password
from threading import Thread
from collections import OrderedDict
from scipy.spatial import distance as dist
from imutils import paths
import imutils
import numpy as np
import os
import cv2
import threading
import time
import datetime
import json
import sys
import queue
import celery
import uuid
import dlib
# =====================================
from Interface.utils.trackableobject import *
from Interface.utils.centroidtracker import *
from Interface.utils.body import *
from Interface.utils.ColorRec import ForensicColorFrame
# ============================================================================

HEATMAP_MAX_DISAPPEARED = 5
COLOR_PALLETE = {"BLUE": (255, 0, 0), "TEAL": (255, 255, 0), "RED": (0, 0, 255),
                 "GREEN": (0, 255, 0), "YELLOW": (0, 255, 255), "PINK": (255, 110, 199), "DEFAULT": (0, 0, 0), "ORANGE": (34, 87, 255)}
global stop
stop = False
global stablize

lock = threading.Lock()
q = queue.Queue()

#Adjust cooridnates based on the scale between frame and canvas of frontend
def applyScale(a,x_scale,y_scale):
    b = a
    if(len(b)>0):
        for i in range(len(b)):
            b[i][0]= int(b[i][0]*x_scale)
            b[i][1]= int(b[i][1]*y_scale)
    return b

def applyDirectionScale(a,x_scale,y_scale):
    b = a
    if(len(b)>0):
        for j in range(len(b)):
            for item in b[j]:
                item[0] = int(item[0]*x_scale)
                item[1] = int(item[1]*y_scale)
    return b

def tuplefyItem(arrayOfArrays):
    return [tuple(item) for item in arrayOfArrays]

def genDirectDict(directions):
    direct_dict ={}
    total = len(directions)
    for item in directions:
        if item.direction in direct_dict:
            direct_dict[item.direction]+=1
        else:
            direct_dict[item.direction]=0
    for i in direct_dict:
        direct_dict[i]=direct_dict[i]/total
    return direct_dict


# Return list of start points rectangle
# startPoints of direction:origin==0
# endPoints of direction: origin ==1
def map_poly_directs(polygons, directions):
    result = {}
    zone = 0
    currentZone =0
    for poly in polygons:
        targetZone = Polygon(tuplefyItem(poly["points"]))
        for targeDirection in directions:
            targetPoint= Point(targeDirection[1])
            if(targetPoint.within(targetZone)):
                currentZone= zone
                result[currentZone]=targeDirection
        zone+=1

    return result



def genRect(directions, origin,width,height):
    # get all points into x , y list
    x = [point[origin][0] for point in directions]
    y = [point[origin][1] for point in directions]

    # take max and min values of x, y to construct
    # left-top, right-top, right-bottom, left-bottom coordinates
    minX, maxX, minY, maxY = min(x), max(x), min(y), max(y)
    minX = (minX-50, 0)[minX-50 < 0]
    maxX = (maxX+50, 700)[maxX+50 > width]
    minY = (minY-50, 0)[minY-50 < 0]
    maxY = (maxY+50, 500)[maxY+50 > height]

    leftTop = (minX, minY)
    rightTop = (maxX, minY)
    rightBottom = (maxX, maxY)
    leftBottom = (minX, maxY)
    return [leftTop, rightTop, rightBottom, leftBottom]

# Get direction'end points by direction 
def genEndPoints(directions):
    result = [tuple(point[1]) for point in directions]
    return result

# Return specific direction by entering the input of its end point
def getDirectionsByEnds(directions, endPoint):
    if direction and endpoint:
        for points in directions:
            if(points[1] == endPoint):
                return points

def distMap(frame1, frame2):
	"""outputs pythagorean distance between two frames"""
	frame1_32 = np.float32(frame1)
	frame2_32 = np.float32(frame2)
	diff32 = frame1_32 - frame2_32
	norm32 = np.sqrt(diff32[:,:,0]**2 + diff32[:,:,1]**2 + diff32[:,:,2]**2)/np.sqrt(255**2 + 255**2 + 255**2)
	dist = np.uint8(norm32*255)
	return dist

def saveDirection(id, link):

    target_dir = settings.MEDIA_ROOT + "/images/"+str(id)+"/"
    if (not os.path.isdir(target_dir)):
        os.makedirs(target_dir)
    # get default channel to save specific frame and heatmap
    defaultChannel = id
    # access global value stop to conrol thread if required
    global stop
    frame_counter = 0
    firstFrame = None
    ct = CentroidTracker(HEATMAP_MAX_DISAPPEARED)
    trackableObjects = {}
    trackers = []
    vid = cv2.VideoCapture(link)
    # define frame_height and frame_width
    # print("the video size is{} {}".format(width, height))
    
    # width 1280
    width= vid.get(3)
    # height 960
    height = vid.get(4) 
    x_scale = 700/width
    y_scale = 500/height 
    #load polygon coordinates data to array
    p = json.loads(Channel.objects.get(id=defaultChannel).coordinates)
    #load direction coordinates
    d = json.loads(Channel.objects.get(id=defaultChannel).directions)
    # generate dictionay contains zone index mapped to specific direction coorinates
    zone_direct_dictionary = map_poly_directs(p,d)
    #load polygon coordinates data to array
    targetPolygons = json.loads(Channel.objects.get(id=defaultChannel).coordinates)
    #load direction coordinates
    directions = json.loads(Channel.objects.get(id=defaultChannel).directions)
    # generate dictionay contains zone index mapped to specific direction coorinates

    print(str(zone_direct_dictionary))
    print("the original directions are------ "+str(directions))
    print("the startRect before adjustment---- "+str(genRect(directions,0,700,500)))
    #convert directions coordinates by applying actual scale on live streaming
    adjustedDirection = applyDirectionScale(directions,width/700,height/500)
    # generate targetStartRectangel
    # output -- [x0, x1,y1,y0]
    
    print("the adjust---- directions are---- "+str(adjustedDirection))
    print("the startGen after adj---- "+str(genRect(adjustedDirection,0,width,height)))
    # print("startRect before"+str(genRect(directions,0,700,500)))


    startRect = genRect(adjustedDirection, 0,width,height)
    # print("startRect after applying scale" + str(startRect))
    endRect = genRect(adjustedDirection, 1,width, height)
    xStartPoint,xEndPoint, yStartPoint, yEndPoint = startRect[0][0],startRect[1][0],startRect[3][0],startRect[2][1]
    
    

    
    #convert targetPolygon to the scale of detecting streaming
    adjustedTargetPolygons=targetPolygons
    for item in adjustedTargetPolygons:
        item["points"]=applyScale(item["points"],width/700,height/500)
    
    
    
    print("zone_direct_dictionary"+str(zone_direct_dictionary))
    
    while (not stop):
        ret, frame = vid.read()
        # initialize frame counter and firstFrame
        if ret == True:
            frame_counter += 1
            fresh_copy = frame.copy()
            fresh_copy2= frame.copy()
            recogFrame = frame.copy()
            frame_height = frame.shape[0]
            frame_width = frame.shape[1]
            
            if firstFrame is None:
                firstFrame = recogFrame
                frame1 = recogFrame
                frame2 = recogFrame  
                
            rows, cols, _ = np.shape(recogFrame)
            dist = distMap(frame1, recogFrame)
            frame1 = frame2
            frame2 = recogFrame                    
            
            rgb = cv2.cvtColor(recogFrame, cv2.COLOR_BGR2RGB)
            mod = cv2.GaussianBlur(dist, (9,9), 0)
            # apply thresholding
            #_, thresh = cv2.threshold(mod, 100, 255, 0)
            _, thresh = cv2.threshold(mod, 25, 255, 0)
            # calculate st dev test
            _, stDev = cv2.meanStdDev(mod)
            
            
            rects = []
            if frame_counter % 15 == 0:    
                if stDev > 2:
                    trackers = []
                    thresh = cv2.dilate(thresh, None, iterations=2)
                    cnts = cv2.findContours(
                        thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                    cnts = imutils.grab_contours(cnts)
                    # loop over the contours
                    print("------------------cnts length------------------------  "+str(len(cnts)))
                    for c in cnts:
                        # Check Contour location
                        (xPoint, yPoint, wPoint, hPoint) = cv2.boundingRect(c)
                        yCenter = int((yPoint + (yPoint+hPoint)) / 2.0)
                        # if yCenter < int(round(H // 8)) or yCenter > int(round(H // 1.2)):
                        if yCenter < int(round(hPoint // 8)) or yCenter > int(round(hPoint // 1.2)):
                            # 100:
                            if cv2.contourArea(c) < 300 or cv2.contourArea(c) > 20000:
                                continue
                        else:
                            if cv2.contourArea(c) < 3000 or cv2.contourArea(c) > 20000:
                                continue
                                
                        (x, y, w, h) = cv2.boundingRect(c)
                        
                        xCenter = int((x+(x+w))/2.0 )
                        yCenter = int((y+(y+h))/2.0 )

                        startCheckPoint = False
                        objStartPoint = Point(xCenter, yCenter)
                        
                        #change xstartpoints, y start point, xstarpoint+w == x2, ystartpoint+h== y2

                        # startPoints = np.array([(xStartPoint,yStartPoint),(xStartPoint+wStartPoint,yStartPoint), (xStartPoint+wStartPoint,yStartPoint+hStartPoint), (xStartPoint,yStartPoint+hStartPoint)], dtype=np.int32)  
                        startPoints = np.array([(xStartPoint,yStartPoint),(xEndPoint,yStartPoint), (xEndPoint,yEndPoint), (xStartPoint,yEndPoint)], dtype=np.int32) 
                        print("startpoints rect(applied scale) is ________"+str(startPoints))
                        startPoly = Polygon(startPoints)
                        startCheckPoint = objStartPoint.within(startPoly)
                        print("CHECKING______________RESULT____"+str(startCheckPoint))
                        tracker = dlib.correlation_tracker()
                        rect = dlib.rectangle(x, y, x+w, y+h)
                        tracker.start_track(rgb, rect)
                        
                        trackers.append([tracker, 0, startCheckPoint, defaultChannel])
            else:
                print("frame_counter ", frame_counter)
                print("TRACKING OBJECTS, Length: "+str(len(trackers)))
                # loop over the trackers
                for tracker in trackers:
                    # set the status of our system to be 'tracking' rather
                    # than 'waiting' or 'detecting'
                    status = "Tracking"

                    # update the tracker and grab the updated position
                    tracker[0].update(rgb)
                    pos = tracker[0].get_position()

                    # unpack the position object
                    startX = int(pos.left())
                    startY = int(pos.top())
                    endX = int(pos.right())
                    endY = int(pos.bottom())
                    dwellZone = tracker[1]
                    cntType = tracker[2]
                    ch_id = tracker[3]
                    # add the bounding box coordinates to the rectangles list
                    rects.append((startX, startY, endX, endY, dwellZone, cntType, ch_id))

            objects = ct.update(rects)
            for (objectID, centroid) in list(objects.items()):
                # check to see if a trackable object exists for the current
                # object ID
                to = trackableObjects.get(objectID, None)
                counted = False

                # if there is no existing trackable object, create one
                if to is None:
                    print("TRACKER NOT FOUND")
                    initStartTime = datetime.datetime.now()
                    alertStartTime = datetime.datetime.now()

                    x0 = centroid[2]
                    y0 = centroid[3]
                    x1 = centroid[4]
                    y1 = centroid[5]
                    # find object x 0+ x1 center
                    w = centroid[4] - centroid[2]
                    h = centroid[5] - centroid[3]
                    probability = centroid[6]
                    alertNumber = 0
                    
                    if ct.disappeared[objectID] == 0:
                        pic = ForensicColorFrame(fresh_copy)
                        height_unit = int((y1 - y0)/14)
                        width_unit = int((x1 - x0)/5)
                        
                        # --TOP
                        top_avg_color_name, top_colors, top_counts, top_count = pic.get_color_in_box(x0+width_unit, y0+height_unit*3, x1-width_unit, y0+height_unit*7, float(10/100), int(frame_width), int(frame_height))
                        # --BOTTOM
                        bot_avg_color_name, bot_colors, bot_counts, bot_count = pic.get_color_in_box(x0+width_unit, y0+height_unit*10, x1-width_unit, y0+height_unit*12, float(10/100), int(frame_width), int(frame_height))

                        topBox = [x0, y0+height_unit*2, x1, y0+height_unit*8]
                        botBox = [x0, y0+height_unit*8, x1, y1-height_unit]
                        
                        body_id = 0
                        to = TrackableObject(
                            objectID, centroid, counted, initStartTime, body_id, alertNumber, alertStartTime,defaultChannel)

                else:
                    # if not to.counted:
                    print("TRACKER FOUND")
                    print("objectID: "+str(objectID))
                    to.centroids.append(centroid)

                    x0 = centroid[2]
                    y0 = centroid[3]
                    x1 = centroid[4]
                    y1 = centroid[5]
                    w = centroid[4] - centroid[2]
                    h = centroid[5] - centroid[3]
                    dwellZone = centroid[6]
                    startPointObj = centroid[7]
                    
                    if not to.counted:
                        if startPointObj and ct.disappeared[objectID] == HEATMAP_MAX_DISAPPEARED:
                            #generate object center
                            xCenter = int((x0+x0+w)/2)
                            yCenter = int((y0+y0+h)/2)
                            zone = 0
                            currentZone = 0
                            for target in adjustedTargetPolygons:
                                targetZone = tuplefyItem(target["points"])
                                point1 = Point(xCenter, yCenter)  # center of object
                                poly = Polygon(targetZone)
                                checkPoint = point1.within(poly)
                                if checkPoint == True:
                                    index = targetPolygons.index(target)
                                    currentZone = zone
                                    break
                                zone += 1
                            # InsertObject
                            pic = ForensicColorFrame(fresh_copy)
                            height_unit = int((y1 - y0)/14)
                            width_unit = int((x1 - x0)/5)
                        
                            # --TOP
                            top_avg_color_name, top_colors, top_counts, top_count = pic.get_color_in_box(x0+width_unit, y0+height_unit*3, x1-width_unit, y0+height_unit*7, float(10/100), int(frame_width), int(frame_height))
                            # --BOTTOM
                            bot_avg_color_name, bot_colors, bot_counts, bot_count = pic.get_color_in_box(x0+width_unit, y0+height_unit*10, x1-width_unit, y0+height_unit*12, float(10/100), int(frame_width), int(frame_height))
                            frameName = str(uuid.uuid4()) + '.jpg'
                            #check center x y is within which zone area and get specifiic direction
                            requiredDirection= zone_direct_dictionary[currentZone]
                            directionIndex = d.index(requiredDirection)
                            # for coord in requiredDirection:
                            #     coord[0]=int(coord*x_scale)
                            #     coodr[1]=int(coord*y_scale)
                            # save heatmap frame
                            newFrame = Frame(channel_id=defaultChannel, img_name=frameName, captureTime=datetime.datetime.now())
                            newFrame.save()
                            print("________________________________saving______________________frames")
                            #Save to Direction Table
                            #direction table = Direction().......
                            print("________________________________saving______________________directions")
                            tempDirectionObject = Direction(frame_id=newFrame.id,
                                                        topLeftX=int(x*x_scale),
                                                        topLeftY=int(y*y_scale),
                                                        width=int(w*x_scale),
                                                        height=int(h*y_scale),
                                                        direction=str(directionIndex),
                                                        topColor=str(top_avg_color_name),
                                                        bottomColor=str(bot_avg_color_name))
                            tempDirectionObject.save()
                            to.counted = True

                # store the trackable object in our dictionary
                trackableObjects[objectID] = to
                cv2.rectangle(
                    frame, (centroid[2], centroid[3]), (centroid[4], centroid[5]), COLOR_PALLETE["TEAL"], 2)


def saveFrame(id, link):
    # detectionSampleFile = settings.MEDIA_ROOT + "/carDetectionSample/cars.xml"
    # car_cascade = cv2.CascadeClassifier(detectionSampleFile)
    target_dir = settings.MEDIA_ROOT + "/images/"+str(id)+"/"
    if (not os.path.isdir(target_dir)):
        os.makedirs(target_dir)
    print("current channel is "+str(id))
    # get default channel to save specific frame and heatmap
    defaultChannel = id
    defaultTopColor = "gray"
    defaultBottomColor = "red"
    defaultDwellingTime = 100
    targetPolygons = json.loads(
        Channel.objects.get(id=defaultChannel).coordinates)
    adjustedTargetPolygons=targetPolygons

    global stop
    frame_counter = 0
    firstFrame = None
    ct = CentroidTracker(HEATMAP_MAX_DISAPPEARED)
    trackableObjects = {}
    trackers = []
    vid = cv2.VideoCapture(link)
    # width 1280
    width= vid.get(3)
    # height 960
    height = vid.get(4) 
    x_scale = 700/width
    y_scale = 500/height
    for item in adjustedTargetPolygons:
        item["points"]=applyScale(item["points"],width/700,height/500)
    print("adjustedTarget zone is "+str(adjustedTargetPolygons))

    while (not stop):
        ret, frame = vid.read()
        # initialize frame counter and firstFrame
        if ret == True:
            frame_counter += 1
            fresh_copy = frame.copy()
            fresh_copy2= frame.copy()
            recogFrame = frame.copy()
            frame_height = frame.shape[0]
            frame_width = frame.shape[1]

            # convert to gray scale of each frames
            mask = np.zeros((frame_height, frame_width), dtype=np.uint8)
            for target in adjustedTargetPolygons:
                index = targetPolygons.index(target)
                # print(targetZone)
                targetZone = tuplefyItem(target["points"])
                # print(targetZone)
                cv2.drawContours(frame,np.array([targetZone]),-1,(255,0,0),2)
                cv2.fillPoly(mask, np.array([targetZone]), (255))
                

            resChannel = cv2.bitwise_and(fresh_copy2,fresh_copy2,mask = mask)
            bgChannel = np.ones_like(resChannel, np.uint8)*255
            cv2.bitwise_not(bgChannel,bgChannel, mask=mask)
            dstChannel = bgChannel+ resChannel
            recogFrame = dstChannel
            
            rgb = cv2.cvtColor(recogFrame, cv2.COLOR_BGR2RGB)
            imgName =target_dir+"recordFrame.jpg"
            cv2.imwrite(imgName,recogFrame)
            gray = cv2.cvtColor(recogFrame, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (21, 21), 0)
            # Initialize the first frame
            if firstFrame is None:
                origImg = fresh_copy
                mask = np.zeros((frame_height, frame_width), dtype=np.uint8)
                for target in adjustedTargetPolygons:
                    
                    targetZone = tuplefyItem(target["points"])
                    cv2.fillPoly(mask, np.array([targetZone]), (255))

                resOrig = cv2.bitwise_and(origImg, origImg, mask=mask)
                bgOrig = np.ones_like(resOrig, np.uint8)*255
                cv2.bitwise_not(bgOrig, bgOrig, mask=mask)
                dstOrig = bgOrig + resOrig
                grayOrig = cv2.cvtColor(dstOrig, cv2.COLOR_BGR2GRAY)
                grayOrig = cv2.GaussianBlur(grayOrig, (21, 21), 0)
                firstFrame = grayOrig
                
                # Saving the first frame for test purposes
                frameName = str(uuid.uuid4())+".jpg"
                dirName = target_dir+frameName
                cv2.imwrite(dirName,firstFrame)
                # cv2.imwrite(dirName+"_frame.jpg",frame)
                #Update current image on heatmap
                desciption = Channel.objects.get(id=defaultChannel).description
                print("description is "+str(desciption))
                imgName =target_dir+desciption+".jpg"
                cv2.imwrite(imgName,fresh_copy)
                continue

            frameDelta = cv2.absdiff(firstFrame, gray)
            thresh = cv2.threshold(frameDelta, 35, 255, cv2.THRESH_BINARY)[1]
            # Object detection every 30th frame
            rects = []
            if frame_counter % 30 == 0:     
                trackers = []
                thresh = cv2.dilate(thresh, None, iterations=2)
                cnts = cv2.findContours(
                    thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                cnts = imutils.grab_contours(cnts)
                # loop over the contours
                print("------------------cnts length------------------------  "+str(len(cnts)))
                for c in cnts:
                    # Check Contour location
                    (xPoint, yPoint, wPoint, hPoint) = cv2.boundingRect(c)
                    yCenter = int((yPoint + (yPoint+hPoint)) / 2.0)
                    # if yCenter < int(round(H // 8)) or yCenter > int(round(H // 1.2)):
                    if yCenter < int(round(hPoint // 8)) or yCenter > int(round(hPoint // 1.2)):
                        # 100:
                        if cv2.contourArea(c) < 600 or cv2.contourArea(c) > 20000:
                            continue
                    else:
                        if cv2.contourArea(c) < 3000 or cv2.contourArea(c) > 20000:
                            continue
                            
                    (x, y, w, h) = cv2.boundingRect(c)
                    
                    xCenter = int((x+(x+w))/2.0 )
                    yCenter = int((y+(y+h))/2.0 )
                    
                    zone = 0
                    currentZone = 0
                    for target in adjustedTargetPolygons:
                        targetZone = tuplefyItem(target["points"])
                        point1 = Point(xCenter, yCenter)  # center of object
                        poly = Polygon(targetZone)
                        checkPoint = point1.within(poly)
                        if checkPoint == True:
                            index = targetPolygons.index(target)
                            currentZone = zone
                            break
                        zone += 1
                    # if currentZone == 0:
                    #     currentZone = zone-1

                    tracker = dlib.correlation_tracker()
                    rect = dlib.rectangle(x, y, x+w, y+h)
                    tracker.start_track(rgb, rect)
                    trackers.append([tracker, currentZone, 0, defaultChannel])
            else:

                print("frame_counter ", frame_counter)
                print("TRACKING OBJECTS, Length: "+str(len(trackers)))
                # loop over the trackers
                for tracker in trackers:
                    # set the status of our system to be 'tracking' rather
                    # than 'waiting' or 'detecting'
                    status = "Tracking"

                    # update the tracker and grab the updated position
                    tracker[0].update(rgb)
                    pos = tracker[0].get_position()

                    # unpack the position object
                    startX = int(pos.left())
                    startY = int(pos.top())
                    endX = int(pos.right())
                    endY = int(pos.bottom())
                    dwellZone = tracker[1]
                    cntType = tracker[2]
                    ch_id = tracker[3]
                    # add the bounding box coordinates to the rectangles list
                    rects.append((startX, startY, endX, endY, dwellZone, cntType, ch_id))

            objects = ct.update(rects)
            for (objectID, centroid) in list(objects.items()):
                # check to see if a trackable object exists for the current
                # object ID
                to = trackableObjects.get(objectID, None)
                counted = False

                # if there is no existing trackable object, create one
                if to is None:
                    print("TRACKER NOT FOUND")
                    initStartTime = datetime.datetime.now()
                    alertStartTime = datetime.datetime.now()

                    x0 = centroid[2]
                    y0 = centroid[3]
                    x1 = centroid[4]
                    y1 = centroid[5]
                    w = centroid[4] - centroid[2]
                    h = centroid[5] - centroid[3]
                    probability = centroid[6]
                    alertNumber = 0

                    if ct.disappeared[objectID] == 0:
                        pic = ForensicColorFrame(fresh_copy)
                        height_unit = int((y1 - y0)/14)
                        width_unit = int((x1 - x0)/5)

                        # --TOP
                        top_avg_color_name, top_colors, top_counts, top_count = pic.get_color_in_box(x0+width_unit, y0+height_unit*3, x1-width_unit, y0+height_unit*7, float(10/100), int(frame_width), int(frame_height))
                        # --BOTTOM
                        bot_avg_color_name, bot_colors, bot_counts, bot_count = pic.get_color_in_box(x0+width_unit, y0+height_unit*10, x1-width_unit, y0+height_unit*12, float(10/100), int(frame_width), int(frame_height))

                        topBox = [x0, y0+height_unit*2, x1, y0+height_unit*8]
                        botBox = [x0, y0+height_unit*8, x1, y1-height_unit]  
                        body_id = 0
                        to = TrackableObject(
                            objectID, centroid, counted, initStartTime, body_id, alertNumber, alertStartTime,defaultChannel)

                else:
                    # if not to.counted:
                    print("TRACKER FOUND")
                    print("objectID: "+str(objectID))
                    to.centroids.append(centroid)

                    x0 = centroid[2]
                    y0 = centroid[3]
                    x1 = centroid[4]
                    y1 = centroid[5]
                    w = centroid[4] - centroid[2]
                    h = centroid[5] - centroid[3]
                    dwellZone = centroid[6]

                    if not to.counted:
                        endDwellingTime = datetime.datetime.now()
                        dwellingTime = abs(
                            (endDwellingTime-to.startTime).total_seconds())

                        if ct.disappeared[objectID] == 5:
                            if dwellingTime >= 2:
                                to.counted = True
                                x0 = centroid[2]
                                y0 = centroid[3]
                                x1 = centroid[4]
                                y1 = centroid[5]
                                w = centroid[4] - centroid[2]
                                h = centroid[5] - centroid[3]
                                dwellZone = centroid[6]
                                pic = ForensicColorFrame(fresh_copy)
                                height_unit = int((y1 - y0)/14)
                                width_unit = int((x1 - x0)/5)

                                # --TOP
                                top_avg_color_name, top_colors, top_counts, top_count = pic.get_color_in_box(x0+width_unit, y0+height_unit*3, x1-width_unit, y0+height_unit*7, float(10/100), int(frame_width), int(frame_height))
                                # --BOTTOM
                                bot_avg_color_name, bot_colors, bot_counts, bot_count = pic.get_color_in_box(x0+width_unit, y0+height_unit*10, x1-width_unit, y0+height_unit*12, float(10/100), int(frame_width), int(frame_height))
                                # InsertHeatmap
                                # save heatmap frame
                                newFrame = Frame(channel_id=defaultChannel, img_name=frameName, captureTime=datetime.datetime.now())
                                newFrame.save()
                                print("first original x0, y0 " +str(x0)+" "+str(y0))
                                tempHeatMapObject = Heatmap(frame_id=newFrame.id,
                                                            topLeftX=int(x0*x_scale),
                                                            topLeftY=int(y0*y_scale),
                                                            width=int(w*x_scale),
                                                            height=int(h*y_scale),
                                                            dwellingTime=dwellingTime,
                                                            zoneArea=int(
                                                                dwellZone),
                                                            topColor=str(top_avg_color_name),
                                                            bottomColor=str(bot_avg_color_name))
                                tempHeatMapObject.save()
                                ct.deregister(objectID)

                        if not to.counted:
                            if dwellingTime >= 2 and ct.disappeared[objectID] == HEATMAP_MAX_DISAPPEARED:
                                # InsertObject
                                pic = ForensicColorFrame(fresh_copy)
                                height_unit = int((y1 - y0)/14)
                                width_unit = int((x1 - x0)/5)

                                # --TOP
                                top_avg_color_name, top_colors, top_counts, top_count = pic.get_color_in_box(x0+width_unit, y0+height_unit*3, x1-width_unit, y0+height_unit*7, float(10/100), int(frame_width), int(frame_height))
                                # --BOTTOM
                                bot_avg_color_name, bot_colors, bot_counts, bot_count = pic.get_color_in_box(x0+width_unit, y0+height_unit*10, x1-width_unit, y0+height_unit*12, float(10/100), int(frame_width), int(frame_height))
                                frameName = str(uuid.uuid4()) + '.jpg'
                                # heatMap = HeatMap(objectID, to.firstBody_id, dwellingTime, int(dwellZone), 1, body)
                                # save heatmap frame
                                newFrame = Frame(channel_id=defaultChannel, img_name=frameName, captureTime=datetime.datetime.now())
                                newFrame.save()
                                tempHeatMapObject = Heatmap(frame_id=newFrame.id,
                                                            topLeftX=int(x0*x_scale),
                                                            topLeftY=int(y0*y_scale),
                                                            width=int(w*x_scale),
                                                            height=int(h*y_scale),
                                                            dwellingTime=dwellingTime,
                                                            zoneArea=int(
                                                                dwellZone),
                                                            topColor=str(top_avg_color_name),
                                                            bottomColor=str(bot_avg_color_name))
                                tempHeatMapObject.save()
 
                                to.counted = True

                # store the trackable object in our dictionary
                trackableObjects[objectID] = to
                cv2.rectangle(
                    frame, (centroid[2], centroid[3]), (centroid[4], centroid[5]), COLOR_PALLETE["TEAL"], 2)


def change_language(request):
    response = HttpResponseRedirect('/login')
    if request.method == 'POST':
        language = request.POST.get('language')
        if language:
            if language != settings.LANGUAGE_CODE and [lang for lang in settings.LANGUAGES if lang[0] == language]:
                redirect_path = f'/{language}/login'
            elif language == settings.LANGUAGE_CODE:
                redirect_path = '/login'
            else:
                return response
            from django.utils import translation
            translation.activate(language)
            response = HttpResponseRedirect(redirect_path)
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    return response


def Front(request):
    global stablize
    stablize = 20

    return render(request, 'Interface/front.html', {'title': 'Front'})


@login_required
def generel(request):
    # global stop
    # stop = True
    print(timezone.now)
    response = HttpResponseRedirect('/channel')
    # return render(request, 'Interface/generel_Ui.html', {'title': 'GenerelUI'})
    return response

# Create only USB channel
@login_required
def createUSB(request):
    cameras = Camera.objects.all
    if request.method == 'POST':
        print("post request")
        form = ChannelUSBForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Channelcreate = Channel(description=data['description'],
                                    enabled=data['enabled'],
                                    camera=cameras)
            Channelcreate.save()
            print("form save")
            return HttpResponse(render_to_string('Interface/channel_create_success.html'))
        else:
            return render(request, 'Interface/new_USB_channel.html', {'form': form})
    return render(request, 'Interface/new_USB_channel.html')
    #  return render_to_response('Interface/new_channel.html', locals(), context_instance=RequestContext(request))


# for context variables to the other views
def channel(request):
    context = {
        'channels': Channel.objects.prefetch_related('camera'),
    }

# Adding channels
@login_required
def Home(request):
    # stop playing live streaming in case redirecting to other pages

    print(type(settings.INTERFACE_ROOT))
    channels = Channel.objects.all()
    form = ChannelCreateForm(request.POST)
    context = {
        'cameras': Camera.objects.all(),
        'form': form,
        'channels': channels
    }
    # cameras1 = Camera.objects.get(pk=7)
    if request.method == 'POST':
        print("post request")
        print(form.errors)

        if form.is_valid():
            data = form.cleaned_data
            print("form cleaned")
            print("channel create data")
            # form.save()
            form.save()

            target_id = Channel.objects.get(IP=request.POST["IP"]).id
            target_description = request.POST["description"]
            print("target Id is ", target_id)
            print("target description is ",target_description)
            # print("form.description is",form.description.value)
            return HttpResponse(render_to_string('Interface/channel_create_success.html'))
        else:
            return render(request, 'Interface/new_channel.html', context)

    return render(request, 'Interface/new_channel.html', context=context)


class ChannelListView(ListView):
    # global stop
    # stop = True

    model = Channel
    form_class = ListForm
    template_name = 'Interface/channel.html'
    context_object_name = 'channels'

# IP camera channel update


class ChannelUpdateView(UpdateView):
    model = Channel
    fields = ['username', 'password', 'IP', 'portNum', 'cameraNum',
              'description', 'enabled', 'camera']

    success_message = "Channel Updated"
    success_url = reverse_lazy('Interface-channel')
    template_name = 'Interface/channel_edit.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ChannelUpdateView, self).get_context_data(**kwargs)
        context['cameras'] = Camera.objects.all()
        return context

    def form_valid(self, form):

        form.save()

        return HttpResponse(render_to_string('Interface/channel_edit_success.html'))


# UPdates only USB channel
class USBChannelUpdateView(UpdateView):
    model = Channel
    form_class = USBchannelEditForm
    success_message = "Channel Updated"
    success_url = reverse_lazy('Interface-channel')
    template_name = 'Interface/USB_channel_edit.html'

    def get_context_data(self, *args, **kwargs):
        context = super(USBChannelUpdateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.save()
        return HttpResponse(render_to_string('Interface/channel_edit_success.html'))


class ChannelDeleteView(DeleteView):
    model = Channel
    template_name = 'Interface/channel_delete.html'
    context_object_name = 'channels'
    success_url = reverse_lazy('Interface-channel')


@login_required
def ZoneeditData(request):
    return render(request, 'Interface/zoneedit.html', {'title': 'Zoneedit'})


class ZoneUpdateView(UpdateView):
    model = Channel
    fields = ["coordinates", "names", "directions"]
    success_message = "Channel Updated"
    success_url = reverse_lazy('Interface-channel_edit')
    template_name = 'Interface/zone.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ZoneUpdateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        print("form valid")
        form.save()
        return HttpResponse(render_to_string('Interface/channel_edit_success.html'))


@login_required
def heatmap_page(request):
    camera = Camera.objects.all()
    frame = Frame.objects.all()
    channels = Channel.objects.all()
    heatmap = Heatmap.objects.all()
    directions = Direction.objects.all()
    
    print(str(genDirectDict(directions)))
    topResult = set([])
    botResult = set([])
    for item in heatmap:
        topResult.add(item.topColor)
        botResult.add(item.bottomColor)
    # print(sorted(list(topResult)))
    # print(sorted(list(botResult)))

    enabledList = []
    if channels:
        for channel in channels:
            if (channel.enabled == 1):
                enabledList.append(channel)


    
    if(len(enabledList) > 0 and enabledList[0]):
        context = {"defaultChannel": enabledList[0],
                   "channels": enabledList,
                   "heatmap": heatmap,
                   "frame": frame,
                   "camera": camera,
                   "directions":directions,
                   "topColor":sorted(list(topResult)),
                   "botColor":sorted(list(botResult))}
        return render(request, 'Interface/heat_map.html', context=context)
    return HttpResponse("No channel is enabled or created yet.Please click play button after you activate the channel ")


# livesteam feature


class VideoCamera:
    def __init__(self, link):
        # cars "rtsp://174.6.126.86/axis-media/media.amp"
        # mountain "rtsp://207.194.135.17/axis-media/media.amp"
        self.video = cv2.VideoCapture(link)
        if(self.video is None or self.video.isOpened()):
            print("The camera is not working yet--+++++++++++++++++++_____________")
        # (self.grabbed, self.frame) = self.video.read()
        # threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()
        time.sleep(2)
        print("current camera release---------------------------")

    def get_frame(self):
        ret, frame1 = self.video.read()
        ret, frame2 = self.video.read()
        if ret == True:
            # compare two sample frames and do the detection
            diff= cv2.absdiff(frame1,frame2)
            gray =cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray,(5,5),0)
            _, thresh =cv2.threshold(blur,20,255, cv2.THRESH_BINARY)
            dilated =cv2.dilate(thresh,None,iterations=3)
            contours,_ = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

            # draw rectangle on each detected frame
            for contour in contours:
                (x,y,w,h) = cv2.boundingRect(contour)

                if cv2.contourArea(contour)<700:
                    continue
                cv2.rectangle(frame1,(x,y),(x+w,y+h),COLOR_PALLETE["TEAL"],2)
            # encode frame to .jpg format and return bytes result
            ret, jpeg= cv2.imencode('.jpg',frame1)

            return jpeg.tobytes()

def gen(camera):

    # print("The global stop status in gen function is ", stop)

    while (True):
        frame = camera.get_frame()
        camera.__del__
        # time.sleep(2)
        output = b'--frame\r\n'+b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n'
        yield(output)

def displayLiveStream(request):
    channels = Channel.objects.all()
    enabledList = []

    if channels:
        for channel in channels:
            if (channel.enabled == 1):
                enabledList.append(channel)
    if (request.POST.get("channelId")):
        print("Display live stream page request send from template, the channel id you click is",
              request.POST.get("channelId"))
        request.session['tempId'] = request.POST.get("channelId")
        # print("session , temp Id is ", request.session['tempId'])

    if (request.POST.get("pauseChannelId")):
        print("pause ChannelId is", request.POST.get("pauseChannelId"))
        # request.session['tempId'] = request.POST.get("channelId")
        # print("session , temp Id is ", request.session['tempId'])
    global stop
    stop = False

    # print("On displaying live stream page, the stop status is ", stop)
    # t1 = Thread(target=saveFrame)
    # t1.start()
    if(len(enabledList) > 0 and enabledList[0]):
        context = {
            'statue': "display",
            "enabledChannels": enabledList,
            "defaultChannel": enabledList[0]
        }
        return render(request, 'Interface/live_stream/display_live_stream.html', context=context)
    return HttpResponse("No channel is enabled or created yet.")


global threadList
threadList = []
thread_name = []

# @app.task()
@gzip.gzip_page
def liveStream_page(request, id):
    global threadList
    selected_username = Channel.objects.get(id=id).username
    selected_password = Channel.objects.get(id=id).password
    selected_channel_IP = Channel.objects.get(id=id).IP
    selected_channel_portNum = Channel.objects.get(id=id).portNum
    selected_camera_url = Channel.objects.get(id=id).camera.rtsp_url
    # Final version of link
    # link = "rtsp://" + str(selected_username) + str(selected_password) +"@" + str(selected_channel_IP) + str(selected_camera_url)
    link = "http://"+str(selected_channel_IP) + str(selected_camera_url)
    # link = "rtsp://"+str(selected_channel_IP) + str(selected_camera_url)
    print("the link is",link)
    t = threading.Thread(name=str(id), target=saveFrame, args=(id, link))
    # thread of save directionFrame 
    t2 = threading.Thread(target=saveDirection, args=(id, link))
    if str(id) not in thread_name:
        threadList.append(t)
        t.start()
        t2.start()
        thread_name.append(str(id))
        print("Thread ID is " + str(id) + " -------------------")

    # print("You selected channel link is ", link)

    # Beach "http://162.17.212.89:8000/mjpg/video.mjpg"
    # patio http://192.164.155.52:8000/mjpg/video.mjpg
    # port http://142.112.65.17:80/mjpg/video.mjpg
    # golf http://184.68.127.82:89/mjpg/video.mjpg
    
    try:
        return StreamingHttpResponse(gen(VideoCamera(link)), content_type="multipart/x-mixed-replace;boundary=frame")
    except HttpResponseServerError as e:
        print("aborted")


# def pauseLiveStream(request):
#     # stop live streaming and image saving
#     global t
#     global stop
#     stop = True
#     if(not q.empty()):
#         stop = True
#         print("on pause action ----------queue is not empty, I am gonna release camera")
#         target=q.get()
#         print("the target in queue is ",target)
#         target.__del__
#         # time.sleep(3)
#         print("deleting on pause action ++++++++++++++++++++++")
#     # print("current thread is ", threading.current_thread().name)


#     print("pause live stream, stop value  is ", stop)

#     return render(request, 'Interface/livestream/pauseLiveStream.html', )


# @gzip.gzip_page
# def pauseLiveStream_page(request):
#     if(request.session['tempId']):
#         tempId = request.session['tempId']
#         print("On page pause live stream paaaaage, the request post value will be =============",
#               request.session['tempId'])
#         print(type(tempId))
#     if(tempId == "22"):
#         link = "http://142.112.65.17:80/mjpg/video.mjpg"

#     else:
#         link = "http://184.68.127.82:89/mjpg/video.mjpg"

#     try:
#         return StreamingHttpResponse(pause_gen(VideoCamera(link)), content_type="multipart/x-mixed-replace;boundary=frame")
#     except HttpResponseServerError as e:
#         print("aborted")
