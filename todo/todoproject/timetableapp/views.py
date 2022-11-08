from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import TodoForms
from .models import Timetable
from django import forms
from django.views.generic import ListView, DetailView, UpdateView, DeleteView


class Timetablelistview(ListView):
    model=Timetable
    template_name='home.html'
    context_object_name='task1'

class Timetabledetailview(DetailView):
        model = Timetable
        template_name = 'detail.html'
        context_object_name = 'task4'


class Timetableupdateview(UpdateView):
    model=Timetable
    template_name='update.html'
    context_object_name='task2'
    fields = ['day','task','date']
    def get_success_url(self):
        return reverse_lazy('cbhome')

class Timetabledeleteview(DeleteView):
        model = Timetable
        template_name = 'delete.html'

        success_url=reverse_lazy('cbhome')


def add(request):
    task1 = Timetable.objects.all()
    if request.method == 'POST':
        day = request.POST.get('day','')
        task = request.POST.get('task','')
        date = request.POST.get('date', '')
        timetable=Timetable(day=day,task=task,date=date)
        timetable.save();
        return redirect('detail/')
    return render(request, "home.html", {'task1':task1})

def update(request, id):
    task2=Timetable.objects.get(id=id)
    form=TodoForms(request.POST or None, request.FILES, instance=task2)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, "update.html",{'form':form, 'task2':task2})

def detail(request):
   task4=Timetable.objects.all()
   return render(request,'detail.html',{'task4':task4})

def delete(request, id):
    if request.method == 'POST':
        task3=Timetable.objects.get(id=id)
        task3.delete()
        return redirect('/')
    return render(request, "delete.html")