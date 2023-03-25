from django.contrib import admin
from django.urls import path, include
from doces import views
from doces.views import CategoriaBolosView, home, lista_doce

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doces/', include('doces.urls')),
    path('', views.home, name='home'),
    path('doces/lista/', views.lista_doce, name='lista_doce'),
    path('categoria_bolos/', CategoriaBolosView.as_view(), name='categoria_bolos'),

]
