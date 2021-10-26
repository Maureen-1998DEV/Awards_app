from django.conf.urls import url

from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url('^loader/$',views.loader,name = 'loader'),
    url('^search/', views.search_results, name='search_results'),
    url('^signup/$', views.signup, name='signup'),
    url('^comment/(?P<image_id>\d+)', views.comment, name='comment'),
    url('^project/new$', views.new_project, name='new-project'),
    url('^profile/$',views.profile,name='profile'),
    url('^profiles/(\d+)',views.profiles,name='profiles'),
    url('^projects/(\d+)',views.projects,name='projects'),

    url('^edit/profile/$',views.edit_profile,name='edit_profile'),
    # url('^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     views.activate, name='activate'),
    url(r'^api/projects/$', views.ProjectList.as_view()),
    url(r'^api/profiles',views.ProfileList.as_view()),
    url(r'^api/profile/(?P<pk>\d+)',views.ProfileDesc.as_view())
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)