from django.urls import path  # Import the path function from Django's URL module
from . import views  # Import the views from the current app

urlpatterns = [
    path('', views.home, name='home'),  # URL pattern for the home page, linked to the 'home' view
    path('funding', views.funding, name='funding'),  # URL pattern for the funding page, linked to the 'funding' view
    path('member_info/<str:member_name>', views.member_info, name='member_info'),  # URL pattern for the member info page, accepts a 'member_name' parameter, linked to the 'member_info' view
]
