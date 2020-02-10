from django.shortcuts import render
# Create your views here.
from django.shortcuts import redirect
from .models import Article
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404

def create_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            # обработать данные формы, если метод POST
            form = {
            'text': request.POST["text"], 'title': request.POST["title"]
            }
            # в словаре form будет храниться информация, введенная пользователем
            if form["text"] and form["title"]:
                approve = int(1)
                posts = Article.objects.all()
                for post in posts:
                    if form["title"] == post.title:
                         approve = int(0)

                if approve > 0:
                    Article.objects.create(text=form["text"],
                                       title=form["title"], author=request.user)
                    return redirect('get_article',
                         article_id=Article.objects.get(title=form["title"]).id)
                    # перейти на страницу поста
                else:
                    form['errors'] = u"Повторяющееся название статьи"
                    return render(request, 'create_post.html', {'form': form})
            else:
                # если введенные данные некорректны
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            # просто вернуть страницу с формой, если метод GET
            return render(request, 'create_post.html', {})
    else:
        raise Http404


def create_user(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            # обработать данные формы, если метод POST
            form = {
            'username': request.POST["username"],
            'email': request.POST["email"],
            'first_password': request.POST['first_password'],
            'second_password': request.POST['second_password']
            }
            # в словаре form будет храниться информация, введенная пользователем
            if form["username"] and form["first_password"] and form["second_password"]:
                approve = int(1)
                posts = User.objects.all();
                for post in posts:
                    if form["username"] == post.username:
                         approve = int(0)

                if approve > 0:
                    if form["first_password"] == form["second_password"]:
                        User.objects.create_user(form["username"], form["email"]
                                                    , form["first_password"])
                        return redirect('sign_in')
                    else:
                        form['errors'] = u"Пароли не совпадают"
                        return render(request, 'sign_up.html', {'form': form})
                    # перейти на страницу поста
                else:
                    form['errors'] = u"Повторяющееся логин пользователя"
                    return render(request, 'sign_up.html', {'form': form})
            else:
                # если введенные данные некорректны
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'sign_up.html', {'form': form})
        else:
            # просто вернуть страницу с формой, если метод GET
            return render(request, 'sign_up.html', {})
    else:
        raise Http404

def login_user(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            # обработать данные формы, если метод POST
            form = {
            'username': request.POST["username"],
            'password': request.POST['password'],
            }
            # в словаре form будет храниться информация, введенная пользователем
            if form["username"] and form["password"]:
                user = authenticate(username=form["username"],
                                    password=form["password"])
                if user != None:
                    login(request, user)
                    return redirect('home')
                    # перейти на страницу поста
                else:
                    form['errors'] = u"Такой связки логин/пароль не существует"
                    return render(request, 'sign_in.html', {'form': form})
            else:
                # если введенные данные некорректны
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'sign_in.html', {'form': form})
        else:
            # просто вернуть страницу с формой, если метод GET
            return render(request, 'sign_in.html', {})
    else:
        raise Http404
