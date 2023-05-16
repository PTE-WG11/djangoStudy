from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse


def page1_view(request):
    html = "<h1>这是第一个页面</h1>"
    return HttpResponse(html)


def page2_view(request, name=''):
    return HttpResponse("<h1>你的名字是%s</h1>" % name)


def test_get_post(request):
    if request.method == 'GET':
        return HttpResponse('--test get is ok--')
    elif request.method == 'POST':
        return HttpResponse('--post is ok--')
    else:
        return HttpResponse('--... is ok--')


def mypage(request):
    if request.method == 'GET':
        a = request.GET['a']
        b = request.GET.get('b', 'no b')
        c = request.GET.get('c', 'no c')
        print(a)
        print(b)
        print(c)
        # return HttpResponse('a+b+c={}'.format(int(a) + int(b) + int(c)))
        return render(request, 'index.html')
    elif request.method == 'POST':
        a = request.POST['a']
        b = request.POST.get('b', 'no b')
        print(a)
        print(b)
        return HttpResponse('--post is ok--\n<br>a+b=%s' % (int(a) + int(b)))
    else:
        return HttpResponse('--... is ok--')


def test_html01(request):
    # 方案1，早期用这个
    from django.template import loader
    t = loader.get_template('test_html.html')
    html = t.render()
    return HttpResponse(html)


def ces():
    c = []
    for i in range(10):
        c.append(i)
        # print(i)
    return c


def test_html02(request):
    from django.shortcuts import render
    dic = {'username': 'wgy', 'age': 18, 'func': ces}

    return render(request, 'test_html.html', dic)


def say_hi():
    return 'Hi,'


class Dog:
    def __init__(self):
        pass

    def say(self):
        return "wangwangwang"


def test_html_param(request):
    dic = {}
    dic['int'] = 88
    dic['str'] = 'WHY'
    dic['lst'] = ['Tom', 'Jack', '...']
    dic['dict'] = {'a': 9, 'b': 10}
    dic['func'] = say_hi
    dic['class_obj'] = Dog()
    dic['script'] = '<script>alert(1111)</script>'
    return render(request, 'test_html.html', dic)


def mycal(request):
    if request.method == 'GET':
        dic = {'x': '', 'y': '', 'op': '', 'ero': None}
        return render(request, 'calculator.html')
    elif request.method == 'POST':
        # x = request.POST.get['x', '']
        # y = request.POST.get['y', '']
        # op = request.POST.get['op', '']
        x = request.POST['x']
        y = request.POST['y']
        op = request.POST['op']
        if x == '' or y == '':
            return render(request, 'calculator.html', {'ero': '输入错误请重新输入'})
        else:
            dic = {'x': x, 'y': y, 'op': op, 'ero': ''}
        if op == 'add':
            sum = int(x) + int(y)
        elif op == 'sub':
            sum = int(x) - int(y)
        elif op == 'mul':
            sum = int(x) * int(y)
        elif op == 'div':
            sum = int(x) / int(y)
        dic['sum'] = sum
        dic['fu'] = "="
        dic2 = locals()  # 自动生成字典
        print(dic2)
    return render(request, 'calculator.html', dic)


def test_url_result(request):
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(reverse('ur'))
    return render(request, 'test_url.html')
