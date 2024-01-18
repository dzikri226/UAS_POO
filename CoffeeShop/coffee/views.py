from django.shortcuts import render, get_object_or_404, redirect
from .models import Coffee
from django.contrib import messages

def home(request):
    coffee = Coffee.objects.all()
    return render(request, 'home.html', {'coffee': coffee})

def order(request, coffee_id):
    selected_coffee = get_object_or_404(Coffee, pk=coffee_id)
    quantity = request.POST.get('quantity', 1)  # default to 1 if not provided

    if request.method == 'POST':
        # Process order logic here
        messages.success(request, f"Order for {quantity} {selected_coffee.name}(s) placed successfully!")
        return redirect('home')  # Redirect back to the home page or any other page you prefer

    return render(request, 'order.html', {'selected_coffee': selected_coffee, 'quantity': quantity})
