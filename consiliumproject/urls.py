"""consiliumproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static
from consilium_api.views import *
from consilium_api.models import *


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'travelers', Travelers, 'traveler')
router.register(r'users', Users, 'user')
router.register(r'accommodations', Accommodations, 'accommodation')
router.register(r'rooms', Rooms, 'room')
router.register(r'trips', Trips, 'trip')
router.register(r'travelertrips', TravelerTrips, 'travelertrips')
router.register(r'friends', Friends, 'friend')
router.register(r'flights', Flights, 'flight')
router.register(r'activities', Activities, 'activity')
# router.register(r'tripflights', TripFlights, 'tripflights')
# router.register(r'tripaccommodations', TripAccommodations, 'tripaccommodations')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('register/', register_user),
    path('login/', login_user),
    path('api-token-auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
