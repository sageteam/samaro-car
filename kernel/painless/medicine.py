from django.conf import settings
from django.http import JsonResponse
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.mail import BadHeaderError
from django.template.loader import render_to_string

class Treatment():
    succeed = True
    failed = False
    data = dict()
    
    def __init__(self, *args, **kwargs):
        pass

    def load_partial(self, request, template_name, type, *args, **kwargs):

        context = { 
            'type': type
        }
        
        for key, value in kwargs.items():
            context[key] = value

        self.data['html_markup'] = render_to_string(
            template_name,
            context = context,
            request = request
        )

        if type == 'email':
            return self.data['html_markup']
        else:
            return JsonResponse(self.data)

treatment = Treatment()