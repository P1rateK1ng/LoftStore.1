from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from users.views import MyObtainTokenPairView

# router = routers.DefaultRouter()
#
# router.register('cart', carts.views)

urlpatterns = [
    path('admin/', admin.site.urls),

    # My app urls
    path('products/', include('products.urls')),
    path('users/', include('users.urls')),
    path('orders/', include('orders.urls')),
    path('auth/', include('auth.urls')),
    path('carts/', include('carts.urls')),

    #  jwt token urls
    # path('token/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # ckeditor urls
    path('ckeditor/', include('ckeditor_uploader.urls'))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)