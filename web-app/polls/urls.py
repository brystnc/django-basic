from django.urls import path
from . import views  # . == polls

app_name = "polls"
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/detail/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultView.as_view(), name='result'),
    # ex: /polls/5/vote
    path('<int:pk>/vote/', views.vote, name='vote'),
]

# urlpatterns = [
#     # ex: /polls/
#     path('', views.index, name='index'),
#     # ex: /polls/5/
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='result'),
#     # ex: /polls/5/vote
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]
