from django.urls import path

from hello_app.views import HelloWorldView, HelloView

urlpatterns = [
    path('world/', HelloWorldView.as_view(), name='hello_world'),
    path('<str:name>/', HelloView.as_view(), name='hello_person'),
]