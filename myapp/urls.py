from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from.import views

urlpatterns = [
    path('',views.index, name='index'),
    path('item/<int:id>/',views.detail,name='detail'),
    path('category/<int:id>/', views.category_items, name='category_items'),
    
]
