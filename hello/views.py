from django.shortcuts import render
import robot

# Create your views here.

from django.http import HttpResponse

def index(request):
    
    if request.method == 'POST' and 'benu1' in request.POST:

    # import function to run
    #   from .robot_libs import benu1

    # call function
        robot.run('robot_libs/benu1.robot', outputdir='robot_libs/log') 
    #return HttpResponse('Hello')
    # return user to required page
    #return HttpResponseRedirect(reverse(app_name:view_name)
    return render(request, "index.html")