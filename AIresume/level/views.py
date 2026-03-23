
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Resume
from .serializers import Resumeserializer
# Create your views here.
@api_view(['POST'])
def create_resume(request):
    serializer=Resumeserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
@api_view(['GET'])
def get_resume(request,id):
    try:
        resume=Resume.object.get(id=id)
    except Resume.DoesNotExist:
        return Response({'error': 'resume does not found '})
    serializer=Resumeserializer(resume)
    return Response(serializer.data)
@api_view(['POST'])
def save_answers(request,id):
    try:
        resume=Resume.object.get(id=id)
    except Resume.DoesNotExist:
        return Response({"error":"resume not found"})
    resume.answers=request.data.get('answers')
    resume.save()
    return Response({"message":"Answers saved"})