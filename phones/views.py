from django.shortcuts import render
from phones.models import Phone

def show_catalog(request):
    all_phones = Phone.objects.all()
    phone_context = []
    for k in all_phones:
        print(k.phone_name, k.phone_image, k.phone_price)
        phone_context.append({'phone_name': k.phone_name,
                              'phone_image': k.phone_image,
                              'phone_price': k.phone_price,
                              'phone_n_slug': k.phone_n_slug})
    print(phone_context)
    template = 'catalog.html'
    context = {'allphones': phone_context}
    #context = {'phone_id_0': {'phone_name': phone_name, 'phone_image': phone_image, 'phone_price': phone_price, 'phone_n_slug': phone_n_slug}}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)
