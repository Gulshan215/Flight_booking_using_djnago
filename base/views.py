from django.shortcuts import render,redirect
from base.models import IndigoModels,AirIndiaModel,VistaraModel,SpiceJetModel,GoFirstModel,BookingModel,DeletedBookingModel
from datetime import datetime, timedelta

# def add(request):

#     if request.method=='POST':
#         name=request.POST['name']
#         flight_number=request.POST['flight_number']
#         depart_from=request.POST['depart_from']
#         departure_time=request.POST['departure_time']
#         destination=request.POST['destination']
#         arrival_time=request.POST['arrival_time']
#         price = request.POST['price']
        
#         print(title_data,desc_data)
#         TaskModel.objects.create(title=title_data,desc=desc_data)
#         return redirect('home')

#     return render(request,'add.html')
# Create your views here.
def home(request):
    return render(request,'home.html',{})

def booking(request):
    return render(request,'booking.html',{})

def history(request):
    return render(request,'history.html',{})

def profile(request):
    return render(request,'profile.html',{})

def about(request):
    return render(request,'about.html',{})



def indigo(request):

    indigo=IndigoModels.objects.all()

    return render(request,'indigo.html',{'indigo':indigo})

def airindia(request):

    air=AirIndiaModel.objects.all()

    return render(request,'airindia.html',{'air':air})

def spicejet(request):

    spice=SpiceJetModel.objects.all()

    return render(request,'spicejet.html',{'spice':spice})

def gofirst(request):

    go=GoFirstModel.objects.all()

    return render(request,'gofirst.html',{'go':go})

def vistara(request):

    vis = VistaraModel.objects.all()

    return render(request,'Vistara.html',{'vis':vis})

def booking(request,airline,pk):
    airline_models = {
        'indigo': IndigoModels,
        'airindia': AirIndiaModel,
        'vistara': VistaraModel,
        'gofirst': GoFirstModel,
        'spicejet': SpiceJetModel,
    }
    model = airline_models.get(airline.lower())

    if not model:
        return HttpResponse("Invalid airline", status=400)

    try:
        flight = model.objects.get(id=pk)
    except model.DoesNotExist:
        return HttpResponse("Flight not found", status=404)

    if request.method=='POST':
        flight_data=request.POST['flight_name']
        name_data=request.POST['name']
        email_data=request.POST['email']
        ph_data=request.POST['phno']
        age_data=request.POST['age']
        print(name_data,email_data,ph_data,age_data,flight_data)

        BookingModel.objects.create(flight_name=flight_data,name=name_data,email=email_data,phno=ph_data,age=age_data)
        return redirect('home')

    return render(request,'booking.html',{'flight': flight})

def booking_details(request):
    bookings = BookingModel.objects.all()

    # Get all flights once
    all_flights = list(IndigoModels.objects.all()) + \
                  list(AirIndiaModel.objects.all()) + \
                  list(VistaraModel.objects.all()) + \
                  list(GoFirstModel.objects.all()) + \
                  list(SpiceJetModel.objects.all())

    # Build list of bookings with matched flight
    detailed_bookings = []

    for booking in bookings:
        # Try to match booking.flight_name with any flight.name
        matched_flight = next((f for f in all_flights if f.name.lower() == booking.flight_name.lower()), None)

        detailed_bookings.append({
            'booking': booking,
            'flight': matched_flight
        })
    return render(request, 'booking_details.html', {'detailed_bookings': detailed_bookings})

def edit(request,pk):
    book=BookingModel.objects.get(id=pk)

    if request.method=='POST':
        name_data=request.POST['name']
        email_data=request.POST['email']
        ph_data=request.POST['phno']
        flight_data=request.POST['flight_name']
        age_data=request.POST['age']

        book.name=name_data
        book.email=email_data
        book.phno=ph_data
        book.flight_name=flight_data
        book.age=age_data
        book.save()
        return redirect('booking_details')
    
    return render(request,'edit.html',{'book':book})

def confirm_del(request,pk):

    book=BookingModel.objects.get(id=pk)

    return render(request,'confirm_del.html',{'book':book})

def del_(request, pk):
    book = BookingModel.objects.get(id=pk)

    # Save to deleted model before deleting
    DeletedBookingModel.objects.create(
        flight_name=book.flight_name,
        name=book.name,
        email=book.email,
        phno=book.phno,
        age=book.age,
    )

    book.delete()
    return redirect('booking_details')

def history(request):
    deleted_bookings = DeletedBookingModel.objects.all().order_by('-deleted_at')
    return render(request, 'history.html', {'deleted_bookings': deleted_bookings})

def recover_booking(request, pk):
    deleted = DeletedBookingModel.objects.get(id=pk)

    # Move data back to BookingModel
    BookingModel.objects.create(
        flight_name=deleted.flight_name,
        name=deleted.name,
        email=deleted.email,
        phno=deleted.phno,
        age=deleted.age,
        
    )

    # Delete from DeletedBookingModel
    deleted.delete()

    return redirect('booking_details')


def delete_forever(request, pk):
    deleted = DeletedBookingModel.objects.get(id=pk)
    deleted.delete()
    return redirect('home')
