from django.shortcuts import render
from django.views.generic import TemplateView

class AddToCart (TemplateView):
    template_name = "order/cart.html"
    def get_context_data(self, **kwargs):
        print(self.POST)
        context = super().get_context_data(**kwargs)
        return context
    
