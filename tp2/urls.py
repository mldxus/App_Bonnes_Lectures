from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns 

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

# On "enveloppe" nos URLs habituelles pour qu'elles acceptent le préfixe de langue
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('bonnes_lectures.urls')),
)