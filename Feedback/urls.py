from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'feedback'
urlpatterns = [
    path('', views.FeedbackFormView.as_view(), name='feedback_form'),
    path('success/', views.FeedbackSuccessView.as_view(), name='success'),
    path('list/', views.FeedbackListView, name='feedback_list'),
]
