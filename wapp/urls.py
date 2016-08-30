from django.conf.urls import url
from wapp import views

urlpatterns = [
	url(r'^$', views.upload_file, name='upload_file')
]