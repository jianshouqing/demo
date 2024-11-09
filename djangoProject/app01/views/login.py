from django.shortcuts import render
from app01.models import User

def login(request):
    user = request.GET.get('user')
    pwd = request.GET.get('pwd')
    flag = User.objects.filter(name=user, password=pwd).first()
    if flag:
        print("成功")
    else:
        print('失败')

    return render(request, 'logins/login.html')