from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from .serializer import SingnupSerializer
from .models import Signup
from rest_framework.views import APIView
from knox.models import AuthToken
from .serializer import UserSerializer, ChangePasswordSerializer

from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticated


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Register API
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


def index(request):
    # ser=SingnupSerializer.get_value("username","Password")
    # print(ser)
    # request.session['name'] = 'aditya'
    email = request.POST.get('email', '')
    password = request.POST.get('password', '')
    print(email)
    print(password)
    if email == 'adityanikhade22@gmail.com' and password == 'Password':

        return HttpResponseRedirect('/website/table/')
    else:
        return render(request, 'website/index.html ')


def table(request):
    # request.session['name'] = Signup.username
    list_ene = Signup.objects.all()
    # table=Signup.objects.all()
    # print(table)
    return render(request, 'website/table.html', {'list_ene': list_ene})


def about(request):
    if request.method == 'POST':
        # serializer=UserSerializer(data=request.data)
        username = request.POST.get('username', '')
        # print(username)
        email = request.POST.get('Email', '')
        password = request.POST.get('Password', '')
        conpasswork = request.POST.get('confirm', '')
        address = request.POST.get('Address', '')

        # x = User.objects.create_user(username=username, Email=email, Password=password, Address=address)
        x = Signup(username=username, Email=email, Password=password, Address=address)
        x.save()
        print("user created")

    else:
        return render(request, 'website/sing.html')


def delete_post(request, post_id=None):
    post_to_delete = Signup.objects.get(id=post_id)
    print(post_to_delete)
    post_to_delete.delete()
    return HttpResponseRedirect('/website/table/')


def Teacher(request):
    email = request.POST.get('email', '')
    password = request.POST.get('password', '')
    print(email)
    print(password)
    if email == 'adityanikhade22@gmail.com' and password == 'Password':
        return render(request, 'website/sing.html')

    else:
        return render(request, 'website/teacher.html ')


def edit(request, id):
    id = Signup.objects.get(id=id)
    print(id)
    return HttpResponseRedirect('/about')


@api_view(['GET'])
def getData(request):
    items = Signup.objects.all()
    serializer = SingnupSerializer(items, many=True)
    return Response(serializer.data)
