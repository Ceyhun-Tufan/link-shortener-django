from django.urls import path

from .views import ShortLinkCreate, ShortLinkRetrieve, RedirectShortLink,home

urlpatterns = [
    path('create/', ShortLinkCreate.as_view(), name='shortlink-list-create'),
    path('retrieve/', ShortLinkRetrieve.as_view(), name='shortlink-detail'),
    path('<str:short_url>/', RedirectShortLink.as_view(), name='shortlink-redirect'),
    path("",home,name="home")
]
