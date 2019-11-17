
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from pages import views
from django.contrib.sitemaps.views import sitemap
from pages.sitemap import StaticViewsSitemap
sitemaps ={
    'static': StaticViewsSitemap
}




urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^ads\.txt',views.ads,name='ads'),
    path('about',views.about,name='about'),
    path('sitemap.xml',sitemap,{'sitemaps':sitemaps}),
    path('ccat',views.ccat,name='ccat'),
    path('C-CAT-2019-Predac-Course',views.crashcourse,name='C-CAT-2019-Predac-Course'),
    path('cdac',views.cdac,name='cdac'),
    path('ccee',views.ccee,name='ccee'),
    path('test',views.test,name='test'),
    path('search',views.search,name='search'),
    path('rank',views.rank,name='rank'),
    path('payment/',include('payment.urls')),
    path('OnlineTest/',include('OnlineTest.urls')),
    path('accounts/',include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('interview',views.interview,name='interview'),
    path('notify',views.notify,name='notify'),
    path('ccat_notify',views.ccat_notify,name='ccat_notify'),
    path('questions',views.questions,name='questions'),
    path('ccat_questions',views.ccat_questions,name='ccat_questions'),
    path('previous',views.prev_questions,name='previous'),
    path('CPP/',include('CPP.urls')),
    path('C/',include('C.urls')),
    path('English-Tutorial',views.eng,name='English-Tutorial'),
    path('dac_interview',views.dac_interview,name='dac_interview'),
    path('big_data_interview',views.bd_interview,name='big_data_interview'),
    path('Aptitude-Tutorial',views.apti,name='Aptitude-Tutorial'),
    path('C-CPP-Objective-Questions',views.section_b,name='C-CPP-Objective-Questions'),
    path('C-CPP-Programming-Questions',views.coding,name='C-CPP-Programming-Questions'),
]
 
