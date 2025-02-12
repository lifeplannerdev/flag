import razorpay
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import JsonResponse
from .models import Registration




def home(request):
    return render (request,"home.html")


def demo(request):
    return render (request ,"demo.html")


def about(request):    
    return render (request,"about.html")

razorpay_client = razorpay.Client(auth=("rzp_test_dTWp25pBQ5jW81", "Sg6ymJfWNf4atGBsqXhuaALE"))

def registeration(request):
    if request.method == "POST":
        name = request.POST.get("fullName")
        email = request.POST.get("emailAddress")
        phone = request.POST.get("contact")
        course = request.POST.get("course")
        amount = int(request.POST.get("amount")) * 100  # Convert to paisa

        # Create Razorpay order
        order_data = {
            "amount": amount,
            "currency": "INR",
            "payment_capture": 1  # Auto capture
        }
        order = razorpay_client.order.create(data=order_data)

        # Save user data in database
        registration = Registration(
            name=name,
            email=email,
            phone=phone,
            course=course,
            amount=amount // 100,  # Convert back to INR for storage
            payment_id=order['id']
        )
        registration.save()

        # Send order details to frontend
        return JsonResponse({
            "order_id": order["id"],
            "key": "rzp_test_dTWp25pBQ5jW81",
            "amount": amount,
            "currency": "INR",
            "name": name,
            "email": email,
            "contact": phone
        })

    return render(request, "registration.html")



from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def payment_success(request):
    if request.method == "POST":
        payment_id = request.POST.get("payment_id")
        order_id = request.POST.get("order_id")

        try:
            registration = Registration.objects.get(payment_id=order_id)
            registration.payment_status = "Paid"
            registration.save()
            return JsonResponse({"status": "success"})
        except Registration.DoesNotExist:
            return JsonResponse({"status": "failed", "message": "Order not found"})

    return JsonResponse({"status": "failed", "message": "Invalid request"})

def success_page(request):
    return render(request, "success.html")

def levels(request):
    return render (request,"levels.html")    

def whyflag(request):
    return render (request,"whyflag.html")   

def germany(request):
    return render (request,"germany.html")