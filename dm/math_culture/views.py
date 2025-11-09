from django.shortcuts import render
from .tools import DataTool
import os
from .forms import ShareForm
from django.http import HttpResponseRedirect, Http404, HttpResponse
from .models import Material
from django.urls import reverse
from urllib.parse import quote


# 根路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 实例化静态数据类
DT = DataTool()


# Create your views here.
def index(request):
    """主页"""
    # 标题
    title = '基于信息技术的高中数学文化素材库'

    context = {'title': title}
    return render(request, 'math_culture/index.html', context)


def book(request):
    """课本素材分类主页"""
    return render(request, 'math_culture/book.html', {})


def chapter_list(request, book_id):
    """一本书的章节列表"""
    # 取得章节id、名称二元组列表
    cps = []
    for cp in DT.chapter_list[book_id]:
        cps.append((cp, DT.chapter_name[cp]))

    # 生成标题
    title = DT.book_name[book_id]

    context = {'title': title, 'cps': tuple(cps)}
    return render(request, 'math_culture/chapter_list.html', context)


def bk(request, chapter_id):
    """一个章节的主页"""
    # 生成章节标题
    chapter_name = DT.chapter_name[chapter_id]

    # 所属课本id
    bk_id = DT.get_book_id(chapter_id)

    context = {'title': chapter_name, 'cp_id': chapter_id, 'bk_id': bk_id}
    return render(request, 'math_culture/bk.html', context)


def pic_item(request, chapter_id):
    """一个章节的图片素材"""
    # 生成模板名称
    temp = 'math_culture/pic_bk.html'

    # 生成标题
    chapter_name = DT.chapter_name[chapter_id]
    title = '{}课本素材（图片形式呈现）'.format(chapter_name)

    # 确保服务器上进入正确的目录，可正常运行
    if os.name != 'nt':
        os.chdir('/root/dormitory_manager/dm')

    # 目录名
    dir_name = os.path.join('media', 'math_culture', 'chapter_{}'.format(chapter_id), 'pic')

    # 读取目录内容
    pics = []
    for fn in os.listdir(dir_name):
        root = '/media/math_culture/chapter_{}/pic/{}'.format(chapter_id, fn)
        filename = '.'.join(fn.split('.')[:-1])
        pics.append((filename, root))

    context = {'title': title, 'pics': tuple(pics)}
    return render(request, temp, context)


def doc_items(request, chapter_id):
    """文本素材列表"""
    # 生成标题
    chapter_name = DT.chapter_name[chapter_id]
    title = '{}课本素材（文本形式呈现）'.format(chapter_name)

    # 确保服务器上进入正确的目录，可正常运行
    if os.name != 'nt':
        os.chdir('/root/dormitory_manager/dm')

    # 目录名
    dir_name = os.path.join('media', 'math_culture', 'chapter_{}'.format(chapter_id), 'doc')

    # 读取目录内容
    docs = []
    for path in os.listdir(dir_name):
        htm_root = '/media/math_culture/chapter_{}/doc/{}/{}.htm'.format(chapter_id, path, path)
        docx_root = '/media/math_culture/chapter_{}/doc/{}/{}.docx'.format(chapter_id, path, path)
        docs.append((path, htm_root, docx_root))

    context = {'cp_id': chapter_id, 'title': title, 'docs': tuple(docs)}
    return render(request, 'math_culture/docs_bk.html', context)


def video_items(request, chapter_id):
    """视频素材列表"""
    # 生成标题
    chapter_name = DT.chapter_name[chapter_id]
    title = '{}视频素材（外部链接）'.format(chapter_name)

    # 确保服务器上进入正确的目录，可正常运行
    if os.name != 'nt':
        os.chdir('/root/dormitory_manager/dm')

    # 目录名
    dir_name = os.path.join('media', 'math_culture', 'chapter_{}'.format(chapter_id), 'video_link')

    # 读取目录内容
    links = []
    for fn in os.listdir(dir_name):
        filename = '.'.join(fn.split('.')[:-1])
        fp = os.path.join(dir_name, fn)
        with open(fp, 'r') as f:
            links.append((filename, f.read()))

    context = {'cp_id': chapter_id, 'title': title, 'links': tuple(links)}
    return render(request, 'math_culture/links_bk.html', context)


def share_index(request):
    """素材共享平台主页"""
    context = {'is_manager': request.user.is_staff}
    return render(request, 'math_culture/share_index.html', context)


def add(request):
    """上传素材"""
    if request.method != 'POST':
        # 未提交数据，创建新的表单
        form = ShareForm()
    else:
        # 对POST提交的数据作出处理
        form = ShareForm(request.POST, request.FILES)
        if form.is_valid():
            nm = form.save(commit=False)
            nm.save()

            # 重定向至素材主页
            return HttpResponseRedirect(reverse('math_culture:material_main', args=[nm.id]))

    context = {'form': form}
    return render(request, 'math_culture/add.html', context)


def line_index(request, line_id):
    """主线主页"""
    # 主线名称
    line_name = DT.line_dict[line_id]

    # 取得该主线所有素材
    materials = Material.objects.filter(line=line_name)

    context = {'line_name': line_name, 'materials': materials}
    return render(request, 'math_culture/line_index.html', context)


def material_main(request, material_id):
    """素材主页"""
    # 取出素材对象
    material = Material.objects.get(id=material_id)

    # 判断附件类型
    if str(material.file).split('.')[-1] == 'pptx':
        is_pptx = True
    else:
        is_pptx = False

    # 中文url进行编码
    encode_url = quote(str(material.file))

    return render(request, 'math_culture/material_main.html', {
        'material': material, 'is_pptx': is_pptx, 'file_url': encode_url})


def share_manage(request):
    """素材管理"""
    # 取出所有素材
    materials = Material.objects.all()

    context = {'materials': materials}
    return render(request, 'math_culture/share_manage.html', context)


def delete_material(request, material_id):
    """删除素材"""
    # 取出要删除的对象
    material = Material.objects.get(id=material_id)

    # 删除文件
    try:
        fp = BASE_DIR + '/media/' + str(material.file)
        os.remove(fp)
    except IsADirectoryError:
        # 不存在文件，忽略此步
        pass

    # 执行删除操作
    material.delete()

    # 重定向至管理页
    return HttpResponseRedirect(reverse('math_culture:share_manage'))
