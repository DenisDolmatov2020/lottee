from django.contrib import admin
from django.urls import path, include
from number.views import NumberListUpdateView
from tracker.views import TrackerView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/my-user/', include('my_user.urls')),
    path('api/lot/', include('lot.urls')),
    path('api/number/', NumberListUpdateView.as_view(), name='NumberListUpdateView'),
    path('api/tracker', TrackerView.as_view(), name='tracker-view'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
