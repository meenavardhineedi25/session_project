from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Home Page
def home(request):
    return render(request, 'home.html')


# Set Session + Cookie
def set_session(request):
    request.session['username'] = 'Meena'
    request.session['role'] = 'Student'

    response = HttpResponse("Session and Cookie Set Successfully!")

    # Setting Cookie
    response.set_cookie('fav_color', 'blue')

    return response


# Get Session + Cookie
def get_session(request):
    username = request.session.get('username', 'Not Found')
    role = request.session.get('role', 'Not Found')

    fav_color = request.COOKIES.get('fav_color', 'No Cookie')

    return HttpResponse(f"""
        Username: {username} <br>
        Role: {role} <br>
        Favorite Color (Cookie): {fav_color}
    """)


# Delete Session
def delete_session(request):
    request.session.flush()
    return HttpResponse("Session Deleted Successfully!")