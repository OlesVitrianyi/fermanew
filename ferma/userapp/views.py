from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import Profile


# def test_def(request):
#     return HttpResponse('A page of vision-apps')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('index')
        else:
            # Return an 'invalid login' error message.
            ...
            messages.success(request, "Там була помилка!")
            return redirect('login')
    else:
        return render(request, 'userapp/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "Ви вийшли успішно")
    return redirect('index')


# def register_user(request):
#     if request.method == "POST":
#         form = RegisterUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             messages.success(request, "Реєстрацію завершено!")
#             return redirect('index')
#     else:
#         form = RegisterUserForm()
#     return render(request, 'userapp/register_user.html', {
#         'form': form,
#     })

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            phone_number = form.cleaned_data.get('phone_number')
            Profile.objects.create(user=user, phone_number=phone_number)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Реєстрацію завершено!")
            return redirect('index')
    else:
        form = RegisterUserForm()
    return render(request, 'userapp/register_user.html', {'form': form})
