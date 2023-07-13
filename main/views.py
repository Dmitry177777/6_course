import random
from django import forms
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# from main.forms import forms
from main.models import Client, MailingSetting, Blog, Message, MailingLogs
from main.services import get_category_product


# Create your views here.


class index(LoginRequiredMixin, ListView):
    model = Client
    extra_context = {
        'title': 'Первые продукты'
    }

    # Метод переопределяет представление и выводит только продукты с атрибутом (is_active=True)
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_active=True)
        return queryset[:6]



class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
    extra_context = {
        'title': 'Список постов'
    }

    # Метод переопределяет представление и выводит только продукты с атрибутом is_active=True)
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_publication=True)
        return queryset


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    success_url = reverse_lazy('main:blog_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = context_data['object'].message_heading
        return context_data

    # Обновлени счетчика просмотрове
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Обновлени счетчика просмотрове
        self.object.views_count += 1
        # запись изменений
        self.object.save()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class BlogCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Blog
    fields = ('message_heading', 'message_content', 'message_preview', 'is_publication',)
    success_url = reverse_lazy('main:blog_list')


class BlogUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Blog
    fields = ('message_heading', 'message_content', 'message_preview', 'is_publication',)

    # Получаем данные объекта и выводим ту же страницу
    def get_success_url(self) -> str:
        return reverse_lazy('main:blog_update', kwargs={'pk': self.object.pk})


class BlogDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('main:blog_list')

# class UsersListView(ListView):
#     model=Users
#     extra_context = {
#         'title': 'Список пользователей'
#     }