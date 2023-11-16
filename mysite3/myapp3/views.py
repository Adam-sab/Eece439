from django.shortcuts import render
from .forms import FiboForm
from django.http import HttpResponse

# Function to calculate the Fibonacci value
def fibonacci(n):
    if n < 0:
        return "Input should be a non-negative integer"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_prev = 0
        fib_current = 1

        for i in range(2, n + 1):
            fib_next = fib_prev + fib_current
            fib_prev, fib_current = fib_current, fib_next

        return fib_current

def home(request):
    if request.method == 'POST':
        form = FiboForm(request.POST)
        if form.is_valid():
            formdata = form.cleaned_data
            num = formdata['num']
            num = int(num)
            fib_value = fibonacci(num)
            fib_value_str = str(fib_value)
            return HttpResponse(fib_value_str)
    else:
        form = FiboForm()
    return render(request, 'myapp3/Fibo.html', {'form': form})
