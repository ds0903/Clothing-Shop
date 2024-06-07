import json

from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from .forms import OrderForm
from .models import Order

comment1 = "Трохи про нас, Наш магазин займається продажем одягу по всьому світу. Наша мета - перевежно етно одягом Якщо ми вас зацікавили виберіть потрібна ваи категорівю одягу"  # noqa


def main_page(request):
    return render(request, "shop_app/main_page.html")


def review_list(request):
    reviews = [
        {
            "image": "shop_app/images/main.jpg",
            "comment": comment1,
            # "date": date_name1,
        },
    ]
    return render(request, "shop_app/main_page.html", {"reviews": reviews})


def cart(request):
    # Опрацьовуємо логіку кошика тут, якщо потрібно

    return render(request, "shop_app/cart.html")  # Повертаємо сторінку кошика


def kids(request):
    cloth = [
        {
            "title": "Сукня для дівчинки «Дзвінка» білого кольору",
            "image": "shop_app/images/kids/1.jpg",
            "price": 2300,
        },
        {
            "title": "Вишиванка для хлопчика «Омелянчик» блакитного кольору",
            "image": "shop_app/images/kids/2.jpg",
            "price": 1499,
        },
        {
            "title": "Вишиванка для дівчинки «Мереживний розмай» білого кольору з червоно-чорною вишивкою",# noqa
            "image": "shop_app/images/kids/3.jpg",
            "price": 1200,
        },
        {
            "title": "Сукня для дівчинки «Дзвінка» червоного кольору",
            "image": "shop_app/images/kids/4.jpg",
            "price": 2300,
        },
        {
            "title": "Вишиванка для хлопчика «Кольорова» темно-синього кольору",# noqa
            "image": "shop_app/images/kids/5.jpg",
            "price": 2250,
        },
        {
            "title": "Вишиванка для хлопчика «Завитки» білого кольору",
            "image": "shop_app/images/kids/6.jpg",
            "price": 750,
        },
        {
            "title": "Футболка для дівчинки «Весняна 2» червоного кольору",
            "image": "shop_app/images/kids/7.jpg",
            "price": 350,
        },
        {
            "title": "Вишиванка для хлопчика «Отаман» чорна з білим орнаментом",# noqa
            "image": "shop_app/images/kids/8.jpg",
            "price": 1650,
        },
        {
            "title": "Вишиванка для хлопчика «Полонина» з синім орнаментом",
            "image": "shop_app/images/kids/9.jpg",
            "price": 1400,
        },
        {
            "title": "Сукня для дівчинки «Квіткова гілка» синього кольору",
            "image": "shop_app/images/kids/10.jpg",
            "price": 2000,
        },
        {
            "title": "Вишиванка для хлопчика «Отаман» біла з червоним орнаментом",# noqa
            "image": "shop_app/images/kids/11.jpg",
            "price": 1650,
        },
        {
            "title": "Вишиванка для дівчинки «Мереживні сни» рожевого кольору",
            "image": "shop_app/images/kids/12.jpg",
            "price": 1700,
        },
        {
            "title": "Вишиванка для хлопчика «Грація» зеленого кольору",
            "image": "shop_app/images/kids/13.jpg",
            "price": 950,
        },
        {
            "title": "Вишиванка для хлопчика «Грація» темно-синього кольору",
            "image": "shop_app/images/kids/14.jpg",
            "price": 950,
        },
        {
            "title": "Вишитий комбінезон для дівчинки «Розмай» кольору охри",
            "image": "shop_app/images/kids/15.jpg",
            "price": 1900,
        },
    ]
    return render(request, "shop_app/kids.html", {"cloth": cloth})


