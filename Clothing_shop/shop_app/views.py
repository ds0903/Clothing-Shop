from django.shortcuts import render
comment1 = "Трохи про нас, Наш магазин займається продажем одягу по всьому світу. Наша мета - перевежно етно одягом Якщо ми вас зацікавили виберіть потрібна ваи категорівю одягу"# noqa
date_name1 = "тест повідомлення, посилання на розробника знизу"
comment2 = "Отличная компания с высокопрофессиональными людьми. Не обещают лишнего, точны в прогнозах. Очень порадовал уровень сервиса и внимательное отношение к требованиям клиента. Четко разграниченная специализация – дино стенд, чиптюнинг, работа с выхлопными системами. Надежность чиповки обеспечена дилерским взаимодействием с австрийскими инженерами, которые индивидуально прорабатывают прошивки для каждого клиента. Радует, что в Киеве существует такая крепкая компания по тюнингу, куда с удовольствием и спокойствием может отдать свой автомобиль, как респектабельный бизнесмен, так и оторванный на всю голову стритрейсер."# noqa
date_name2 = "04.03.2023, Сергей, Киев"


def review_list(request):
    reviews = [
        {"image": "shop_app/images/audi1.jpg", "comment": comment1, "date": date_name1},# noqa
        # {'image': 'shop_app/images/audi.jpg', 'comment': comment2, 'date': date_name2},# noqa
        # {'image': 'shop_app/images/audi2.jpg', 'comment': 'Залупа а не сервіс', 'date': '01.01.2022'},# noqa
        # {'image': 'shop_app/images/audi3.jpg', 'comment': 'параша повна', 'date': '02.01.2022'},# noqa
        # {'image': 'shop_app/images/audi4.jpg', 'comment': 'Залупа а не сервіс', 'date': '01.01.2022'},# noqa
        # {'image': 'shop_app/images/audi5.jpg', 'comment': 'параша повна', 'date': '02.01.2022'},# noqa
        # {'image': 'shop_app/images/audi6.jpg', 'comment': 'Залупа а не сервіс', 'date': '01.01.2022'},# noqa
        # {'image': 'shop_app/images/audi7.jpg', 'comment': 'параша повна', 'date': '02.01.2022'},# noqa
        # Додайте більше відгуків, якщо потрібно
    ]
    return render(request, "shop_app/review_list.html", {"reviews": reviews})
