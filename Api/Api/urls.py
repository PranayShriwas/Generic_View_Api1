from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('emp.urls')),
    path('product/', include('Product.urls')),
    path('user/', include('user.urls')),
    path('student/', include('student.urls'))
]
