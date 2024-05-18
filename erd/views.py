from .Serializers import pSerializers,ESerializers,RSerializers,DOSerializers,DSerializers,MSerializers,RegisterSerializers
from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .models import patient,Escort,Medicine,Diseases,Document,Reminder,Register
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response


class GetRegister(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializers

# class GetLogin(viewsets.ModelViewSet):
#     queryset = Login.objects.all()
#     serializer_class = LoginSerializers


    

class GetPatient(viewsets.ModelViewSet):
    queryset = patient.objects.all()
    serializer_class = pSerializers
    # def get_extra_actions(self):
    #     return []

class GetEscort(viewsets.ModelViewSet):
    queryset = Escort.objects.all()
    serializer_class = ESerializers

class GetReminder(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = RSerializers

class GetDocument(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DOSerializers

class GetMedicine(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MSerializers

class GetDiseases(viewsets.ModelViewSet):
    queryset =Diseases.objects.all()
    serializer_class = DSerializers






# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.decorators import api_view






# @api_view(['POST'])
# def showmultiplemodels(request):
#     patientt=patient.objects.all()
#     Escortt=Escort.objects.all()
#     ppSerializers=pSerializers(patientt,many=True)
#     EESerializers=ESerializers(patientt,many=True)
#     Resultmodel=ppSerializers.data+EESerializers.data
#     return JsonResponse(Resultmodel)
    
# @csrf_exempt
# @api_view(['POST'])
# def Login(request):
#     if request.method == 'POST':
#         Userhandel = request.POST.get('Userhandel')
#         Password = request.POST.get('Password')

#         # Perform authentication and database operations as needed
#         # ...

#         return JsonResponse({'message': 'Login successful'})
#     return JsonResponse({'message': 'Invalid request method'})



class RegisterList(generics.ListAPIView):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializers
    def get_extra_actions(self):
        return []

    @swagger_auto_schema(responses={
        200: RegisterSerializers(many=True)
    })
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    
# class LoginList(generics.ListAPIView):
#     queryset = Login.objects.all()
#     serializer_class = LoginSerializers
#     def get_extra_actions(self):
#         return []

#     @swagger_auto_schema(responses={
#         200: LoginSerializers(many=True)
#     })
#     def get(self, request, *args, **kwargs):
#         return super().get(request, *args, **kwargs)
    from rest_framework import status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import CreateAPIView

# class LoginList(CreateAPIView):
#     serializer_class = LoginSerializers

#     @swagger_auto_schema(responses={200: LoginSerializers(many=True)})
#     def post(self, request, *args, **kwargs):
#         return super().post(request, *args, **kwargs)


    
class PatientList(generics.ListAPIView):
    queryset = patient.objects.all()
    serializer_class = pSerializers
    def get_extra_actions(self):
        return []

    @swagger_auto_schema(responses={
        200: pSerializers(many=True)
    })
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class EscortList(generics.ListAPIView):
    queryset = Escort.objects.all()
    serializer_class = ESerializers

    @swagger_auto_schema(responses={
        200: ESerializers(many=True)
    })
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class ReminderList(generics.ListAPIView):
    queryset = Reminder.objects.all()
    serializer_class = RSerializers

    @swagger_auto_schema(responses={
        200: RSerializers(many=True)
    })
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class DiseasesList(generics.ListAPIView):
    queryset = Diseases.objects.all()
    serializer_class = DSerializers

    @swagger_auto_schema(responses={
        200: DSerializers(many=True)
    })
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class DocumentList(generics.ListAPIView):
    queryset = Document.objects.all()
    serializer_class = DOSerializers

    @swagger_auto_schema(responses={
        200: DOSerializers(many=True)
    })
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class MedicineList(generics.ListAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MSerializers

    @swagger_auto_schema(responses={
        200: MSerializers(many=True)
    })
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
