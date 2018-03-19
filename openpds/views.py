import json

from django.http import JsonResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def home(request):
    return render_to_response('home.html', {}, RequestContext(request))

def ping(request):
    return JsonResponse({"success": True})
