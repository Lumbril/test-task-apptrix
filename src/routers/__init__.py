from .main_router import urlpatterns as main
from .yasg_router import urlpatterns as yasg

urlpatterns = main + yasg
