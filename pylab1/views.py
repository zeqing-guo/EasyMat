# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from numpy import *
from matplotlib.pylab import *
from matplotlib.cbook import *
from matplotlib.patches import Ellipse
from mpl_toolkits.mplot3d import Axes3D
from util import mimeTypeDict
from django.conf import settings

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
    returnInfo = {}
    try:
        query = ""
        mimeType = ""
    	imgData = cStringIO.StringIO()
    
        # Test and get npQuery and pltQuery from request
        if (not request.method == "POST") or not ("query" in request.POST or "mimeType" in request.POST or "fileName" in request.POST):
            return HttpResponse("error!")
        mimeType = request.POST["mimeType"]
        fileName = request.POST["fileName"]
        query = request.POST["query"]
    
        # Make sure that the input instruction is valid 
        if not checkScurity(query):
            return HttpResponse("Invalid characters!")
    
        # Split the query and execute thme
        split = re.compile("&%&")
        queryList = split.split(query)
    
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
