from api.views.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)

router.register(r'post', PostViewSet, basename='post')

router.register(r'comment', CommentViewSet, basename='comment')

urlpatterns = router.urls