from django.conf.urls import include, url
from .views import botview
urlpatterns = [
	url(r'^110gfnjfnfggn573894b32c0475743a5b5c7e88bcb78e3cd8a1ff3/?$', botview.as_view()) 
]