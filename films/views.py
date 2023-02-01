from random import randint, shuffle
from django.shortcuts import render,redirect
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView,CreateView
from .utils import *
from .forms import *
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin


def index(request):
    posts = 'Приветствую, тебя на нашем сайте по подбору фильмов.Зарегистируйся и нажми на кнопку подбора рекомендаций'
    context = {
        'posts':posts,
        'menu':menu,
        'title':'Главная страница',
    }
    return render(request,'films/index.html',context=context)

def about(request):
    posts = 'Сайт создан, для подбора фильмов на основе ваших предпочтений.'
    context = {
        'posts':posts,
        'menu':menu,
        'title':'О нас',
    }
    return render(request,'films/about.html',context=context)

class RegisterUser(DataMixin,CreateView):
    form_class = RegisterUserForm
    template_name = 'films/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *,object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = "Регистрация")
        return dict(list(context.items())+ list(c_def.items()))
    
    def form_valid(self,form):
        user = form.save()
        login(self.request,user)
        return redirect('home')
    
class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'films/login.html'
 
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')

class ChangePasswordView(SuccessMessageMixin,PasswordChangeView):
    template_name = 'films/change_password.html'
    success_message = 'Пароль успешно изменен'
    success_url = reverse_lazy('home')
    
def logout_user(request):
    logout(request)
    return redirect ('login')

def recom(request):
    current_user = request.user
    posts = Film.objects.all()
    rec = Reaction.objects.all().reverse()
    new_soup = []
    for el in posts:
        new_soup.append(el.soup)
    count = CountVectorizer(stop_words='english')
    count_matrix = count.fit_transform(new_soup)
    cosine_sim2 = cosine_similarity(count_matrix, count_matrix)
    ok = False
    for p in rec:
        if p.username == current_user and p.like == 'Понравилось':
            id_film_output1 = get_recs2(current_user, cosine_sim2)
            ok = True
            break
    if (ok == False):
        id_film = randint(1,100) 
    else:
        id_film = id_film_output1 + 1
    for p in posts:
        if p.id == id_film:
            post = p
    context = {
        'post':post,
        'id_film':id_film,
        'user':current_user,
        'id_user':current_user.id,
        'title': 'Подбор фильмов',
    }
    return render (request,'films/recom.html',context=context)

def kabinet_control(request,number):
    current_user = request.user
    if request.method == 'POST':
        if number == 0:
            person = User.objects.get(username=current_user)
            person.delete()
            return redirect('home')
        if number == 1:
            person = User.objects.get(username=current_user)
            return redirect('password_change')

