from django.test import TestCase

# Create your tests here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView
from django.urls import reverse, reverse_lazy
from .models import HotelInfo
from .forms import HotelForm


class HotelFormView(View):
    form_class = HotelForm
    initial = {'key': 'value'}
    template_name = 'hotel_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            # return HttpResponseRedirect(reverse_lazy('post:image_display', kwargs={'pk': obj.id}))
            return redirect('/hotel/success/')
        return render(request, self.template_name, {'form': form})



class SuccessView(TemplateView):
    template_name = 'success.html'


class HotelView(TemplateView):
    template_name = 'hotel.html'

