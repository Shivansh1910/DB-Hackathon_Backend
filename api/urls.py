from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('users/', views.getUsers),
    path('user/', views.getUser),

    path('loginUser/', views.loginUser),
    path('getUserFromToken/', views.getUserFromToken),
    path('getUserBooks/', views.getUserBooks),
    path('getAllTradeByBook/', views.getAllTradeByBook),
    path('reportTrade/', views.reportTrade),
    path('addToWatchlist/', views.addToWatchlist),
    path('deleteFromWatchlist/', views.deleteFromWatchlist),
    path('getAllTradeByWatchList/', views.getAllTradeByWatchList),
    path('getAllSecurities/', views.getAllSecurities),
    path("dashboard/", views.dashboard),
    path('searchRelatedSecutity/', views.searchRelatedSecutity),
]
