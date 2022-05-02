from django.urls import path

from .views import InboxView, chat

urlpatterns = [
    path("chat/<int:receiver>", chat, name="chat"),
    path("inbox/<int:pk>", InboxView.as_view(), name="inbox"),
]


app_name = "chat"
