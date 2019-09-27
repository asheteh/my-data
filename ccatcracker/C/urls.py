from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.intro,name='intro'),
    path('platform',views.platform,name='platform'),
    path('variables',views.variables,name='variables'),
    path('library',views.library,name='library'),
    path('data_types',views.data_types,name='data_types'),
    path('size_of',views.size_of,name='size_of'),
    path('modify_operator',views.modify,name='modify_operator'),
    path('control_statement',views.if_else,name='control_statement'),
    path('String-In-C-Tutorial',views.string,name='String-In-C-Tutorial'),
    path('Structure-In-C-Tutorial',views.structure,name='Structure-In-C-Tutorial'),
    path('Array-In-C-Language-Tutorial',views.array,name='Array-In-C-Language-Tutorial'),
    path('Pointers-In-C-Language-Tutorial',views.pointers,name='Pointers-In-C-Language-Tutorial'),
    path('Memory-Allocation-In-C-Tutorial',views.memory_allocation,name='Memory-Allocation-In-C-Tutorial'),
    path('File-Handling-In-C-Tutorial',views.files,name='File-Handling-In-C-Tutorial'),
    path('typedef-In-C-Tutorial',views.typedef,name='typedef-In-C-Tutorial'),
    path('command-line-In-C-Tutorial',views.some_extra,name='command-line-In-C-Tutorial'),
    path('program-In-C-Tutorial',views.program,name='program-In-C-Tutorial'),
    path('projects-In-C-Tutorial',views.projects,name='projects-In-C-Tutorial'),
    path('Data-Structure-Tutorial',views.ds,name='Data-Structure-Tutorial'),
    path('Linked-List-Tutorial',views.linked_list,name='Linked-List-Tutorial'),
    path('Queue-Tutorial',views.queue,name='Queue-Tutorial'),
    path('Linked-List-Implementaion',views.implement,name='Linked-List-Implementaion'),
    path('Tree-Data-Structure',views.tree,name='Tree-Data-Structure'),
    path('OS-Tutorial',views.os,name='OS-Tutorial'),
    path('Paging-Segementation-OS',views.paging,name='Paging-Segementation-OS'),
    path('Difference-In-Os',views.diff,name='Difference-In-Os'),
    path('download',views.download,name='download'),
    path('Networking-Tutorials',views.network,name='Networking-Tutorials'),
    

    
    
    
    #path('payment_test',views.payment_test,name='payment_test'),
     
]
