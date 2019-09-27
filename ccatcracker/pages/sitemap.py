from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse



class StaticViewsSitemap(Sitemap):

    def items(self):
        return['index','cdac','ccat','ccee','test','about','register','login','payment','intro','cpp','ccat_notify','C-CAT-2019-Predac-Course']
    
    
    def location(self,item):
        return reverse(item)
