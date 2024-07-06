from django.shortcuts import redirect, render, get_object_or_404
from django.conf import settings
import shutil
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import CustomUser, AddNewCustomer, Event, EventImage, Users
from django.http import HttpResponse
from itertools import groupby
from django.contrib import messages
import re
import os
from urllib.parse import urlencode
from itertools import groupby
from .create_encoder import encoder_script
import pickle
import numpy as np
import cv2
import face_recognition


def contains_vowel(string):
    vowels = set("aeiouAEIOU")  # Vowels Validation
    return any(char in vowels for char in string)

def is_valid_phone(phone):
    pattern = re.compile(r'^\d{10}$')
    return bool(pattern.match(phone))

def validate_email(email):
    regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'  # Email Validation | Format Starts with strings takes , one or more words, takes @ symbol
    return re.match(regex, email)

def validate_password(password):
    regex = (
        r'^(?=.*[a-z])'  # At least one lowercase letter
        r'(?=.*[A-Z])'  # At least one uppercase letter
        r'(?=.*\W{1,})'  # At least one symbols
        r'.{7,}$'  # Minimum length of 7 characters
    )
    return re.match(regex, password)

# ------------------------ ADMIN VIEWS ------------------------
def admin_home(request):

    user_id = request.session.get('user_id')
    if user_id:
        try:
            user = CustomUser.objects.get(pk=user_id)
            username = user.username
        except CustomUser.DoesNotExist:
            # Handle case where user does not exist
            return redirect('admin_index')
    else:
        # User is not logged in
        return redirect('admin_index')

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        organization = request.POST.get('add_customer_organization')
        organizations_name = request.POST.get('organizations_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')[:10]

        AddNewCustomer.objects.create(
            Customer_full_name=full_name,
            Organization_name=organization,
            Customer_email=email,
            Customer_mobile=phone,
        )

        return redirect('admin_home')

    return render(request, "Admin/home.html", context={'customer_data': AddNewCustomer.objects.all(), 'username': username})

def admin_index(request):

    # error_message = None
    # data = {}
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        try:
            # Fetch the user by phone number
            user = CustomUser.objects.get(phone=phone)
            username = user.username

            user = CustomUser.objects.get(username=username)
            print(user)
            stored_password = user.password

            if stored_password == password:
                # Authentication successful
                request.session['user_id'] = user.id
                return redirect('admin_home')
            else:
                # Invalid password
                messages.error(request, 'Invalid username or password!')
        except CustomUser.DoesNotExist:
            # User with provided username does not exist
            messages.error(request, 'User not Found!')

    return render(request, 'Admin/__index.html')

def admin_home1(request, customer_id):
    
    user_id = request.session.get('user_id')
    print("event user id",user_id)
    
    if not user_id:
        # User is not logged in
        return redirect('admin_index')

    try:
        global username
        user = CustomUser.objects.get(pk=user_id)
        username = user.username
    except CustomUser.DoesNotExist:
        # Handle case where user does not exist
        return redirect('admin_index')

    
    customer = AddNewCustomer.objects.get(pk=customer_id)
    Customer_full_name = customer.Customer_full_name

    if request.method == 'POST':
        if 'share-btn' in request.POST:
            # If the "Share" button is clicked
            event_name = request.POST.get('event')
            print('name', event_name)
            # Redirect to the OTP page with the event name as a query parameter
            return redirect(reverse('user_index') + f'?event={event_name}&customer_id={customer_id}&Customer_full_name={Customer_full_name}')
        else:
            # If the form is submitted
            event_name = request.POST.get('eventName')
            event_date = request.POST.get('eventDate')
            event_description = request.POST.get('eventDescription')
            event_images = request.FILES.getlist('eventImages')

            # Get the customer object
            try:
                customer = AddNewCustomer.objects.get(pk=customer_id)
                Customer_full_name = customer.Customer_full_name
                print('cust first name : ', Customer_full_name)
            except AddNewCustomer.DoesNotExist:
                # Handle case where customer does not exist
                return redirect('login')

            # Create or get existing event
            event, created = Event.objects.get_or_create(
                admin=user,  # Use the logged-in user as the admin of the event
                customer=customer,
                name=event_name,
                defaults={'date': event_date, 'description': event_description}
            )

            # Save event images
            for image in event_images:
                EventImage.objects.create(event=event, image=image)

            # Create image encodings using encoder_script method
            # -------------- Encoding Start Here ------------------
            imgs_path = f"media/{username}/{Customer_full_name}/{event}"
            print(imgs_path)
            if not os.path.exists(imgs_path):
                os.makedirs(imgs_path)

            encs_path = os.path.join(imgs_path, "Encodings")
            if not os.path.exists(encs_path):
                os.makedirs(encs_path)

            encoder_script(dir_path=imgs_path, enc_path=encs_path)
            # -------------- Encoding Ends Here ------------------

            # Redirect to the event page to display images
            return redirect(reverse('user_images', kwargs={'event_id': event.id}))

    else:
        # Fetch existing events and group them by name
        existing_events = Event.objects.filter(customer_id=customer_id).order_by('name')
        grouped_events = {key: list(group) for key, group in groupby(existing_events, lambda x: x.name)}

        customer_names = AddNewCustomer.objects.filter(id=customer_id).values_list('Customer_full_name', flat=True)
    
        return render(request, 'Admin/home1.html', {'grouped_events': grouped_events, 'username': username, 'customer_id': customer_id, 'customer_names': customer_names})

