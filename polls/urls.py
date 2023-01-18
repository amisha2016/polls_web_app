from django.urls import path
from . import views

app_name= 'polls'                  #Namespacing URL names (https://docs.djangoproject.com/en/4.1/intro/tutorial03/#namespacing-url-names)

urlpatterns= [
        path('', views.IndexView.as_view(), name='index'),
        path('<int:pk>/', views.DetailView.as_view(), name='detail'),
        path('<int:question_id>/vote/', views.vote, name='vote'),
        path('<int:pk>/results/>', views.ResultsView.as_view(), name='results'),
        ]

