from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'hotel'
urlpatterns = [
    path('', views.HotelView.as_view(), name='hotel'),
    path('hotel_form/', views.HotelFormView.as_view(), name='hotel_form'),
    path('success/', views.HotelBookSuccessView.as_view(), name='success'),
    path('list/', views.HotelBookListView, name='hotel_book_list'),
    path('<int:pk>/', views.HotelFormDetailView,name='hotel_book_detail'),
    path('<int:pk>/edit/', views.HotelFormUpdateView,name='hotel_book_edit'),
    path('<int:pk>/update_success/', views.UpdateSuccessView, name='update_success'),
    path('<int:pk>/delete/', views.HotelFormDeleteView,name='hotel_book_delete'),
]
