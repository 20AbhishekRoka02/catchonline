from django.urls import path,include
    # path('admin/', admin.site.urls),
from . import views

urlpatterns = [
    # path('', views.ApiOverview, name='home'),
    path('create/', views.add_query, name='add-query'),
    path('testcreate/', views.add_test_query, name='add-test-query'),
]