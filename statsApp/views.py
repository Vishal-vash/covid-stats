from django.http import HttpResponse
from django.shortcuts import render
import json
# Create your views here.
from django.views import generic

from .models import Stats


def index(request):
    return HttpResponse("Hello from stats app.")


class IndexView(generic.ListView):
    template_name = 'statsApp/index.html'
    context_object_name = 'country_stats_list'

    def get_queryset(self):
        return Stats.objects.order_by('-cases')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        country_names = Stats.objects.values_list('country', flat=True).order_by('-cases')[:10]
        country_cases = Stats.objects.values_list('cases', flat=True).order_by('-cases')[:10]
        country_active = Stats.objects.values_list('active', flat=True).order_by('-cases')[:10]
        country_recovered = Stats.objects.values_list('recovered', flat=True).order_by('-cases')[:10]
        country_deaths = Stats.objects.values_list('deaths', flat=True).order_by('-cases')[:10]
        country_critical = Stats.objects.values_list('critical', flat=True).order_by('-cases')[:10]
        country_names = list(country_names)
        country_cases = list(country_cases)
        country_active = list(country_active)
        country_recovered = list(country_recovered)
        country_deaths = list(country_deaths)
        country_critical = list(country_critical)
        print(country_active)
        print(country_recovered)
        context['country_name_list'] = country_names
        context['country_case_list'] = country_cases
        context['country_active_list'] = country_active
        context['country_recovered_list'] = country_recovered
        context['country_deaths_list'] = country_deaths
        context['country_critical_list'] = country_critical
        return context


class CountryView(generic.DetailView):
    model = Stats
    template_name = 'statsApp/country.html'
    context_object_name = 'country'

    def get_context_data(self, **kwargs):
        context = super(CountryView, self).get_context_data(**kwargs)
        for key, value in context.items():
            country_stat = value
        print(context.items())
        return context