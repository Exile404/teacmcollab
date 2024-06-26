from django.contrib import admin
from .models import User, Project, ProjectMember, Task, Comment

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'date_joined']
    search_fields = ['username', 'email']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'owner', 'created_at']
    search_fields = ['name', 'description']
    list_filter = ['owner']

@admin.register(ProjectMember)
class ProjectMemberAdmin(admin.ModelAdmin):
    list_display = ['project', 'user', 'role']
    search_fields = ['project__name', 'user__username', 'role']
    list_filter = ['role']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'status', 'priority', 'assigned_to', 'project', 'created_at', 'due_date']
    search_fields = ['title', 'description']
    list_filter = ['status', 'priority', 'project']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'user', 'task', 'created_at']
    search_fields = ['content', 'user__username']
    list_filter = ['task']
