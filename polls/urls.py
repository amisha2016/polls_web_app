from django.urls import path
from . import views

app_name= 'polls'                  #Namespacing URL names (https://docs.djangoproject.com/en/4.1/intro/tutorial03/#namespacing-url-names)

urlpatterns= [
        path('', views.index, name='index'),
        path('<int:question_id>/', views.detail, name='detail'),
        path('<int:question_id>/vote/', views.vote, name='vote'),
        path('<int:question_id>/results/>', views.results, name='results'),
        ]

