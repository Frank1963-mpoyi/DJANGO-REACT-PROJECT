# this is how we retrieve user when we create user custom model 
from django.contrib.auth import get_user_model
User = get_user_model() # no need to import User anymore we use our user model we created
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions #by default we nedd to be authenticated in order to access the view
#right now we dont want it 


class SignupView(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def post(self, request, format=None):
        data = self.request.data # data coming from frontend or from the user
        
        name = data['name']
        email = data['email']
        password = data['password']
        password2 = data['password2']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({'error':'Email already exists'})
            else:
                if len(password) < 6:
                    return Response({'error':'Password must be at least 6 characters'})
                else:
                    user = User.objects.create_user(email=email, password=password, name=name)
                    user.save()
                    return Response({'success': 'User created successfully'})
        else:
            return Response ({'error':'Passwords do not match'})

