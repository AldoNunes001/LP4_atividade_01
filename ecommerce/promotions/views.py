from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404


# SIMULANDO O BD COM PROMOÇÕES
promotions = [
    {'id': 1, 'title': 'Título da Promoção 1', 'description': 'Descrição da Promoção 1', 'price': 100},
    {'id': 2, 'title': 'Título da Promoção 2', 'description': 'Descrição da Promoção 2', 'price': 200},
    {'id': 3, 'title': 'Título da Promoção 3', 'description': 'Descrição da Promoção 3', 'price': 300},
    {'id': 4, 'title': 'Título da Promoção 4', 'description': 'Descrição da Promoção 4', 'price': 400},
]


# Create your views here.
def list_promotions(request):
    context = {'promotions': promotions}
    return render(request, 'promotions/index.html', context)


def detail_promotion(request, promotion_id):
    promotion = None
    context = {}
    try:
        promotion = promotions[promotion_id-1]
        context = {'promotion': promotion}
    except IndexError:
        raise Http404('Promoção inexistente')

    # title = get_object_or_404(promotions, pk=id)

    # return HttpResponse(f'Promotion: {title}')
    return render(request, 'promotions/promotion.html', context)
