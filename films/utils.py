from .models import *
 
menu = [{'title':"О сайте",'url_name':"about"},
        { 'title':"Войти",'url_name':'login'}, 
        {'title':"Подбор рекомендаций",'url_name':'home'},
]
class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context