def woman(request):
    cloth = [
        {
            "title": "Вишита сукня Осоння",
            "image": "shop_app/images/woman/1.jpg",
            "price": 5700,
        },
        {
            "title": "Вишита сукня Зоряна ніч",
            "image": "shop_app/images/woman/2.jpg",
            "price": 5700,
        },
        {
            "title": "Вишиванка жіноча Запоріжжя",
            "image": "shop_app/images/woman/3.jpg",
            "price": 4600,
        },
        {
            "title": "Вишиванка жіноча Зілля",
            "image": "shop_app/images/woman/4.jpg",
            "price": 4040,
        },
        {
            "title": "Вишиванка жіноча Дніпровщина",
            "image": "shop_app/images/woman/5.jpg",
            "price": 4540,
        },
        {
            "title": "Вишиванка жіноча Сяйво",
            "image": "shop_app/images/woman/6.jpg",
            "price": 4400,
        },
        {
            "title": "Вишиванка жіноча Серпанок сіра",
            "image": "shop_app/images/woman/7.jpg",
            "price": 4300,
        },
        {
            "title": "Вишиванка жіноча Настасія",
            "image": "shop_app/images/woman/8.jpg",
            "price": 4800,
        },
        {
            "title": "Вишиванка жіноча Дивоцвіт",
            "image": "shop_app/images/woman/9.png",
            "price": 3920,
        },
        {
            "title": "Вишиванка жіноча Кропивниччина",
            "image": "shop_app/images/woman/10.jpg",
            "price": 4650,
        },
        {
            "title": "Вишиванка жіноча Хмельниччина",
            "image": "shop_app/images/woman/11.jpg",
            "price": 4140,
        },
        {
            "title": "Вишита сукня Тетяна хакі",
            "image": "shop_app/images/woman/12.jpg",
            "price": 3600,
        },
        {
            "title": "Вишиванка жіноча Тернопільщина",
            "image": "shop_app/images/woman/13.jpg",
            "price": 5600,
        },
        {
            "title": "Вишиванка жіноча Легіт",
            "image": "shop_app/images/woman/14.jpg",
            "price": 3640,
        },
        {
            "title": "Жіноча вишиванка Катря",
            "image": "shop_app/images/woman/15.jpg",
            "price": 4320,
        },
    ]
    return render(request, "shop_app/woman.html", {"cloth": cloth})


def man(request):
    cloth = [
        {
            "title": "Вишиванка чоловіча Кропивниччина",
            "image": "shop_app/images/man/11.png",
            "price": 3990,
        },
        {
            "title": "Вишиванка чоловіча Юстин білий",
            "image": "shop_app/images/man/22.jpg",
            "price": 3980,
        },
        {
            "title": "Вишиванка чоловіча Гори небесні",
            "image": "shop_app/images/man/33.jpg",
            "price": 3710,
        },
        {
            "title": "Вишиванка чоловіча Червона рута",
            "image": "shop_app/images/man/44.jpg",
            "price": 4200,
        },
        {
            "title": "Вишиванка чоловіча Хмельниччина",
            "image": "shop_app/images/man/55.jpg",
            "price": 3500,
        },
        {
            "title": "Вишиванка чоловіча NEPTUNE",
            "image": "shop_app/images/man/66.jpg",
            "price": 4600,
        },
        {
            "title": "Вишиванка чоловіча NEPTUNE лімітована версія",
            "image": "shop_app/images/man/77.jpg",
            "price": 9700,
        },
        {
            "title": "Вишиванка чоловіча Сумщина",
            "image": "shop_app/images/man/88.jpg",
            "price": 3640,
        },
        {
            "title": "Вишиванка чоловіча Волинь чорна",
            "image": "shop_app/images/man/99.jpg",
            "price": 4300,
        },
        {
            "title": "Вишиванка чоловіча Гори блакитні",
            "image": "shop_app/images/man/100.jpg",
            "price": 3100,
        },
        {
            "title": "Вишиванка чоловіча Кодимське коріння",
            "image": "shop_app/images/man/110.jpg",
            "price": 3300,
        },
        {
            "title": "Вишиванка чоловіча Кодимська кривулька",
            "image": "shop_app/images/man/120.png",
            "price": 3300,
        },
        {
            "title": "Вишиванка чоловіча Черкащина",
            "image": "shop_app/images/man/130.jpg",
            "price": 3900,
        },
        {
            "title": "Вишиванка чоловіча Волинь натуральна",
            "image": "shop_app/images/man/140.jpg",
            "price": 4300,
        },
        {
            "title": "Вишиванка чоловіча Сузір`я",
            "image": "shop_app/images/man/150.jpg",
            "price": 5200,
        },
    ]
    return render(request, "shop_app/man.html", {"cloth": cloth})


@csrf_exempt
def save_order(request: HttpRequest) -> JsonResponse:
    if request.method == "POST":
        data = json.loads(request.body)
        name1 = data.get("name")
        phone1 = data.get("phone")
        order = data.get("order_number")
        order_name = data.get("order_items")
        if name1 and phone1:
            order = Order(
                name=name1, phone=phone1, order_number=order, order_items=order_name# noqa
            )
            order.save()
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False, "error": "Invalid data"})

    return JsonResponse({"success": False, "error": "Invalid method"})


def checkout(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            cart = json.loads(request.POST.get("cart", "[]"))
            order = form.save(commit=False)
            order.items = json.dumps(cart)
            order.save()
            return redirect("main_page")
    else:
        form = OrderForm()
    return redirect("main_page")
