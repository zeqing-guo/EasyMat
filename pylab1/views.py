# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from numpy import abs, cos, sin, linspace, arange, pi, exp, random
from matplotlib.pylab import figure, plot, xlabel, ylabel, title, xlim, ylim, legend, show, savefig, subplot, hist, text, axis, grid
from util import mimeTypeDict

import cStringIO
import json
import re

# Create your views here.
def query(request):
    return render_to_response("index.html")

def help(request):
    return render_to_response("help.html")
        
def ajax(request):
    query = ""
    mimeType = ""
    imgData = cStringIO.StringIO()
    
    # Test and get npQuery and pltQuery from request
    if (not request.method == "POST") or not ("query" in request.POST or "mimeType" in request.POST):
        return HttpResponse("error!")
    mimeType = request.POST["mimeType"]
    query = request.POST["query"]
    
    # Make sure that the input instruction is valid 
    #if not checkScurity(query):
    #    return HttpResponse("发现非法字符")
    
    # Split the query and execute thme
    split = re.compile("&%&")
    queryList = split.split(query)
    
    try:
        for queryItem in queryList:
            exec(queryItem)
    except Exception,data:
        print Exception,":",data
        
    # Response
    response = HttpResponse(mimetype = mimeTypeDict(mimeType))
    response['Content-Disposition'] = 'attachment; filename=test.%s' % mimeType
    response.write(imgData.getvalue().encode("base64").strip())
    return response

def checkScurity(query):
    semicolon = '%'
    if query.find(semicolon):
        return False
    else:
        return True