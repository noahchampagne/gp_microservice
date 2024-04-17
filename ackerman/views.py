from django.shortcuts import render

# Create your views here.
calls = 0

def start_action(request):
    #If initial request
    if request.method == "GET":
      # num = request.GET.get('num')
      # result = ackermann(3, int(num))
      # print(result)
      # context = {'res': result}
      context = {'res': 100}
      return render(request, "start.html", context)

def ackerman_fn(m, n):
  global calls
  calls += 1
  if m == 0:
      return n + 1
  elif n == 0:
      return ackerman_fn(m - 1, 1)
  else:
      return ackerman_fn(m - 1, ackerman_fn(m, n - 1))

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