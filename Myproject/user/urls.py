from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index),
    path('home/',views.index),
    path('about/',views.about),
    path('product/',views.product),
    path('myorder/',views.myorder),
    path('enquiry/',views.enquiry),
    path('signup/',views.signup),
    path('signin/',views.signin),
    path('profile/',views.myprofile),
    path('medicines/',views.medicines),
    path('syrups/',views.syrups),
    path('herbal&skincare/',views.herbal_skincare),
    path('babycare/',views.babycare),
    path('health&nutrition/',views.health_nutrition),
    path('womencare/',views.womencare),
    path('personalcare/',views.personalcare),
    path('ayurveda/',views.ayurveda),
    path('50%OffProduct/',views.PriceLessProduct),
    path('healthdevices/',views.healthdevices),
    path('healthnotes/',views.healthnotes),
    path('healthnote/',views.healthnotes),
    path('viewproduct/', views.viewproduct),
    path('signout/', views.signout),
    path('mcart/', views.mycart),
    path('myordr/', views.myordr),
    path('showcart/', views.showcart),
    path('cpdetail/', views.cpdetail),
    path('search/', views.search), #This URL CAN NOT BE  TYPE IN SEARCH BOX
    path('payment/', views.payment),

    path('',views.index),


]