from django.shortcuts import render


def view_bag(request):
    """
    A view to renders shopping bag page
    """
    return render(request, 'bag/bag.html')
