# Create a django project
django-admin startproject {your project name}
python3 manage.py migrate
python3 manage.py createsuperuser

# Changing code
getting into setting.py, changed the following 
* You need to add the app name here once you installed something
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'language',
]

# setting urls
* change the following into 
from django.urls import path, include
* add app's path into this urls.py (it collects all pathes you will use in the app)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('language.urls'))
]

# creating urls.py in language app
from django.urls import path, include
urlpatterns = [
    
]

# create your first model
* as showing in language/models.py
* you need to add new migration before migrate database
python3 manage.py makemigrations 
python3 manage.py migrate
* then enter language/admin.py, add 
from .models import Language
admin.site.register(Language)
* then you can find your new model Language here.

# Build your restful api 
* creating language/seralizers.py and 
from rest_framework import serializers
from .models import Language

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name', 'program')

# Then in the language/views.py
from rest_framework import viewsets
from .models import Language
from .serializers import LanguageSerializer

class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

# back to urls.py in language app
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('language', views.LanguageView)

urlpatterns = [
    path('', include(router.urls))
]

# you can change the admin view in the model
def __str__(self):
    '''just returns name in the admin '''
    return self.name

# Running your server
python3 manage.py runserver
check localhost:8000, and admin

############################## some key ideas ##############################
when you are trying to make some models (language here) into api, only modifing 
serializers.py in your Language package.

