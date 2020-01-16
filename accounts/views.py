from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout

# Defines the singup_views function
def signup_view (request):
    # If function is a post request - user had added infomation and clicked sign up
    if request.method == 'POST':
        # creates new instance of the form on the server and accesses POST data
        form = UserCreationForm(request.POST)
        # check if the data which has been passed is valid - returns true for valid, false for invalid
        if form.is_valid():
            # if valid save the form and create an instance of the user
            user = form.save()
            # logs user in
            login(request, user)
            # redirects the user to the upload page
            return redirect('upload_image:upload_image')

    # Else (if it is a get request) create an instance of the form
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html',{'form':form})

# Don't use login as function name because of built-in login function
# Defines the login function
def login_view (request):
    if request.method == 'POST':
        # Checks if username and password is valid
        # Data is used as request.post is not the first parameter
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            # log in user
            user = form.get_user()
            login(request, user)
            # checks if next property is present to redirect user to that page
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                # The default is to take the user to the upload page after logging in
                return redirect ('upload_image:upload_image')
    else:
        # The form will be generated unlss the post request is made
        form = AuthenticationForm()
    return render(request, 'accounts/login.html',{'form':form})

# Defines the logout function
def logout_view (request):
    # If the logout is requested the user is returned to the homepage
    if request.method == 'POST':
        logout(request)
        return redirect('homepage')