def user_images(request, event_id):

    user_id = request.session.get('user_id')
    print("event user id",user_id)
    
    if not user_id:
        # User is not logged in
        return redirect('admin_index')

    user = CustomUser.objects.get(pk=user_id)
    username = user.username
    event = get_object_or_404(Event, pk=event_id)
    images = event.images.all()
    customer_id = event.customer_id

    return render(request, 'Admin/images.html',  {'event': event, 'images': images, 'username': username, 'customer_id': customer_id})

def admin_signup(request):

    error_message = None
    data = {}

    if request.method == "POST":
        # Extract form data
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        organizationname = request.POST.get('organizationname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')

        # Manual Validation
        if not fname or not lname:
            error_message = "First Name and Last Name are required!"
        elif len(fname) < 3 or len(lname) < 3:
            error_message = "First Name and Last Name must be 3 characters long or more"
        elif not contains_vowel(fname) or not contains_vowel(lname):
            error_message = "First Name and Last Name must be Valid!"
        elif not validate_email(email):
            error_message = "Invalid email format. Please enter a valid email address."
        elif len(phone) != 10 or not phone.isdigit():
            error_message = "Phone Number must be 10 digits long and contain only numbers"
        elif not validate_password(password):
            error_message = "Password must contain at least one uppercase letter, one lowercase letter, one symbol, and be at least 7 characters long"
        elif password != repassword:
            error_message = "Passwords do not match"
        else:
            # Check if the email or username is already registered
            if CustomUser.objects.filter(email=email).exists():
                error_message = 'Email is already registered. Please use a different email.'
            elif CustomUser.objects.filter(username=username).exists():
                error_message = 'Username is already taken. Please choose a different username.'
            else:
                # Creating the user if all validations pass
                user = CustomUser.objects.create(
                    email=email, organizationname=organizationname, username=username,
                    phone=phone, fname=fname, lname=lname, password=password)
                user.save()

                messages.success(request, 'Account created successfully!')
                return redirect('admin_index')

        # If there are errors, populate the data dict with the form values
        if error_message:
            data = {
                'error': error_message,
                'values': {
                    'fname': fname,
                    'lname': lname,
                    'email': email,
                    'phone': phone,
                    'organizationname': organizationname,
                    'username': username,
                }
            }
            return render(request, 'Admin/signup.html', context=data)

    return render(request, "Admin/signup.html")

def logout(request):
    # Clear the session data
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('admin_index')

def update_user(request, id):

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')

        user = AddNewCustomer.objects.get(pk=id)
        user.Customer_full_name = full_name
        user.Customer_mobile = phone
        user.save()
        return redirect('admin_home')

    return render(request, 'Admin/home.html')

def delete_user(request, id):
    user = AddNewCustomer.objects.filter(pk=id)
    user.delete()

    context = {
        'user': user,
    }
    return redirect('admin_home')

def delete_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    
    # Construct the path to the event folder
    event_folder = os.path.join(settings.MEDIA_ROOT, str(event.admin), str(event.customer), str(event.name))
    
    # Check if the event folder exists
    if os.path.exists(event_folder):
        # Delete the event folder and all its contents from Django media storage
        try:
            shutil.rmtree(event_folder)
        except Exception as e:
            # Handle any exceptions or errors
            pass
    
    # Check if the event folder exists in the local filesystem
    if os.path.exists(event_folder):
        # Delete the event folder and all its contents from the local filesystem
        try:
            shutil.rmtree(event_folder)
        except Exception as e:
            # Handle any exceptions or errors
            pass

    # Delete the event from the database
    event.delete()
    
    return redirect('admin_home1', customer_id=event.customer.id)

def admin_dashboard(request):
    user_id = request.session.get('user_id')
    print("event user id",user_id)
    
    if not user_id:
        # User is not logged in
        return redirect('login')
    return render(request, "Admin/dashboard.html")
# ------------------------ ADMIN END ------------------------

# ------------------------ USER VIEWS ------------------------

def user_dashboard(request):
    user = CustomUser.objects.get(pk=user_id)
    username = user.username

    return render(request, "User/dashboard.html", {'username': username})

