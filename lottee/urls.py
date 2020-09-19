from django.contrib import admin
from django.urls import path, include
from django.urls import path
from number.views import NumberListUpdateView
from tracker.views import TrackerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/my-user/', include('my_user.urls')),
    path('api/lot/', include('lot.urls')),
    path('api/number/<int:pk>/', NumberListUpdateView.as_view(), name='NumberListUpdateView'),
    path('api/tracker', TrackerView.as_view(), name='tracker-view'),
]
