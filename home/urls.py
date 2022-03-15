
from django.urls import path,include
from home.views import access, accessTem,search,account_infomation,get_userss,get_spins_viewss
urlpatterns = [
    path('',access ),
    path('template/',accessTem ),
    path('search/',search ),
        path('account/',account_infomation ),
         path('get_users/',get_userss ),
          path('get_spins_views/',get_spins_viewss ),



]
