# template_tag

Доступ в административную панель: http://127.0.0.1:8000/admin

Логин: admin

Пароль: admin

Путь к запуску:

cd C:\template_tag\menu_project\menu> python manage.py makemigrations my_menu python manage.py migrate
python manage.py runserver

На главной странице представлено три варианта поведения отисовки меню, с возможностью пеехода по книгам. (Для просмотра нажимается плюс и минус соответственно)

{% draw_menu 'main_menu' %} - основное меню
{% draw_menu 'sub_menu' %} - подменю
Меню не добавленное в систему
