from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('trade/',views.trade,name="trade"),
    path('trade/buystock/', views.buystock, name="buystock"),
    path('trade/buystock/<str:tid>', views.buystock, name="buystock"),
    path('trade/<str:tid>',views.stocks,name="stocks"),
    path('success/',views.buydata,name="buydata"),
    path('sellstock/',views.sellstock,name="sellstock"),
    path('sellsuccess/',views.selldata,name="selldata"),
    path('activity/',views.activity,name="activity"),
]