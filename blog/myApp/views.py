from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Article,Message,comment
from django.contrib.auth import logout
from django.shortcuts import redirect
# 引入的返回聚合函数
from django.db.models import Max,Min,F,Q

# Create your views here.
# def article(request):
#     articlelist = Article.article.all()
#     return render(request,'myApp/index.html',{'articlelist':articlelist})#返回给html
# # 分页
# # def stupage(requst,page):
# #     # 0-5   5-10    10-15
# #     # 1     2       3
# #     page = int(page)
# #     studentlist = Article.article.all()[(page-1)*5:page*5]#显示三条匹配的数据
# #     return render(requst, 'myApp/index.html', {'students': studentlist})  # 返回给html，render起渲染作用

from django.core.paginator import Paginator
def articlepage(request):
    alllist = Article.article.all()
    paginator = Paginator(alllist,2)
    page1 = request.GET.get('page', '1')  # 默认跳转到第一页
    page = paginator.page(page1)
    return render(request,"myApp/index.html",{'articlelist':page})

def content(request):
    articlelist = Article.article.all()
    # a = articlelist.filter(id__lte=5)
    return render(request,'myApp/content.html',{'articlelist':articlelist})#返回给html

def tocontent(request,id):
    articlelist = Article.article.filter(pk=id)
    return render(request, "myApp/content.html",{'articlelist':articlelist})

# def list1(request):
#     return render(request,"myApp/list.html")

def message(request):
    return render(request,"myApp/message.html")
from django.utils import timezone #引入timezone模块

def tomessage(request):
    time_now = timezone.now()  # 输出time_now即为当然日期和时间
    commenter1 = request.POST.get("commenter")
    emil1 = request.POST.get("emil")
    phone1 = request.POST.get("phone")
    contend1 = request.POST.get("content")
    create = Message.createmessage(commenter1,phone1,emil1,contend1,time_now,False)
    create.save()

    alllist = Article.article.all()
    paginator = Paginator(alllist, 2)
    page1 = request.GET.get('page', '1')  # 默认跳转到第一页
    page = paginator.page(page1)
    return render(request, "myApp/index.html", {'articlelist': page})

def tocomment(request):
    time_now = timezone.now()  # 输出time_now即为当然日期和时间
    author = request.POST.get("author")
    emil1 = request.POST.get("email")
    contend1 = request.POST.get("comment")
    id = request.POST.get("id")
    create = comment.createcomment(author,emil1,contend1,time_now,id)
    create.save()
    return HttpResponse("发表成功")

def comment1(request,id):
    duixiang = Article.article.get(pk=id)
    comments = duixiang.comment_set.all()
    # grades = Grades.grade.get(pk=num)#获取班级id的对象
    # students = grades.student_set.all()#根据对象获取匹配的所有学生
    return render(request,'myApp/comments.html',{'comments':comments})#返回给html

def me(request):
    return render(request,'myApp/me.html')