from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm, LoginForm
from django.contrib.auth.decorators import login_required
from .models import Trip, ItineraryItem

def home(request):
    # Your logic for the homepage view
    return render(request, 'travel_itinerary_app/home.html')


@login_required
def itinerary(request):
    return render(request, 'travel_itinerary_app/itinerary.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to the homepage or another desired page upon successful signup
    else:
        form = SignupForm()
    return render(request, 'travel_itinerary_app/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the homepage or another desired page upon successful login
    else:
        form = LoginForm()
    return render(request, 'travel_itinerary_app/login.html', {'form': form})


def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to the login page if the user is not authenticated

    user = request.user  # Get the logged-in user
    past_trips = Trip.objects.filter(user=user)
    current_itinerary = ItineraryItem.objects.filter(user=user)
    context = {
        'user': user,
        'past_trips': past_trips,
        'current_itinerary': current_itinerary,
    }

    return render(request, 'travel_itinerary_app/profile.html', context)
