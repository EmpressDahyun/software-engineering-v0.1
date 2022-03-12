from django.urls import path
from stellaris import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "stellaris"

urlpatterns = [
    path('', views.HomeView, name="home"),
    path('category/', views.CategoryView, name="categories"),
    path('category/<str:slug>', views.MenuView, name="menu"),
    path('gallery/', views.GalleryView, name="gallery"),
    path('location/', views.LocationView, name="location"),
    path('party_category/', views.PartyCategoryView, name="party_category"),
    path('party_category/<str:slug>', views.PartyMenuView, name="party_menu"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
