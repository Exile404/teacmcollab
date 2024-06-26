from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .views import UserViewSet, ProjectViewSet, ProjectMemberViewSet, TaskViewSet, CommentViewSet
from django.urls import path, include
from .views import register_user
from rest_framework_simplejwt.views import TokenObtainPairView

# Create the main router
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)  # Add this line for direct task access
router.register(r'comments', CommentViewSet)

# Create a nested router for tasks and members under projects
projects_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
projects_router.register(r'tasks', TaskViewSet, basename='project-tasks')
projects_router.register(r'members', ProjectMemberViewSet, basename='project-members')

# Create a nested router for comments under tasks
tasks_router = routers.NestedSimpleRouter(router, r'tasks', lookup='task')
tasks_router.register(r'comments', CommentViewSet, basename='task-comments')

# Additional URL patterns
urlpatterns = [
    path('users/register/', register_user, name='register_user'),
    path('users/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]

# Include the routers' URLs
urlpatterns += router.urls
urlpatterns += projects_router.urls
urlpatterns += tasks_router.urls
