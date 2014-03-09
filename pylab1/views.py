# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
<<<<<<< HEAD
from numpy import *
from matplotlib.pylab import *
from matplotlib.cbook import *
from matplotlib.patches import Ellipse
from mpl_toolkits.mplot3d import Axes3D
from util import mimeTypeDict
from django.conf import settings
=======
from numpy import abs, cos, sin, linspace, arange, pi, exp, random
from matplotlib.pylab import figure, plot, xlabel, ylabel, title, xlim, ylim, legend, show, savefig, subplot, hist, text, axis, grid, gcf
from util import mimeTypeDict
>>>>>>> 572ea2b005db99e2deeae8ad0ecb7bd12235e50c

import cStringIO
import Image
import json
import re

# Create your views here.
def query(request):
    return render_to_response("index.html")

def help(request):
    return render_to_response("help.html")
        
def ajax(request):
<<<<<<< HEAD
    returnInfo = {}
    try:
        query = ""
        mimeType = ""
    	imgData = cStringIO.StringIO()
=======
    try:
        query = ""
        mimeType = ""
        savePath = ""
>>>>>>> 572ea2b005db99e2deeae8ad0ecb7bd12235e50c
    
        # Test and get npQuery and pltQuery from request
        if (not request.method == "POST") or not ("query" in request.POST or "mimeType" in request.POST or "fileName" in request.POST):
            return HttpResponse("error!")
        mimeType = request.POST["mimeType"]
        fileName = request.POST["fileName"]
        query = request.POST["query"]
    
        # Make sure that the input instruction is valid 
<<<<<<< HEAD
        if not checkScurity(query):
            return HttpResponse("Invalid characters!")
=======
        #if not checkScurity(query):
        #    return HttpResponse("发现非法字符")
>>>>>>> 572ea2b005db99e2deeae8ad0ecb7bd12235e50c
    
        # Split the query and execute thme
        split = re.compile("&%&")
        queryList = split.split(query)
    
        for queryItem in queryList:
            exec(queryItem)
        
        # Save the image
<<<<<<< HEAD
        savefig(imgData, format = mimeType)
        # Clear the streamIO of matplotlib.pylib
        gcf().clear()
    
	    # Response
        response = HttpResponse(mimetype = mimeTypeDict(mimeType))
        response['Content-Disposition'] = 'attachment; filename=test.%s' % mimeType
        response.write(imgData.getvalue().encode("base64").strip())
        return response
    except Exception, data:
        return HttpResponse([True, data])

def ajax_file(request):
    imgData = cStringIO.StringIO()
    mimeType = ""
    if request.method != "POST" or not ("mimeType" in request.POST):
        return HttpResponse("TrueError!")
    fileObj = request.FILES["file"]
    mimeType = request.POST["mimeType"]
    # File's size must be smaller than 1K
    if fileObj.size > 1000:
        return HttpResponse("TrueThe file is larger than 1kb")

    # File's type must be txt
    pattern = re.compile(".+\.txt$")
    if not pattern.match(fileObj.name):
        return HttpResponse("TrueIt must be a txt file")
    
    file = fileObj.read()

    try:
        # Make sure that the input instruction is valid 
        if not checkScurity(file):
            return HttpResponse("TrueInvalid characters!")
    
        # Split the query and execute thme
        pattern1 = re.compile("\n\t")
        tempStr = pattern1.sub('    ', file)
        pattern2 = re.compile("\n +")
        tempStr2 = pattern2.sub('    ', tempStr)
        pattern3 = re.compile("\n")
        queryList = pattern3.split(tempStr2)
        for queryItem in queryList:
            exec(queryItem)
        
        # Save the image
        savefig(imgData, format = mimeType)
        # Clear the streamIO of matplotlib.pylib
        gcf().clear()
    
    	# Response
        response = HttpResponse(mimetype = mimeTypeDict(mimeType))
        response['Content-Disposition'] = 'attachment; filename=test.%s' % mimeType
        response.write(imgData.getvalue().encode("base64").strip())
        return response
    except Exception, data:
        return HttpResponse([True, data])

def checkScurity(query):
    semicolon = ';'
    if query.find(semicolon) > -1:
        return False
    else:
        return True
=======
        savePath = "media/save/%s.%s" % (fileName, mimeType)
        savefig(savePath)
        
        # Clear the streamIO of matplotlib.pylib
        gcf().clear()
    
        # Response
        payload = {"url": savePath, "format": mimeType}
    except Exception,data:
        print Exception,":",data
    return HttpResponse(json.dumps(payload), mimetype="application/json")

def checkScurity(query):
    semicolon = '%'
    if query.find(semicolon):
        return False
    else:
        return True
>>>>>>> 572ea2b005db99e2deeae8ad0ecb7bd12235e50c
