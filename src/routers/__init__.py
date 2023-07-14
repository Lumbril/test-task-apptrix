from .main_router import urlpatterns as main
from .yasg_router import urlpatterns as yasg
from .front_router import urlpatterns as front

urlpatterns = main + yasg + front