def user_index(request):
    event_name = request.GET.get('event')
    print('index-name', event_name)
    customer_id = request.GET.get('customer_id')
    print('index-id', customer_id)
    Customer_full_name = request.GET.get('Customer_full_name')
    print('index-name', Customer_full_name)

    error_message = None
    data = {
        'event_name': event_name,
        'customer_id': customer_id,
        'Customer_full_name': Customer_full_name,
    }

    if request.method == "POST":
        # Extract form data
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        phone = request.POST.get('phone').strip()

        # Ensure we have the GET parameters on POST as well
        event_name = request.POST.get('event', event_name)
        customer_id = request.POST.get('customer_id', customer_id)
        Customer_full_name = request.POST.get('Customer_full_name', Customer_full_name)
        print('POST parameters:', event_name, customer_id, Customer_full_name)


        # Manual Validation
        if not firstname or not lastname:
            error_message = "First Name and Last Name are required!"
        elif len(firstname) < 3 or len(lastname) < 3:
            error_message = "First Name and Last Name must be 3 characters long or more"
        elif not contains_vowel(firstname) or not contains_vowel(lastname):
            error_message = "First Name and Last Name must be Valid!"
        elif len(phone) != 10 or not phone.isdigit():
            error_message = "Phone Number must be 10 digits long and contain only numbers"
        else:
            user = Users.objects.create(first_name=firstname, last_name=lastname, phone=phone)
            user.save()

            # Redirecting to the OTP view with the appropriate query parameters
            return redirect(reverse('user_otp') + f'?event={event_name}&customer_id={customer_id}&Customer_full_name={Customer_full_name}')

        # If there are errors, populate the data dict with the form values
        if error_message:
            data.update({
                'error': error_message,
                'values': {
                    'fname': firstname,
                    'lname': lastname,
                    'phone': phone,
                }
            })
            return redirect(reverse('user_index') + f'?event={event_name}&customer_id={customer_id}&Customer_full_name={Customer_full_name}',context=data)
            # return render(request, 'User/__index.html', context=data)
    
    return render(request, "User/__index.html", context=data)


def user_otp(request):
    # GET request
    event_name = request.GET.get('event', '')
    print('otp', event_name)
    customer_id = request.GET.get('customer_id', '')
    print('otp-id',customer_id)
    Customer_full_name = request.GET.get('Customer_full_name', '')
    print('otp-name', Customer_full_name)

    error_message = None

    if request.method == "POST":
        otp1 = request.POST.get('otp1')
        otp2 = request.POST.get('otp2')
        otp3 = request.POST.get('otp3')
        otp4 = request.POST.get('otp4')

        # Validate the OTP (you can replace this with your own validation logic)
        if otp1 == '1' and otp2 == '2' and otp3 == '3' and otp4 == '4':
            # Passing event_name, customer_id, and Customer_full_name to the next page
            return redirect(reverse('user_selfie') + f'?event={event_name}&customer_id={customer_id}&Customer_full_name={Customer_full_name}')
        else:
            error_message = "Incorrect OTP. Please try again."

    # Creating the context dictionary
    data = {
        'event_name': event_name,
        'error_message': error_message,
        'customer_id': customer_id,
        'Customer_full_name': Customer_full_name,
    }

    # Passing the context to the render function
    return render(request, 'User/otp.html', context=data)

def user_selfie(request):
    event_name = request.GET.get('event', '')
    customer_id = request.GET.get('customer_id', '')
    Customer_full_name = request.GET.get('Customer_full_name', '') 
    user_id = request.session.get('user_id')
    user = CustomUser.objects.get(pk=user_id)
    username = user.username
    
    image_path = []

    # Face Encodings
    path = f"media/{username}/{Customer_full_name}/{event_name}/Encodings/image_encodings.pickle"
    print(path)
    img_path = f"media/{username}/{Customer_full_name}/{event_name}/Encodings/full_image_path.pickle"
    print(img_path)

    print(username,Customer_full_name,event_name)

    # print(path)
    with open(path, "rb") as file, open(img_path, 'rb') as img_labels:
        data = pickle.load(file)
        known_labels = pickle.load(img_labels)


    if request.method == 'POST':
        matches = dict()

        images = request.FILES.getlist('selfie')
        print("images", images)

        img = images[0].read()
        img = np.frombuffer(img, np.uint8)
        img = cv2.imdecode(img, cv2.IMREAD_COLOR)
        # cv2.imshow('image', img)
        # cv2.waitKey(0)

        # upload_encodes = face_recognition.face_encodings(img)[0]

        image_encoding = face_recognition.face_encodings(img)
        if image_encoding:
            image_encoding = image_encoding[0]  # Assuming only one face per image
            for label, encodings in data.items():
                for encoding in encodings:
                    match = face_recognition.compare_faces([encoding], image_encoding, tolerance=0.65)
                    if match[0]:
                        matches[label] = known_labels[label]

        data = {
            'matched_images_path' : matches,
            'event_name': event_name,
            'customer_id': customer_id,
            'Customer_full_name': Customer_full_name,
            'username' : username,
            'images' : images,
        }

        return render(request, 'User/dashboard.html', context=data)
    else:
        return render(request, 'User/selfie.html',{'event_name': event_name, 'customer_id': customer_id, 'Customer_full_name': Customer_full_name})

# ------------------------ USER END  ------------------------
