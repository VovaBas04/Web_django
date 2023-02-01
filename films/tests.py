from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('http://127.0.0.1:8000')
        self.assertEqual(response.status_code, 200)

    def test_about_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('http://127.0.0.1:8000/about')
        self.assertEqual(response.status_code, 301)

    def test_login_loads_properly(self):
        response = self.client.get('http://127.0.0.1:8000/login')
        self.assertEqual(response.status_code, 301)

    def test_register_loads_properly(self):
        response = self.client.get('http://127.0.0.1:8000/register')
        self.assertEqual(response.status_code, 301)

class FilmTestCase(TestCase):
    def setUp(self):
        Film.objects.create(title='Секретная служба Санта-Клауса',overflew='Каждое Рождество Санта и его огромная армия высококвалифицированных эльфов производят подарки и разносят их по всему миру за одну ночь. Однако, когда один из 600 миллионов детей, получивших подарок от Санты в канун Рождества, отсутствует, это считается «приемлемым» для всех, кроме одного — Артура. Артур Клаус — сын-неудачник Санты, который выполняет несанкционированную миссию новичка, чтобы до рассвета рождественским утром доставить последний подарок на полпути вокруг земного шара.',director='Темыч',soup = '1')
    def test_film_database(self):
        Avatar = Film.objects.get(title='Секретная служба Санта-Клауса')
        self.assertEqual(Avatar.ovr(),'Каждое Рождество Санта и его огромная армия высококвалифицированных эльфов производят подарки и разносят их по всему миру за одну ночь. Однако, когда один из 600 миллионов детей, получивших подарок от Санты в канун Рождества, отсутствует, это считается «приемлемым» для всех, кроме одного — Артура. Артур Клаус — сын-неудачник Санты, который выполняет несанкционированную миссию новичка, чтобы до рассвета рождественским утром доставить последний подарок на полпути вокруг земного шара.')

class ReactionTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='Aboba',password='qwerty123')
        Film.objects.create(title='Секретная служба Санта-Клауса',overflew='Каждое Рождество Санта и его огромная армия высококвалифицированных эльфов производят подарки и разносят их по всему миру за одну ночь. Однако, когда один из 600 миллионов детей, получивших подарок от Санты в канун Рождества, отсутствует, это считается «приемлемым» для всех, кроме одного — Артура. Артур Клаус — сын-неудачник Санты, который выполняет несанкционированную миссию новичка, чтобы до рассвета рождественским утром доставить последний подарок на полпути вокруг земного шара.',director='Темыч',soup='1')
        user = User.objects.get(username='Aboba')
        film = Film.objects.get(title='Секретная служба Санта-Клауса')
        Reaction.objects.create(username = user,title = film,like='Понравилось',recsys=0)

    def test_reaction_database(self):
        Choise = Reaction.objects.get(id = 1)
        self.assertEqual(Choise.likes(),'Понравилось')

        