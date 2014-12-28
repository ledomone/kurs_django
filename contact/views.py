from django.contrib.contenttypes import fields
from django.shortcuts import render

from .forms import MessageForm, ContactForm
from django.views.generic import DetailView, ListView, FormView


class MessageAddView(FormView):
    # form_class = MessageForm
    form_class = ContactForm
    template_name = 'contact/message_form.html'
    success_url = '/'

    # def form_valid(self, form):
    #     form.save()  # bo...
    #     return super(MessageAddView, self).form_valid(form)