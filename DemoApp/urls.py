from django.urls import path
from DemoApp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home,name="hm"),
    path('admins/',views.admins,name="ad"),
    path('dele/',views.delse,name="cds"),
    path('playlist2/',views.cts,name="ctps"),
    path('search/',views.vote,name="vat"),
    path('fetchmovie/',views.vot,name="fetchmovie"),
    path('savemovie/',views.bap,name="bap"),
    path('publicpl/',views.pap,name="pap"),
    path('playlist1/',views.paps,name="pap1"),
    path('playlist3/',views.papt,name="pap2"),
    path('logout/',views.logt,name="logt"),
    path('profile/',views.prof,name="prof"),
    

]
