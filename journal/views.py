from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.utils.timezone import now, timedelta
from .models import UserJournal


def user_login(request):
    '''
    处理用户登陆相关，登陆成功进入主页面，失败界面显示错误信息
    '''
    if request.method == 'GET':
        return render(request, "journal/login.html")
    user = request.POST['user']
    passwd = request.POST['passwd']
    user = authenticate(username=user, password=passwd)     # 调用django用户鉴权模块
    if user is not None:
        if user.is_active:
            login(request, user)    # django登陆
            return HttpResponseRedirect(reverse('journal:index'))
        else:
            return render(request, "journal/login.html", {'error_message': '当前用户不可用'})
    else:
        return render(request, "journal/login.html", {'error_message': '用户名或密码错误'})


@login_required
def index(request):
    '''
    首页，显示最近七天日志列表
    '''
    journal_list = get_journal_info(request.user)
    real_name = request.user.get_full_name().replace(' ', '')
    if not journal_list:
        journal_list = []
    return render(
        request,
        "journal/index.html",
        {'journal_list': journal_list, 'username': real_name})


@login_required
def add_journal(request):
    '''
    填写用户日志界面处理
    '''
    # 非post请求，直接返回填写日志界面
    real_name = request.user.get_full_name().replace(' ', '')

    if request.method == 'GET':
        return render(request, "journal/add_journal.html", {'username': real_name})

    # 收到POST请求，则将用户填写的日志写入数据库
    try:
        new_j = UserJournal(
            usr_name=request.user.get_username(),
            real_name=request.user.get_full_name().replace(' ', ''),
            date=now().date(),
            work_today=request.POST['j_work'],
            question=request.POST['j_question'],
            plan_tomorrow=request.POST['j_plan'],
            process=request.POST['j_process'],
            time_consumed=request.POST['j_time'])
        new_j.save()
    except Exception:
        return render(request, "journal/500.html")
    if 'j_save' in request.POST:
        return HttpResponseRedirect(reverse('journal:index'))
    elif 'j_save_add' in request.POST:
        return HttpResponseRedirect(reverse('journal:add_journal'))


@login_required
def modify_journal(request, journal_id):
    '''
    填写修改日志界面处理
    '''
    user_journal = get_object_or_404(UserJournal, pk=journal_id)
    if request.method == 'GET':
        return render(request, "journal/modify_journal.html", {'user_journal': user_journal})
    # 更新数据库字段, 不修改日志填写日期
    if 'j_save' in request.POST:
        user_journal.work_today = request.POST['j_work']
        user_journal.question = request.POST['j_question']
        user_journal.plan_tomorrow = request.POST['j_plan']
        user_journal.process = request.POST['j_process']
        user_journal.time_consumed = request.POST['j_time']
        user_journal.save()
        return HttpResponseRedirect(reverse('journal:index'))


@login_required
def user_logout(request):
    '''用户退出，释放context'''
    logout(request)
    return HttpResponseRedirect(reverse('journal:user_login'))


def get_journal_info(user):
    '''
    获取当日已填写的日志信息
    '''
    try:
        group = get_object_or_404(Group, user=user)
        # usr_list = get_list_or_404(User, groups__name=group.name)
    except Exception:
        return False
    journal_list = []
    end_time = now().date()
    start_time = end_time - timedelta(days=7)
    # 根据delete_userjournal权限判断用户是否是项目组长，组长可查看所有成员日志。
    if user.has_perm('journal.delete_userjournal'):
        usr_list = get_list_or_404(User, groups__name=group.name)
        for usr in usr_list:
            try:
                journal = UserJournal.objects.filter(
                    usr_name=usr.username,
                    date__range=(start_time, end_time)).order_by('-date')
            except Exception:
                continue
            journal_list += journal
    else:
        journal_list = UserJournal.objects.filter(usr_name=user, date__range=(start_time, end_time)).order_by('-date')
    return journal_list
