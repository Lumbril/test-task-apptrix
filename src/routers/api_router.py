from rest_framework.routers import DefaultRouter

from api import views as views_api


router = DefaultRouter(trailing_slash=False)
router.register('clients/create', views_api.UserCreateView, basename='users')
router.register('clients', views_api.UserMatchView, basename='user_match')

urlpatterns = router.urls
