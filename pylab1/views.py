# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from numpy import *
from matplotlib.pylab import *
from mpl_toolkits.mplot3d import Axes3D
from util import mimeTypeDict

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
        #if not checkScurity(query):
        #    return HttpResponse("发现非法字符")
    
        # Split the query and execute thme
        split = re.compile("&%&")
        queryList = split.split(query)
    
        for queryItem in queryList:
            exec(queryItem)
        
        # Save the image
        savefig(imgData, format = mimeType)
        # Clear the streamIO of matplotlib.pylib
        gcf().clear()
    
	# Responsejjj
	response = HttpResponse(mimetype = mimeTypeDict(mimeType))
	response['Content-Disposition'] = 'attachment; filename=test.%s' % mimeType
	response.write(imgData.getvalue().encode("base64").strip())
	return response
    except Exception,data:
        return HttpResponse([True, data])

def checkScurity(query):
    semicolon = '%'
    if query.find(semicolon):
        return False
    else:
        return True
