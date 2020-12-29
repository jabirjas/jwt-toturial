from django.urls import path
from snippets import views

# urlpatterns = [
#     path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>/', views.snippet_detail),
# ]

# urlpatterns = [
#     path('snippets/', views.SnippetList.as_view()),
#     path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
# ]


urlpatterns = [
    path('snippets/', views.ShowSnippets, name='snippets'),
    path('snippets/insert/', views.AddSnippets, name='add new snippets'),
    path('snippets/update/<int:pk>/', views.EditSnippets, name='edit snippets'),
    path('snippets/delete/<int:pk>/', views.DeleteSnippets, name='delete snippets'),
]