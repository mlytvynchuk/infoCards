from django.urls import path,include
from cards import views as cards_views
urlpatterns = [
    path('',cards_views.home,name ="cards-home"),
    path('card/<str:slug>/', cards_views.card_details, name="card-details"),
    path('tags/',cards_views.tags_list,name="tags_list"),
]
