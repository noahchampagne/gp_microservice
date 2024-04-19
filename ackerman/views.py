from django.shortcuts import render
import random

# Create your views here.
calls = 0
global_arr = [i for i in range(8192)]

def start_action(request):
    #If initial request
    if request.method == "GET":
      num = request.GET.get('num')
    #   result = ackermann(3, int(num))

      result = loop_it(int(num))
      context = {'res': result}
      return render(request, "start.html", context)

def loop_it(n):
    global global_arr
    for i in range(n):
        for j in range(8192):
            x = global_arr[j] #touch
    return x

def ackermann(m, n):
    global calls
    stack = []

    while True:
        calls += 1
        if m == 0:
            if not stack:
                return n + 1
            m, n = stack.pop(), n + 1
        elif n == 0:
            m, n = m - 1, 1
        else:
            stack.append(m - 1)
            n -= 1