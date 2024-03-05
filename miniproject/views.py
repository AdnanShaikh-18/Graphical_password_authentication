from django.core.mail import *
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from random import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def home(request):

    tweets = Tweet.objects.all().order_by('-date_created')
    context = {'tweet': tweets}

    if request.method == 'GET':
        return render(request, 'home.html', context)
    else:
        input = request.POST['inputtweet']
        print(input)
        t = Tweet.objects.create(user=request.user, body=input)
        t.save()
        return render(request, 'home.html', context)


def profiles(request):
    if request.method == 'GET':
        prof = User.objects.all()
        profile = list(prof)
        shuffle(profile)
        context = {'profile': profile}
        return render(request, 'profile.html', context)


def imagelogin(request):
    pass

#     # getting all color objects
#     col1=Color1.objects.all()
#     col2=Color2.objects.all()
#     col3=Color3.objects.all()

#     # converting to list
#     color1=list(col1)
#     color2=list(col2)
#     color3=list(col3)
#     # shuffling the order
#     shuffle(color1)
#     shuffle(color2)
#     shuffle(color3)
#     context={'color1':color1,'color2':color2,'color3':color3}
#     if request.method=='GET':
#         return render(request,'imagelogin.html',context)

#     else:
#         u=User.objects.get(username=request.POST['uname'])
#         print(u)
#         val1=request.POST['color1']
#         val2=request.POST['color2']
#         val3=request.POST['color3']
#         print(val1+"\t"+val2+"\t"+val3)
#         print(request.POST['uname'])
#         person=Profile.objects.create(user=u,color1=val1,color2=val2,color3=val3)


#         return render(request,'imagelogin.html',context)


def register(request):
    # getting all color objects
    col1 = Color1.objects.all()
    col2 = Color2.objects.all()
    col3 = Color3.objects.all()

    # converting to list
    color1 = list(col1)
    color2 = list(col2)
    color3 = list(col3)

    # shuffling the order of color
    # heart of the project
    shuffle(color1)
    shuffle(color2)
    shuffle(color3)
    context = {'color1': color1, 'color2': color2, 'color3': color3}

    if request.method == 'GET':
        return render(request, 'register.html', context)
    else:

        uname = request.POST['username']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        em = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        print(uname)
        print(pass1)
        print(pass2)
        print(em)
        print(fname)
        print(lname)

        val1 = request.POST['color1']
        val2 = request.POST['color2']
        val3 = request.POST['color3']
        print(val1+"\t"+val2+"\t"+val3)

        # person=Profile.objects.create(user=uname,color1=val1,color2=val2,color3=val3)

        if pass1 == pass2:
            try:
                user = User.objects.create_user(
                    username=uname, password=pass1, email=em, first_name=fname, last_name=lname)
                user.save()
                person = Profile.objects.create(
                    user=uname, color1=val1, color2=val2, color3=val3, password=pass1)
                person.save()
                login(request, user)
                messages.success(request, 'registeration successfull')

                return redirect('home')
            except:
                messages.error(
                    request, 'username already taken !! try new one')
                return render(request, 'register.html', context)

        else:
            messages.error(request, 'passwords didnt matched')
        return render(request, 'register.html', context)


def takeprofile(request):
    if request.method == 'GET':
        return render(request, 'takeprofile.html')
    else:
        accoutnurl = request.POST['accurl']
        user_bio = request.POST['bio']
        gender = request.POST['gender']
        print(accoutnurl)
        print(gender)
        # print(bio)
        usern = request.user.username
        print(usern)
        p = get_object_or_404(Profile, user=usern)
        p.bio = user_bio
        p.social_media_url = accoutnurl
        p.gender = gender
        p.save()
        messages.success(request, 'PROFILE CREATED SUCCESSFULLY GOOD TO  GO')
        return redirect('home')


def logout_user(request):
    logout(request)
    messages.warning(request, 'you have logged out')
    return redirect('home')


def login_user(request):
    # getting all color objects
    col1 = Color1.objects.all()
    col2 = Color2.objects.all()
    col3 = Color3.objects.all()

    # converting to list
    color1 = list(col1)
    color2 = list(col2)
    color3 = list(col3)
    # shuffling the order
    shuffle(color1)
    shuffle(color2)
    shuffle(color3)
    context = {'color1': color1, 'color2': color2, 'color3': color3}

    # get request

    if request.method == "GET":
        return render(request, 'login.html', context)
    else:
        uname = request.POST['username']
        pword = request.POST['password']
        val1 = request.POST
        # print(val1+"\t"+val2+"\t"+val3)
        val1 = request.POST['colr1']

        val2 = request.POST['colr2']
        val3 = request.POST['colr3']
        # prof=get_object_or_404(Profile,user=uname)
        # print(prof.user)
        # print(prof.color1)
        user = authenticate(request, username=uname, password=pword)
        if user is not None:
            try:
                prof = get_object_or_404(Profile, user=uname)
                a = val1 == prof.color1
                b = val2 == prof.color2
                c = val3 = prof.color3
                if a and b and c:
                    login(request, user)
                    messages.success(request, 'LOG IN SUCCESSFULL')
                    return redirect('home')
                else:
                    messages.error(request, 'COLOR PATTERNS DIDNT MATCHED')
                    return redirect('login')
            except:
                messages.error(request, 'NO SUCH USER FOUND')
                return redirect('login')

        else:
            messages.error(request, 'USERNAME OR PASSWORD DIDNT MATCHED')
            return render(request, 'login.html', context)


def uprofile(request, pk):
    user = get_object_or_404(User, id=pk)
    uname = user.username
    print(uname)
    if request.method == 'GET':
        profile = get_object_or_404(Profile, user=uname)
        tweets = Tweet.objects.filter(user_id=pk)
        context = {'profile': profile, 'tweets': tweets}
        return render(request, 'uprofile.html', context)


def takeemail(request):
    if request.method == 'GET':
        return render(request, 'takeemail.html')
        # messages.info(request,'')
    else:
        tosend = request.POST['otpemail']
        uname = request.POST['uname']

        print(tosend)
        otpnum = randint(1000, 9999)
        print(otpnum)
        send_mail(
            'your otp',
            'enter the otp and dont share with anyone \n {}'.format(otpnum),
            'rahilshaikh7117@gmail.com',
            [tosend],
            fail_silently=False

        )
        messages.info(request, 'Enter the otp')
        context = {'otpgenerated': otpnum, 'youremail': tosend, 'uname': uname}
        return render(request, 'otp.html', context)
        # return render(request,'takeemail.html')


# from django.contrib.auth import get_user_model
def otp(request):
    if request.method == 'GET':
        # print()
        return render(request, 'otp.html')
    else:

        otp_by_user = request.POST['otp_by_user']
        checker_otp = request.POST['checker_otp']
        emaill = request.POST['email']
        uname = request.POST['username']
        user = get_object_or_404(Profile, user=uname)
        # userr=request.user
        print(user.password)

        if otp_by_user == checker_otp:

            u = authenticate(request, username=uname, password=user.password)
            if u is not None:
                login(request, u)
                messages.success(request, 'YOU HAVE SUCCESSFULLY LOGGED IN')
                return redirect('home')
            else:
                messages.warning(request, 'USER NOT FOUND')
                return redirect('login')
        else:
            messages.error(request, 'OTP DIDNT MATCHED')
            # print(user)
            # print(otp_by_user)
            # print(uname)
            # print(checker_otp)
            # print(type(otp_by_user))
            # print(type(checker_otp))
            return render(request, 'otp.html')
