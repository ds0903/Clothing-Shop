from django.shortcuts import render
import json
from django.http import JsonResponse
from .models import Order
from django.shortcuts import render, redirect

from .forms import OrderForm
from django.views.decorators.csrf import csrf_exempt
from .models import Order

comment1 = "Трохи про нас, Наш магазин займається продажем одягу по всьому світу. Наша мета - перевежно етно одягом Якщо ми вас зацікавили виберіть потрібна ваи категорівю одягу"  # noqa
date_name1 = "тест повідомлення, посилання на розробника знизу"
comment2 = "Отличная компания с высокопрофессиональными людьми. Не обещают лишнего, точны в прогнозах. Очень порадовал уровень сервиса и внимательное отношение к требованиям клиента. Четко разграниченная специализация – дино стенд, чиптюнинг, работа с выхлопными системами. Надежность чиповки обеспечена дилерским взаимодействием с австрийскими инженерами, которые индивидуально прорабатывают прошивки для каждого клиента. Радует, что в Киеве существует такая крепкая компания по тюнингу, куда с удовольствием и спокойствием может отдать свой автомобиль, как респектабельный бизнесмен, так и оторванный на всю голову стритрейсер."  # noqa
date_name2 = "04.03.2023, Сергей, Киев"

def checkout(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            cart = json.loads(request.POST.get('cart', '[]'))
            # total_price = sum(item['price'] for item in cart)
            order = form.save(commit=False)
            order.items = json.dumps(cart)
            # order.total_price = total_price
            order.save()
            # Очистка корзины (можно адаптировать под ваши нужды)
            return render(request, 'shop_app/checkout.html', {'order': order})
    else:
        form = OrderForm()
    return render(request, "l", {'form': form})

def review_list(request):
    reviews = [
        {
            "image": "shop_app/images/main.jpg",
            "comment": comment1,
            "date": date_name1,
        },  # noqa
        # {'image': 'shop_app/images/audi.jpg', 'comment': comment2, 'date': date_name2},# noqa
        # {'image': 'shop_app/images/audi2.jpg', 'comment': 'Залупа а не сервіс', 'date': '01.01.2022'},# noqa
        # {'image': 'shop_app/images/audi3.jpg', 'comment': 'параша повна', 'date': '02.01.2022'},# noqa
        # Додайте більше відгуків, якщо потрібно
    ]
    return render(request, "shop_app/main_page.html", {"reviews": reviews})


def cart(request):
    # Опрацьовуємо логіку кошика тут, якщо потрібно

    return render(request, 'shop_app/cart.html')  # Повертаємо сторінку кошика


def kids(request):
    cloth = [
        {"title": "Сукня для дівчинки «Дзвінка» білого кольору", "image": "shop_app/images/kids/1.jpg", "price": 2300},
        {"title": "Вишиванка для хлопчика «Омелянчик» блакитного кольору", "image": "shop_app/images/kids/2.jpg", "price": 1499},
        {"title": "Вишиванка для дівчинки «Мереживний розмай» білого кольору з червоно-чорною вишивкою", "image": "shop_app/images/kids/3.jpg", "price": 1200},
        {"title": "Сукня для дівчинки «Дзвінка» червоного кольору", "image": "shop_app/images/kids/4.jpg", "price": 2300},
        {"title": "Вишиванка для хлопчика «Кольорова» темно-синього кольору", "image": "shop_app/images/kids/5.jpg", "price": 2250},
        {"title": "Вишиванка для хлопчика «Завитки» білого кольору", "image": "shop_app/images/kids/6.jpg", "price": 750},
        {"title": "Футболка для дівчинки «Весняна 2» червоного кольору", "image": "shop_app/images/kids/7.jpg", "price": 350},
        {"title": "Вишиванка для хлопчика «Отаман» чорна з білим орнаментом", "image": "shop_app/images/kids/8.jpg", "price": 1650},
        {"title": "Вишиванка для хлопчика «Полонина» з синім орнаментом", "image": "shop_app/images/kids/9.jpg", "price": 1400},
        {"title": "Сукня для дівчинки «Квіткова гілка» синього кольору", "image": "shop_app/images/kids/10.jpg", "price": 2000},
        {"title": "Вишиванка для хлопчика «Отаман» біла з червоним орнаментом", "image": "shop_app/images/kids/11.jpg", "price": 1650},
        {"title": "Вишиванка для дівчинки «Мереживні сни» рожевого кольору", "image": "shop_app/images/kids/12.jpg", "price": 1700},
        {"title": "Вишиванка для хлопчика «Грація» зеленого кольору", "image": "shop_app/images/kids/13.jpg", "price": 950},
        {"title": "Вишиванка для хлопчика «Грація» темно-синього кольору", "image": "shop_app/images/kids/14.jpg", "price": 950},
        {"title": "Вишитий комбінезон для дівчинки «Розмай» кольору охри", "image": "shop_app/images/kids/15.jpg", "price": 1900},
    ]
    return render(request, "shop_app/kids.html", {"cloth": cloth})


def woman(request):
    cloth = [
        {"title": "Вишита сукня Осоння", "image": "shop_app/images/woman/1.jpg", "price": 5700},
        {"title": "Вишита сукня Зоряна ніч", "image": "shop_app/images/woman/2.jpg", "price": 5700},
        {"title": "Вишиванка жіноча Запоріжжя", "image": "shop_app/images/woman/3.jpg", "price": 4600},
        {"title": "Вишиванка жіноча Зілля", "image": "shop_app/images/woman/4.jpg", "price": 4040},
        {"title": "Вишиванка жіноча Дніпровщина", "image": "shop_app/images/woman/5.jpg", "price": 4540},
        {"title": "Вишиванка жіноча Сяйво", "image": "shop_app/images/woman/6.jpg", "price": 4400},
        {"title": "Вишиванка жіноча Серпанок сіра", "image": "shop_app/images/woman/7.jpg", "price": 4300},
        {"title": "Вишиванка жіноча Настасія", "image": "shop_app/images/woman/8.jpg", "price": 4800},
        {"title": "Вишиванка жіноча Дивоцвіт", "image": "shop_app/images/woman/9.png", "price": 3920},
        {"title": "Вишиванка жіноча Кропивниччина", "image": "shop_app/images/woman/10.jpg", "price": 4650},
        {"title": "Вишиванка жіноча Хмельниччина", "image": "shop_app/images/woman/11.jpg", "price": 4140},
        {"title": "Вишита сукня Тетяна хакі", "image": "shop_app/images/woman/12.jpg", "price": 3600},
        {"title": "Вишиванка жіноча Тернопільщина", "image": "shop_app/images/woman/13.jpg", "price": 5600},
        {"title": "Вишиванка жіноча Легіт", "image": "shop_app/images/woman/14.jpg", "price": 3640},
        {"title": "Жіноча вишиванка Катря", "image": "shop_app/images/woman/15.jpg", "price": 4320},
    ]
    return render(request, "shop_app/woman.html", {"cloth": cloth})


def man(request):
    cloth = [
        {"title": "Вишиванка чоловіча Кропивниччина", "image": "shop_app/images/man/11.png", "price": 3990},
        {"title": "Вишиванка чоловіча Юстин білий", "image": "shop_app/images/man/22.jpg", "price": 3980},
        {"title": "Вишиванка чоловіча Гори небесні", "image": "shop_app/images/man/33.jpg", "price": 3710},
        {"title": "Вишиванка чоловіча Червона рута", "image": "shop_app/images/man/44.jpg", "price": 4200},
        {"title": "Вишиванка чоловіча Хмельниччина", "image": "shop_app/images/man/55.jpg", "price": 3500},
        {"title": "Вишиванка чоловіча NEPTUNE", "image": "shop_app/images/man/66.jpg", "price": 4600},
        {"title": "Вишиванка чоловіча NEPTUNE лімітована версія", "image": "shop_app/images/man/77.jpg", "price": 9700},
        {"title": "Вишиванка чоловіча Сумщина", "image": "shop_app/images/man/88.jpg", "price": 3640},
        {"title": "Вишиванка чоловіча Волинь чорна", "image": "shop_app/images/man/99.jpg", "price": 4300},
        {"title": "Вишиванка чоловіча Гори блакитні", "image": "shop_app/images/man/100.jpg", "price": 3100},
        {"title": "Вишиванка чоловіча Кодимське коріння", "image": "shop_app/images/man/110.jpg", "price": 3300},
        {"title": "Вишиванка чоловіча Кодимська кривулька", "image": "shop_app/images/man/120.png", "price": 3300},
        {"title": "Вишиванка чоловіча Черкащина", "image": "shop_app/images/man/130.jpg", "price": 3900},
        {"title": "Вишиванка чоловіча Волинь натуральна", "image": "shop_app/images/man/140.jpg", "price": 4300},
        {"title": "Вишиванка чоловіча Сузір`я", "image": "shop_app/images/man/150.jpg", "price": 5200},
    ]
    return render(request, "shop_app/man.html", {"cloth": cloth})


@csrf_exempt
def save_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        phone = data.get('phone')

        if name and phone:
            order = Order(name=name, phone=phone)
            order.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid data'})

    return JsonResponse({'success': False, 'error': 'Invalid method'})