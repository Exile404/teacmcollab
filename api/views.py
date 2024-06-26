from rest_framework import viewsets
from .models import User, Project, ProjectMember, Task, Comment
from .serializers import UserSerializer, ProjectSerializer, ProjectMemberSerializer, TaskSerializer, CommentSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, serializers
from django.contrib.auth.hashers import make_password


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectMemberViewSet(viewsets.ModelViewSet):
    queryset = ProjectMember.objects.all()
    serializer_class = ProjectMemberSerializer

    def create(self, request, *args, **kwargs):
        project_id = kwargs.get('project_pk')
        if not project_id:
            return Response({"error": "Project ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        request.data['project'] = project_id
        return super().create(request, *args, **kwargs)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()  # Add this line
    serializer_class = TaskSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        project_pk = self.kwargs.get('project_pk')
        if project_pk:
            return Task.objects.filter(project_id=project_pk)
        return super().get_queryset()

    def perform_create(self, serializer):
        project_pk = self.kwargs.get('project_pk')
        if not project_pk:
            raise serializers.ValidationError({"project": "Project ID is required"})
        serializer.save(project_id=project_pk)



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        task_pk = self.kwargs.get('task_pk')
        if task_pk:
            return Comment.objects.filter(task_id=task_pk)
        return super().get_queryset()



@api_view(['POST'])
def register_user(request):
    data = request.data
    data['password'] = make_password(data['password'])
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)