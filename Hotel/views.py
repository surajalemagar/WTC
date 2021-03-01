from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, DetailView,ListView,UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import render,get_object_or_404,redirect
from .models import HotelInfo
from .forms import HotelForm
from django.db import connection as cn

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
            # getting cleaned data 
            data=form.cleaned_data 
            print(data)
            username=None
            if request.user.is_authenticated:
                username=request.user.username

            # create parts starts from here

            cursor = cn.cursor()
            Name=data['Name']
            Address=data['Address']
            phone_number=data['phone_number']
            number_of_room=data['number_of_room']

            # writing raw queries

            que = "insert into hotel_hotelinfo(Name,Address,phone_number,number_of_room,User) values (%s,%s,%s,%s,%s);"

            # executing raw queries
            cursor.execute(que,[Name,Address,phone_number,number_of_room,username])

            # form.save()
            # return HttpResponseRedirect(reverse_lazy('post:image_display', kwargs={'pk': obj.id}))
            return redirect('/hotel/success/')
        return render(request, self.template_name, {'form': form})


# class HotelBookListView(ListView):
#     model=HotelInfo
#     template_name = 'hotel_book_list.html'

def HotelBookListView(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    cursor=cn.cursor()
    q1="select * from hotel_hotelinfo where User=(%s)"
    cursor.execute(q1,[username])
    data=cursor.fetchall()
    dic={'k1':data}
    return render(request,'hotel_book_list.html',dic)

# class HotelFormDetailView(DetailView):
#     template_name='hotel_form_detail.html'
#     model = HotelInfo

def HotelFormDetailView(request,pk):
    cursor = cn.cursor()
    cursor.execute("select * from hotel_hotelinfo where id=(%s)", [pk])
    data=cursor.fetchone()
    dic={'k1':data}
    return render(request,'hotel_form_detail.html',dic)

# class HotelFormUpdateView(UpdateView):
#     form_class=HotelForm
#     model=HotelInfo
#     template_name='hotel_form_edit.html'
#     success_url='/hotel/update_success'

def HotelFormUpdateView(request,pk):
    cursor = cn.cursor()
    cursor.execute("select * from hotel_hotelinfo where id=(%s)", [pk])
    data = cursor.fetchone()
    dic = {'k1': data}
    return render(request, 'hotel_form_edit.html', dic)

# class HotelFormDeleteView(DeleteView):
#     model=HotelInfo
#     template_name='confirm_delete.html'
#     success_url = '/hotel/list'    

class HotelView(TemplateView):
    template_name = 'hotel.html'


class HotelBookSuccessView(TemplateView):
    template_name = 'success.html'


def UpdateSuccessView(request,pk):
    cursor = cn.cursor()
    Name = str(request.POST['Name'])
    Address = str(request.POST['Address'])
    phone_number = str(request.POST['phone_number'])
    number_of_room = str(request.POST['number_of_room'])
    que = "update hotel_hotelinfo set Name=(%s),Address=(%s),phone_number=(%s),number_of_room=(%s) where id=(%s);"
    cursor.execute(que,[Name,Address,phone_number,number_of_room,pk])
    return render(request, 'update_success.html')

def HotelFormDeleteView(request,pk):
    cursor = cn.cursor()
    q1="delete from hotel_hotelinfo where id=(%s)"
    cursor.execute(q1,[pk])
    return render(request, 'delete_success.html')

class HotelRoyalCentury(TemplateView):
    template_name = 'hotel_royal_century.html'