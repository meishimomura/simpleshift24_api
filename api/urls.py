from django.urls import path, include
from rest_framework import routers
from .views import ProfileViewSet, StaffViewSet, ShiftViewSet, CreateUserView, ListUserView, LoginUserView

router = routers.DefaultRouter()
router.register('profile', ProfileViewSet)
router.register('staff', StaffViewSet)
router.register('shift', ShiftViewSet)

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('users/', ListUserView.as_view(), name='users'),
    path('loginuser/', LoginUserView.as_view(), name='loginuser'),
    path('', include(router.urls)),
]