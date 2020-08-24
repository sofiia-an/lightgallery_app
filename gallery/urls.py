from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('', views.imagedisplay),
    path('', views.IndexView,name="home"),
    path('dashboard/', views.dashboardView, name="dashboard"),
    path('login/',LoginView.as_view(),name="login_url"),
    path('register/',views.registerView,name="register_url"),
    path('logout/',LogoutView.as_view(next_page="dashboard"),name="logout"),
    path('searchbar', views.searchbar,name='searchbar'),

]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

