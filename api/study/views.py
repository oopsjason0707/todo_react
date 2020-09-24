from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, action
from .models import Students
from .serializers import StudentSerializer
from rest_framework.response import Response
from .serializers import ScoreSerializer
from .models import Scores
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# ViewSet 
class Studentview(viewsets.ModelViewSet):  
    queryset = Students.objects.all()
    serializer_class = StudentSerializer  

    def get_query(self):
        qs = super().get_queryset()
        name = self.request.query_params.get('name')
        if name:
            qs = qs.filter(name=name)
        return qs


    @action(detail=False, methods=['GET'])
    def incheon(self, request):
        qs = self.get_queryset().filter(address_contains='인천')  # like '%인천%'
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['PUT'])
    def init(self, request, pk):
        instance = self.get_object()  # pk 로 넣은 인스텐스를 받아서 초기화 시켜서 받은 값을 serializer로 해주는것
        instance.address = ''
        instance.email = ''
        instance.save(update_fields=['address', 'email'])
        serializer=self.get_serializer(instance)
        return Response(serializer.data)

class Scoreview(viewsets.ModelViewSet):
    queryset = Scores.objects.all()
    serializer_class = ScoreSerializer





@api_view(['GET', 'POST'])
def StudentBasicView():
    if request.method == 'GET':
        students = Students.objects.all()
        serializer = StudentBasicSerializer(student, many=True)
        return Response(serializer.data)



@api_view(['PUT'])
def StudentDetailBasicView(request, pk):
    if request.method == 'PUT':
        student = Students.objects.get(pk=pk)
        # student 원래데이터
        # request.data 사람이 보내준 데이터
        # (원래데이터 <-- 사람이 보내준 데이터) --> SAVE
        serializer = StudentBasicSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(Serializer.errors, status=400)






# class StudentView(APIView):
#     def get(self, request):
#         qs = Students.objects.all()  #조회를 한 다음에
#         serializer = StudentSerializer(qs, many=True)
#         return Response(Serializer.data)

#     def post(self, request):
#         serializer = ScoreSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class StudentDetailView(APIView):
#     def get_object(self, pk):
#         return get_object_or_404(Students, pk=pk)
    
#     def get(self, request, pk):
#         qs = self.get_object(pk)
#         serializer = StudentSerializer(qs)
#         return Response(serializer.data)

# class ScorView(APIView):
#     def get(self, request):
#         score = Scores.objects.all() # 메모리에 있는 거
#         # 메모리에서 어떻게 보내지? 메모리에 있는 object --> 텍스트로 변환해서 보내주는것이 serialize(직렬화)
#         serializer = ScoreSerializer(score, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ScoreSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)



# class ScoreDetailView(APIView):

    
#     def get_object(self,id):
#         score = self.getobject(id)
#         serializer = ScoreSerializer(score)
#         return Response(serializer.data)

#     def get(self, request, id):
#         score = self.get_object(id)
#         serializer = ScoreSerializer(score, data=request.data)
#         if serializer.is_valid:
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)

#     def delete(self, request, id):
#         score = self.get_object(id)
#         score = delete()
#         return Response(status=status=204)


# @api_view(['GET', 'POST'])
# def StudentView(request):  #student모델을 가져와서 
    
#     if request.method =='GET':
#         qs = Students.objects.all()  #student studentmodel을 읽었고
#         serializer = StudentSerializer(qs, many=True)  #(위에 objects.get이면 밑에 null=False)
#         return Response(serializer.data)   #view 까지 만들면 urls.py를 만든다
#     elif request.method == 'POST':
#         # 직렬화 생성
#         serializer = StudentSerializer(data=request.data)
#         # validitation 체크 
#         if serializer.is_valid():  # 저장
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)  # 저장한 데이터가 리턴
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET', 'PUT', 'DELETE'])
# def StudentDetailView(request, id):

#     qs = get_object_or_404(Students, pk=id)
#     # 상세조회
#     if request.method == 'GET':
#         qs = Students.objects.get(pk=id)
#         serializer = StudentSerializer(qs)
#         return Response(serializer.data)
        
#     # 수정
#     elif request.method == 'PUT':
#         serializer = StudentSerializer(qs, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)  # 오류가 났을때 '잘못보냈어'라고 해주는 기능

#     #삭제
#     elif request.method == 'DELETE':
#         qs.delete()
#         return Response(status=204)


# # Scores 조회수정삭제기능
# @api_view(['GET', 'PUT', 'DELETE'])
# def ScoreDetailView(request, id):
    
#     qs = get_object_or_404(Scores, pk=id)

#     # 스코어 상세조회
#     if request.method == 'GET':
        
#         serializer = ScoreSerializer(score)
#         return Response(serializer.data)
       
#     # 스코어 수정
#     elif request.method == 'PUT':
#         serializer = ScoreSerializer(score, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)  #오류가 났을때


#     # 삭제 
#     elif request.method == 'DELETE':
#         qs.delete()
#         return Response(status=204)







# @api_view(['GET', 'POST'])
# def ScoreView(request): #Score 모델을 가져와서
#     if request.method == 'GET':

#         qs = Scores.objects.all() #Scoremodel을 읽고
#         serializer = ScoreSerializer(qs, many=True)
#         return Response(serializer.data) #view 까지 만들어서 urls.py를 만든다.

#     elif request.method == 'POST':
#         # 직렬화 생성, 딕셔너리 비슷한 형태
#         serializer = ScoreSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         Response(serializer.errors, status=400)