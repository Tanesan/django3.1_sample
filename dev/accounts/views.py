# from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

def authentificate_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if username == 'user1' and password == 'secret':
                return HttpResponseRedirect('/home_monitoring/')
            else:
                return render(
                    request,
                    'registration/login.html',
                    { 'form':form, 'msg':'Authentication failed'})
        else:
            return render(request, 'registration/login.html', {'form': form})

    else:
        form = LoginForm()
        return render(
            request,
            'registration/login.html',
            {'form':form, 'msg':''})








