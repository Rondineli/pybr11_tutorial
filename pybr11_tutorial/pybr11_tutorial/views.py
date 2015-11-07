# -*- coding: utf-8 -*-
import os

from django.views.generic import TemplateView


class PythonViewTuto(TemplateView):
    template_name = 'pybr11_tutorial/index.html'

    def get_context_data(self, **kwargs):
        context = super(PythonViewTuto, self).get_context_data(**kwargs)
        context['environments_keys'] = os.environ.keys()
        context['environments_values'] = os.environ.values()
        return context


class HealthCheck(TemplateView):
    template_name = 'pybr11_tutorial/health.html'
