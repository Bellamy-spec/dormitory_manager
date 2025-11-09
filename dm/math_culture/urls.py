"""数学文化素材库的url模式"""
from django.urls import path
from . import views


urlpatterns = [
    # 主页
    path('', views.index, name='index'),

    # 课本素材分类主页
    path('book/', views.book, name='book'),

    # 一本书的章节列表
    path('chapter_list/<int:book_id>/', views.chapter_list, name='chapter_list'),

    # 一个章节的主页
    path('bk/<str:chapter_id>/', views.bk, name='bk'),

    # 课本素材（图片形式呈现）
    path('pic_bk/<str:chapter_id>/', views.pic_item, name='pic_item'),

    # 课本素材（文本形式呈现）
    path('doc_bk/<str:chapter_id>/', views.doc_items, name='doc_items'),

    # 视频素材（外部链接）
    path('video_bk/<str:chapter_id>/', views.video_items, name='video_items'),

    # 素材共享平台主页
    path('share_index/', views.share_index, name='share_index'),

    # 上传素材的页面
    path('add/', views.add, name='add'),

    # 主线主页
    path('line_index/<int:line_id>/', views.line_index, name='line_index'),

    # 素材主页
    path('share_main/<int:material_id>/', views.material_main, name='material_main'),

    # 素材管理页
    path('share_manage/', views.share_manage, name='share_manage'),

    # 删除素材
    path('delete_share/<int:material_id>/', views.delete_material, name='delete_material'),
]
