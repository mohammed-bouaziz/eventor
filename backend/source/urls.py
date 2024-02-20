
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView

)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Create, Update, List, Delete Users
    path('api/users/', include('users.urls')),

    # Create, Update, List, Delete Events
    path('api/events/', include('events.urls')),

    #CRUD Locations
    path('api/locations/', include('locations.urls')),

    #CRUD Services
    path('api/services/', include('services.urls')),

    #CRUD Invitations
    path('api/invitations/', include('invitations.urls')),

    #Authentication: Log-in, Log-out, Verify if logged in
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
