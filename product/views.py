from django.http import HttpResponse
from django.shortcuts import render

from product.models import WareHouse, Product


def index(request):

    warehouse = WareHouse.objects.all()
    products = Product.objects.all()

    if request.method == 'POST':
        kuylak = request.POST['kuylak']
        shim = request.POST['shim']

# Kuylak

        omborxona_mato = WareHouse.objects.get(pk=2)
        omborxona_tugma = WareHouse.objects.get(pk=5)
        omborxona_ip = WareHouse.objects.get(pk=4)

        omborxona_mato.qty = omborxona_mato.qty - int(kuylak) * 0.8
        omborxona_tugma.qty = omborxona_tugma.qty - int(kuylak) * 5
        omborxona_ip.qty = omborxona_ip.qty - int(kuylak) * 10

        omborxona_mato.save()
        omborxona_tugma.save()
        omborxona_ip.save()

# Shim

        omborxona_mato = WareHouse.objects.get(pk=2)
        omborxona_ip = WareHouse.objects.get(pk=4)
        omborxona_zamok = WareHouse.objects.get(pk=6)

        omborxona_mato.qty = omborxona_mato.qty - int(shim) * 1.4
        omborxona_ip.qty = omborxona_ip.qty - int(shim) * 15
        omborxona_zamok.qty = omborxona_zamok.qty - int(shim) * 1

        omborxona_mato.save()
        omborxona_ip.save()
        omborxona_zamok.save()
    else:
        kuylak = 0
        shim = 0

    return render(request, 'index.html', {'warehouse': warehouse,
                                          'products': products,
                                          'kuylak': kuylak,
                                          'shim': shim})
