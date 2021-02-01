from rest_framework import permissions
from rest_framework.views import APIView
from .models import Contact
from django.core.mail import send_mail
from rest_framework.response import Response



class ContactCreateView(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def post(self, request, format=None):
        data = self.request.data # here is to retrieve data from backend
        
        try:
            send_mail(
                data['subject'],
                'Name: '
                +data['name']
                +'\nEmail: '
                +data['Email']
                +'\n\nMessage: \n'
                +data['message'],
                'frankmpoyi63@gmail.com',
                {'frankmpoyi63@gmail.com'},
                fail_silently= False
                
            )
            contact = contact(name=data['name'], email=data['email'], subject=data['subject'], message=data['message'])
            contact.save()
            return Response({'success': 'Message sent successfully'})   
        except:
            return Response ({'error':'Message failed to send'})
