from django.urls import path
from snippets import views
from rest_framework . urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippets/', views.snippet_list),           # For listing snippets and creating new snippets
    path('snippets/<int:pk>/', views.snippet_detail) # For retrieving, updating, or deleting individual snippets
]

urlpatterns = format_suffix_patterns ( urlpatterns )

