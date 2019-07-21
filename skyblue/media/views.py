from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from media.forms import MediaEntryForm
from media.models import MediaEntry
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

class MediaEntryList(ListView):
    model = MediaEntry
    context_object_name = 'media_entries'
    paginate_by = 7
    
    # In case we need to define new dictionary elements
    # in the context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class MediaEntryDetail(DetailView):
    model = MediaEntry
    context_object_name = 'media_entry'

class MediaEntryCreate(LoginRequiredMixin, CreateView):
    model = MediaEntry
    form_class = MediaEntryForm

    def get_login_url(self):
        login_url = reverse_lazy('user:login')

        return login_url

    def form_valid(self, form):
        media = form.save()
        media.author = self.request.user
        media.save()
        return HttpResponseRedirect(reverse_lazy('media:media-detail', kwargs = {
            'pk': media.id
        }))

class MediaEntryUpdate(LoginRequiredMixin, UpdateView):
    model = MediaEntry
    form_class = MediaEntryForm

    def form_valid(self, form):
        media = form.save()
        media.save()
        return HttpResponseRedirect(reverse_lazy('media:media-detail', kwargs = {
            'pk': media.id
        }))

class MediaEntryDelete(LoginRequiredMixin, DeleteView):
    model = MediaEntry
    success_url = reverse_lazy('media:media-list')

class MyPosts(View):
    template_name='media/user_posts.html'

    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        medias = MediaEntry.objects.all().filter(author=user)

        context = {
            'medias': medias,
            'user_viewed': user
        }

        return render(request, self.template_name, context)
