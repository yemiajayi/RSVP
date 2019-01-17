from django.views import generic
from django.views.generic import View
from .forms import RsvpForm
from .models import RSVP
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
class CheckList(generic.ListView):
    template_name = 'check_list.html'
    context_object_name = 'all_rsvp'

    def get_queryset(self):
        return RSVP.objects.all()


class CreateRsvp(View):
    template_name = 'rsvp_form.html'
    form_class = RsvpForm

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'We have received your response. Thanks!')
            return redirect('create_rsvp')

