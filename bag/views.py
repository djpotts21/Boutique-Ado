from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')  # render the bag.html template

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    quantity = int(request.POST.get('quantity'))  # get the quantity from the form
    redirect_url = request.POST.get('redirect_url')  # get the redirect url from the form
    bag = request.session.get('bag', {})  # get the bag from the session
    if item_id in list(bag.keys()):  # if the item is already in the bag
        bag[item_id] += quantity  # add the quantity to the existing item
    else:  # if the item is not in the bag
        bag[item_id] = quantity  # add the item to the bag
    request.session['bag'] = bag  # update the session bag variable
    print(request.session['bag'])  # print the session bag variable
    return redirect(redirect_url)  # redirect to the redirect url