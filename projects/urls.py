from django.urls import path
from projects import views
app_name = "projects"
urlpatterns = [
    path('', views.all_projects, name='all_projects'),
    #path('addproject', views.add_project),
    path('<str:title>', views.project_detail, name="project_detail"),
]
