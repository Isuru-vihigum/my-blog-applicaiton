from django.shortcuts import render, redirect  # Import render to display templates and redirect to redirect users
from .models import Investment  # Import the Investment model from the current app
from django.db.models import Sum  # Import the Sum function for aggregating totals

# View to display the home page
def home(request):
    return render(request, 'firmapp/home.html', {})  # Render the 'home.html' template with an empty context

# View to handle funding (investment) operations
def funding(request):    
    if request.method == 'POST':  # Check if the request method is POST, which indicates form submission
        membername = request.POST['member_name']  # Retrieve the member name from the form data
        cpm = request.POST['cpm']  # Retrieve the CPM (student registration number) from the form data
        amount = request.POST['invetsment']  # Retrieve the investment amount from the form data
        
        # Create a new Investment object with the submitted data
        Investment.objects.create(
            member_name=membername,
            member_cpm=cpm,
            investment=amount,
        )
        return redirect('funding')  # Redirect to the funding page to display the updated investment list

    # Retrieve all investment records from the database
    member_list = Investment.objects.all()
    
    # Calculate the total investment amount across all records
    overall_total = sum(Investment.objects.all().values_list('investment', flat=True))
    # **Calculate the sum of 'investment' field for all records in the Investment model**
    
    # Render the funding page with the list of investments and the total investment amount
    return render(request, 'firmapp/funding.html', {
        'member_list': member_list,  # **Pass the retrieved members as a dictionary variable to the template**
        'overall_total': overall_total,  # **Pass the calculated total investment of all members to the template page as a context variable**
    })

# View to display information about a specific member's investments
def member_info(request, member_name):
    # Retrieve all investments for the specified member
    member_investments = Investment.objects.filter(member_name=member_name)
    # **Filter the Investment model to get records matching the specified member's name**
    
    # Calculate the total investment for the specified member
    member_total = Investment.objects.filter(member_name=member_name).aggregate(total=Sum('investment'))['total']
    # **Use the aggregate function to sum up the 'investment' field for the filtered records and retrieve the total**

    # Render the member information page with the member's investments and total investment
    return render(request, 'firmapp/member_info.html', {
        'member_investments': member_investments,  # **Pass the list of investments for the specified member to the template**
        'member_total': member_total,  # **Pass the calculated total investment for the member to the template as a context variable**
    })
