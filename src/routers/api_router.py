from rest_framework.routers import DefaultRouter

from api import views as views_api


router = DefaultRouter(trailing_slash=False)
router.register('clients/create', views_api.UserCreateView, basename='users')

urlpatterns = router.urls
