from django.shortcuts import render
from phones.models import Phone
import operator

def show_catalog(request):
    request_arg = request.GET.get('sort')
    if request_arg == 'price':
        all_phones = Phone.objects.all().order_by('-phone_price')
    else:
        if request_arg == 'name':
            all_phones = Phone.objects.all().order_by('phone_name')
        else:
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
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_data = Phone.objects.get(phone_n_slug=slug)
    print(phone_data)
    context = {'phone_name': phone_data.phone_name,
                    'phone_image': phone_data.phone_image,
                    'phone_price': phone_data.phone_price,
                    'phone_lte_exists': phone_data.phone_lte_exists}
    return render(request, template, context)
