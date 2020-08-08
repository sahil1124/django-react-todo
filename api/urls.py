from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('users',views.UserViewset,basename='user')
urlpatterns = [
    path('',views.apiOverview,name="api-overview"),
    path('task-list/',views.taskList,name='task-list'),
    path('task-detail/<int:pk>/',views.taskDetail,name='task-detail'),
    path('task-create/',views.taskCreate,name='task-create'),
    path('task-update/<int:pk>/',views.taskUpdate,name='task-update'),
    path('task-delete/<int:pk>/',views.taskDelete,name='task-delete'),
    path('',include(router.urls))

]
