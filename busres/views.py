from django.shortcuts import render

from django.http import HttpResponse
from .models import *

# USER = {'USER_ID': '', 'USER_NAME': '' }
USER_ID = ''
USER_NAME = ''

# Create your views here.
def home(request):
    # return HttpResponse("Home page ...")
    return render(request, "login.html", {} )

# login
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        pswd = request.POST['pswd']
        user = UsersData.objects.filter(userid = email, password = pswd )
        if user:
            USER_ID = email
            USER_NAME = user[0].user_name

            CurrentUser.objects.filter(id=1).update(userid = USER_ID, user_name = USER_NAME )
            return render(request, 'home.html', {'user_name': USER_NAME , 'nameInitial': USER_NAME[0] })     
        else:
            return render(request, 'login.html', {'loginError': 'Invalid details :( '})
    else:
        return render(request, "login.html", {})

# logout
def logout(request):
    CurrentUser.objects.filter(id=1).update(userid = '', user_name = '' )
    return render(request, 'login.html', {})

# registration
def registration(request):
    if request.method == "POST":
        email = request.POST['email']
        name = request.POST['name']
        pswd1 = request.POST['pswd1']
        pswd2 = request.POST['pswd2']

        if pswd1 == pswd2:
            user = UsersData.objects.create(userid = email,
                                        user_name = name,
                                        password = pswd1
                                        )
            user.save()
            passedInfo = {'email': email, 'name': name, 'pswd1': pswd1, 'pswd2': pswd2}
            return render(request, "login.html", {'passedInfo': passedInfo} )
        else:
            return render(request, "registration.html", {'pswd_error': 'Retyped password mismatched !'} )
    else:
        return render(request, "registration.html", {})

# feedback
def feedback(request):
    return render(request, "feedback.html")

# showBuses
def showBuses(request):
    if request.method == "POST":
        source_search = request.POST['source_search']
        data = Booking.objects.filter(source= source_search)

        return render(request, "showBuses.html", {'source_search': source_search, 'data': data })
    else:
        return render(request, "showBuses.html", {})
    
# makeBookings
def makeBookings(request):
    curruser = CurrentUser.objects.first()
    userid = curruser.userid
    user_name = curruser.user_name
    if request.method == 'POST':
        bus_id = int(request.POST['selected_bus'])       # if bus_id received, means user clicked 'book' button
        req_seats = int(request.POST['req_seats'])

        # if bus_id:
        book = UserBookings.objects.create(userid = userid,
                                        user_name = user_name,
                                        booking_id_id = bus_id,      # CAUTION ! _id at end is a minor adjustment (jugad) to make it work
                                        req_seats = req_seats,
                                        status = "Booked")
                                 # avoid using "_id" in column filed names as django often adds this thing in column names like "xyz" becomes "xyz_id" automatically in db
        book.save()

        return render(request, "home.html", {'book': book})
    else:
        return render(request, "showBuses.html", {})

# userBookings
def userBookings(request):
    curruser = CurrentUser.objects.all()
    if curruser.exists():
        userid = curruser[0].userid
        user_name = curruser[0].user_name
        print('---------',userid,'---------')
        data = UserBookings.objects.filter(userid=userid)
        # print('_______________',data.booking_id_id,'_________________')
        # booking_data = Booking.objects.filter(id = id in data.booking_id_id)
        booking_data=''
        return render(request,"userBookings.html", {'data': data, 'booking_data': booking_data})