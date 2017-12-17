# from django.http import HttpResponse
# from alexmateva.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def login_view(request):
    form = LoginForm()

    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(reverse('index'))
        else:
            alert = form.errors
            return render(request, 'login.html', {'alert': alert})
    return render(request, 'login.html', locals())


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


# def login(request):
#     m = User.objects.get(username=request.POST['username'])
#     if m.password == request.POST['password']:
#         request.session['member_id'] = m.id
#         return HttpResponse("You're logged in.")
#     else:
#         return HttpResponse("Your username and password didn't match.")
