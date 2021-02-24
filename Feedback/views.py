from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from .models import Feedback
from .forms import FeedbackForm
from django.db import connection as cn


class FeedbackFormView(View):
    form_class = FeedbackForm
    initial = {'key': 'value'}
    template_name = 'feedback_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data
            cursor = cn.cursor()
            feedback = data['feedback']
            que = "insert into feedback_feedback(feedback) values (%s);"
            cursor.execute(que, [feedback])
            return redirect('/feedback/success/')
        return render(request, self.template_name, {'form': form})


class FeedbackSuccessView(TemplateView):
    template_name = 'feedback_success.html'


def FeedbackListView(request):
    username = None
    cursor = cn.cursor()
    q1 = "select * from feedback_feedback"
    cursor.execute(q1)
    data = cursor.fetchall()
    dic = {'k1': data}
    return render(request, 'feedback_list.html', dic)
