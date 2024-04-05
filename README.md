<h1><span>Виртуальная стажировка от SkillFactory -2024&nbsp;</span></h1>
<h3><span>RestAPI для Федерации Спортивного Туризма России (ФСТР).</span></h3>

<p><em>ФСТР &mdash; организация, занимающаяся развитием и популяризацией спортивного туризма в России и руководящая проведением всероссийских соревнований в этом виде спорта.</em></p>

<p><strong><em>ТЗ от заказчика:</em></strong></p>

• разработать мобильное приложение для Android и IOS, которое упростило бы туристам задачу по отправке данных о перевале и сократило время обработки запроса до трёх дней. Пользоваться мобильным приложением будут туристы. В горах они будут вносить данные о перевале в приложение и отправлять их в ФСТР, как только появится доступ в Интернет.

• модератор из федерации будет верифицировать и вносить в базу данных информацию, полученную от пользователей, а те в свою очередь смогут увидеть в мобильном приложении статус модерации и просматривать базу с объектами, внесёнными другими.

<p><em><strong>Задачи:</strong></em></p>

<ul dir="auto">
<li>Разработка<span>&nbsp;</span><em>REST</em><span>&nbsp;</span><em>API</em>, которое будет обслуживать мобильное приложение;</li>
<li>Разработка мобильного приложения;</li>
<li>Тестирование<span>&nbsp;</span><em>REST</em><span>&nbsp;</span><em>API</em><span>&nbsp;</span>и мобильного приложения.</li>
</ul>
Пользователь с помощью мобильного приложения будет передавать в ФСТР:

- следующие данные о перевале:
- координаты перевала и его высота;
- имя пользователя;
- почта и телефон пользователя;
- название перевала;
- несколько фотографий перевала

После этого турист нажмёт кнопку «Отправить» в мобильном приложении. Мобильное приложение вызывает метод **submitData** твоего REST API.

  GET /submitData/ - получает и выводит информацию о всех записях (перевалах).

  POST /submitData/ - заявка на внесение информации об одном горном перевале

  Пример JSON с информацией о перевале

    >{
            "id": 1,
            "user_id": {
                "id": 1,
                "email": "user1@gmail.com",
                "full_name": "Joe Rogan",
                "phone": 15711349804
            },
            "coords_id": {
                "id": 1,
                "latitude": "23.23423400",
                "longitude": "34.23423400",
                "height": 123
            },
            "level_diff": {
                "id": 1,
                "winter": "1B",
                "summer": "2A",
                "autumn": "2B",
                "spring": "1B"
            },
            "beauty_title": "some words",
            "title": "sdfsd",
            "other_titles": "234",
            "connect": "asdfsd",
            "add_time": "2023-12-04T05:31:18.560720Z",
            "image": [],
            "status": "new"
            }

    > Результат метода: JSON
        *status — код HTTP, целое число:
            *500 — ошибка при выполнении операции;
            *400 — Bad Request (при нехватке полей);
            *200 — успех.
        *message — строка:
            *Причина ошибки (если она была);
            *Отправлено успешно;
            *Если отправка успешна, дополнительно возвращается id вставленной записи.
            *id — идентификатор, который был присвоен объекту при добавлении в базу данных.

            ***
            GET /submitData/{id} - получение данных о конкретном горном перевале с выводом всей информации
            ***
            PATCH /submitData/{id} - позволяет отредактировать существующую запись (замена), при условии, что она в статусе "new".
            Редактировать можно все поля, кроме тех, что содержат ФИО, адрес почты и номер телефона.
            ***
            GET /api/submitData/user__email=<str:email> - позволяет получить данные всех объектов, отправленных на сервер пользователем с почтой <***str:email***>.
            Фильтрация по адресу электронной почты реализуется с помощью пакета ***django-filter***.
При разработке проекта все требования и задачи были учтены и успешно выполнены.

About
Спринт№1 от SkillFactory

Resources
 Readme
 Activity
Stars
 0 stars
Watchers
 1 watching
Forks
 0 forks
Releases
No releases published
Create a new release
Packages
No packages published
Publish your first package
Footer
© 2024 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact
Manage cookies
Do not share my personal information
