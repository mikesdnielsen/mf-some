import api.posts.views
import api.users.views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register(r'users', api.users.views.UserViewSet, base_name='user')

router.register(r'posts', api.posts.views.PostViewSet, base_name='post')

router.register(r'likes', api.posts.views.LikeViewSet, base_name='like')

app_name = 'api'
urlpatterns = router.urls
