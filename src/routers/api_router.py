from rest_framework.routers import DefaultRouter

from api import views as views_api


router = DefaultRouter(trailing_slash=False)
router.register('users', views_api.UserView, basename='users')

urlpatterns = router.urls
