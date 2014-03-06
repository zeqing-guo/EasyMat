# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from numpy import abs, cos, sin, linspace, arange, pi, exp, random
from matplotlib.pylab import figure, plot, xlabel, ylabel, title, xlim, ylim, legend, show, savefig, subplot, hist, text, axis, grid, gcf
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
    try:
        query = ""
        mimeType = ""
        savePath = ""
    
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