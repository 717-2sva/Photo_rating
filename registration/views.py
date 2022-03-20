from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import FormView
from .forms import MyForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('/news')
        else:
            messages.info(request, 'Неверное имя пользователя или пароль')

    context = {}
    return render(request, 'registration/login.html', context)

def logoutUser (request):
    logout(request)
    return redirect('login')






# Вариант регистрации на базе класса FormView
class MyRegisterFormView(FormView):
    # Указажем какую форму мы будем использовать для регистрации наших пользователей, в нашем случае
    # это UserCreationForm - стандартный класс Django унаследованный
    form_class = MyForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/news"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "registration/registration.html"

    def form_valid(self, form):
        form.save()
        # Функция super( тип [ , объект или тип ] )
        # Возвратите объект прокси, который делегирует вызовы метода родительскому или родственному классу типа .
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)