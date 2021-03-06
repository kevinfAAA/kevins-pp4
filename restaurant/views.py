from django.shortcuts import render
from django.views import generic
from .forms import ReservationsForm
from .models import Reservations
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def index(request):
    return render(request, 'index.html', {})


def menu(request):
    return render(request, 'menu.html', {})


def reserved(request):
    return render(request, 'reserved.html', {})

# booking list class


class BookingsList(ListView):
    model = Reservations
    template_name = 'restaurant/bookings_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bookings'] = Reservations.objects.filter(user=self.request.user)
        return context

# booking detail class


class BookingsDetail(DetailView):
    model = Reservations
    context_object_name = 'booking'
    template_name = 'restaurant/bookings_detail.html'

# create booking class


class BookingsCreate(CreateView):
    model = Reservations
    template_name = 'restaurant/bookings_form.html'
    fields = ('title', 'number_of_guests', 'date', 'time', 'comments')
    success_url = reverse_lazy('bookings')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BookingsCreate, self).form_valid(form)

# update bookings class


class BookingsUpdate(UpdateView):
    model = Reservations
    template_name = 'restaurant/bookings_form.html'
    fields = ('title', 'number_of_guests', 'date', 'time', 'comments')
    success_url = reverse_lazy('bookings')

# delete bookings class


class DeleteView(DeleteView):
    model = Reservations
    template_name = 'restaurant/bookings_delete.html'
    context_object_name = 'booking'
    success_url = reverse_lazy('bookings')
