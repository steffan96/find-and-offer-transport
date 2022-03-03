from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .models import ChatBox, Message
from accounts.models import CustomUser
from .forms import MessageForm


@login_required
def chat(request, receiver):
    form = MessageForm(request.POST or None)
    chat_receiver = CustomUser.objects.get(id=receiver)
    
    #display chat
    if request.method == "GET":
      chat = ChatBox.objects.filter(Q(user1=request.user, user2=chat_receiver) \
      | Q(user2=request.user, user1=chat_receiver)).first()
      if not chat:   
        chat = ChatBox.objects.create(user1=request.user, user2=chat_receiver)
      all_messages = Message.objects.filter(chat=chat).all()

      # seen functionality
      msg = Message.objects.filter(chat=chat).first() # get the last message sent
      try:
        if msg.sender != request.user:
          each_message = Message.objects.filter(Q(chat=chat) & 
          ~Q(sender=request.user)).all()
          for m in each_message:
            m.seen = True
            m.save()
      except:
        pass

    # send message
    
    elif request.method == 'POST':
      form = MessageForm(request.POST or None)
      chat1 = ChatBox.objects.filter(Q(user1=request.user, user2=chat_receiver) \
      | Q(user2=request.user, user1=chat_receiver)).first()
      
      if form.is_valid():
        new_message = form.save(commit=False)
        new_message.chat = chat1
        new_message.sender = request.user
        new_message.receiver = chat_receiver
        new_message.save()
        return redirect('posts:home')
    
    context = {
      'form': form,
      'all_messages': all_messages,
      'chat_receiver': chat_receiver,
      }
    return render(request, 'chat/chat.html', context)


class InboxView(LoginRequiredMixin, ListView):
  model = ChatBox
  template_name = 'chat/inbox.html'

  def get_queryset(self):
    # getting all chats for request.user
    object_list = ChatBox.objects.filter(Q(user1=self.request.user) \
    | Q(user2=self.request.user)).all()
    return object_list
  
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        # use 'pk' of a user to get the number of unseen messages
        context['pk'] = pk
        return context
  


  
