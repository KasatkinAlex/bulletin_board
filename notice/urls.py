from django.urls import path
from rest_framework.routers import SimpleRouter

from notice.apps import NoticeConfig
from notice.views import AdsListAPIView, AdsRetrieveAPIView, AdsCreateAPIView, AdsUpdateAPIView, AdsDestroyAPIView, \
    CommentListAPIView, CommentRetrieveAPIView, CommentCreateAPIView, CommentUpdateAPIView, CommentDestroyAPIView

app_name = NoticeConfig.name

router = SimpleRouter()
urlpatterns = [
    path('', AdsListAPIView.as_view(), name='ads_list'),
    path('<int:pk>/', AdsRetrieveAPIView.as_view(), name='ads_detail'),
    path('create/', AdsCreateAPIView.as_view(), name='ads_create'),
    path('<int:pk>/update/', AdsUpdateAPIView.as_view(), name='ads_update'),
    path('<int:pk>/delete/', AdsDestroyAPIView.as_view(), name='ads_delete'),
    path('comment/', CommentListAPIView.as_view(), name='comment_list'),
    path('comment/<int:pk>/', CommentRetrieveAPIView.as_view(), name='comment_detail'),
    path('comment/create/', CommentCreateAPIView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', CommentUpdateAPIView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDestroyAPIView.as_view(), name='comment_delete'),
] + router.urls
