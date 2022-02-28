from django.shortcuts import render
from django.http import HttpResponse


def index(request):


    return HttpResponse("Login "
                        "<br>"
                        "<br>"
                        "<br>"
                        "<a href='/website'> Student Login</a>"
                        "<br>"
                        "<br>"
                        "<br>"
                        
                        "<a href='/admin'>Admin Login </a>"
                        "<br>"
                        "<br>"
                        "<br>"

                        "<a href='/website/teacher/'>Teacher Login</a>")