def get_recommendations(cosine_sim,id_title):
    idx1 = id_title
    sim_scores1 = list(enumerate(cosine_sim[idx1]))
    sim_scores1 = sorted(sim_scores1, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores1[1:490]
    movie_indices = [i[0] for i in sim_scores]
    return movie_indices

def send_reaction(request,id_film,number):
    name = User.objects.all()
    current_user = request.user
    posts = Film.objects.all()
    username1 = current_user.username
    for p in name:
        if p.username == username1:
            username1 = p
            break
    for p in posts:
        if p.id == id_film:
            post = p
    if request.method=='POST':
            if number==1:
                p=Reaction.objects.create(username=username1,like="Понравилось",title=post,recsys = False)
            elif number==2:
                p=Reaction.objects.create(username=username1,like="Не понравилось",title=post,recsys = False)
            else:
                p=Reaction.objects.create(username=username1,like="Не смотрел",title=post,recsys = False)
    id_film = id_film
    id_film_output = id_film - 1
    point = Reaction.objects.all()
    posts = Film.objects.all()
    for p in posts:
        if p.id == id_film:
            error = f'{p.title}'
    new_soup = []
    for p in posts:
        new_soup.append(p.soup)
    count = CountVectorizer(stop_words='english')
    count_matrix = count.fit_transform(new_soup)
    cosine_sim2 = cosine_similarity(count_matrix, count_matrix)
    ok = False
    for p in point:
        if p.username == current_user and p.like == 'Понравилось':
            ok=True
    if (ok):
        id_film_output1 = get_recs2(current_user,cosine_sim2)
        for p in posts:
            if p.id == id_film_output1 + 1:
                film = p

    else:
        id_film_output1 = randint(1,490)
        for p in posts:
            if p.id == id_film_output1:
                film = p

    context = {
        'post':film,
        'menu':menu,
        'id_film':id_film_output1,
        'id_user':current_user.id,
        'title':'Подбор фильмов',
        'error':error,
    }
    
    return render (request,'films/recom.html', context=context)


def get_recs2(current_user, cosine_sim): # массив из хз элементов с реакциями по 3 понравилось и не понравилось
    ok = 1
    reacts = Reaction.objects.all().reverse()
    posts = Film.objects.all()
    sim_recs = []
    sim_unrecs = []
    range1 = 6
    range2 = 51
    count_like = 0
    count_dislike = 0
    count1_like = 0
    count1_dislike = 0
    # for p in reacts:
    #     if p.username == current_user and p.like == 'Понравилось':
    #         count_like += 1
    #         recs = p.title.id - 1
    #     if p.username == current_user and p.like == 'Не понравилось':
    #         count_dislike += 1
    #         unrecs = p.title.id - 1
    while ok:
        count_like = 0
        count_dislike = 0
        for p in reacts:
            if p.username == current_user and p.like == 'Понравилось':
                count_like += 1
                if (count_like <= 2):
                    recs = p.title.id - 1
                    sim_scores1 = list(enumerate(cosine_sim[recs]))
                    sim_scores1 = sorted(sim_scores1, key=lambda x: x[1], reverse=True)
                    sim_recs += sim_scores1[1:range1]
            if p.username == current_user and p.like == 'Не понравилось':
                count_dislike += 1
                if (count_dislike <= 2):
                    unrecs = p.title.id - 1     
                    sim_scores1 = list(enumerate(cosine_sim[unrecs]))
                    sim_scores1 = sorted(sim_scores1, key=lambda x: x[1], reverse=True)
                    sim_unrecs += sim_scores1[1:range2]

        setarr = set(sim_recs)
        if len(sim_recs) != len(setarr) and ok: # проверка шоб в масиве реков были одинаковые фильмы
            for i in range(len(sim_recs)-1):
                for j in range(i + 1, len(sim_recs)):
                    if sim_recs[i] == sim_recs[j] and ok:
                        if sim_recs[i] in sim_unrecs: # шоб не было фильмов похожих на задизлайканые
                            continue
                        else:
                            check = 0
                            for p in reacts:
                                if p.username == current_user and p.title.id == sim_recs[i][0] + 1:
                                    check = 1
                                    ok = 1
                                    range1 += 5
                                    break
                            if check == 0:
                                ok = 0
                                return sim_recs[i][0]
                            else:
                                continue
                    else:
                        continue
        else:
            ok = 1
            range1 += 5



def kabinet(request):
    current_user = request.user
    username1 = request.user.username
    react = Reaction.objects.all()
    film = Film.objects.all()
    ok = 0
    ok1 = 0
    for p in react:
        if p.username == current_user:
            ok+=1
    if ok >= 2:
        for p in react:
            if p.username == current_user:
                ok1+=1
                if (ok1 == ok-1):
                    first = p
                    first_overflew = p.title.overflew
                if ok1 == ok:
                    second = p
                    second_overflew = p.title.overflew
    elif ok == 0:
        first_overflew = 'У вас пока нет ни одной оценки фильма'
        first = {
            'title': 'Нет фильма',
            'like' : 'Нет оценки'
        }
        second_overflew = 'У вас пока нет ни одной оценки фильма'
        second = {
            'title': 'Нет фильма',
            'like' : 'Нет оценки'
        }
    else:
        for p in react:
            if p.username == current_user:
                first = p
                first_overflew = p.title.overflew
        second_overflew = ''
        second = {
            'title': '',
            'like' : ''
        }
    context = {
         'username1':username1,
         'react':react,
         'first':first,
         'first_overflew':first_overflew,
         'second':second,
         'ok':ok,
         'second_overflew':second_overflew,
         'current_user':current_user,
         'film':film
    }
    return render (request,'films/kabinet.html',context=context)
    