'''qwe  rty'''
import flet as ft

# from controls.containers import red_container, blue_container,green_container


def main(page: ft.Page):
    """'qwe rty"""
    # page.appbar = ft.AppBar(
    #     title=ft.Text("Проект"),
    #     center_title=True,
    #     bgcolor=ft.Colors.BLUE,
    # )
    # page.appbar = ft.CupertinoAppBar(
    #     ft.Text('bla-bla'), leading=ft.IconButton(ft.icons.ARROW_BACK)
    # )

    page.appbar = ft.AppBar(
        leading=ft.IconButton(ft.Icons.ARROW_BACK),
        title=ft.Text("Пример AppBar"),
         bgcolor=ft.Colors.BLUE,
        actions=[
            ft.IconButton(ft.Icons.SEARCH),
            ft.IconButton(ft.Icons.MORE_VERT),
        ]
    )


    # Создаем три контейнера с разными цветами
    red_container = ft.Container(
        bgcolor=  ft.Colors.BLUE_200,
        expand=True,
        content=ft.Row(
            [
                ft.ElevatedButton(text="Кнопка 1", expand=1),
                ft.ElevatedButton(text="Кнопка 2", expand=1),
                ft.ElevatedButton(text="Кнопка 3", expand=1),
            ]
        ),
    )

    green_container = blue_container = ft.Container(
        bgcolor=ft.Colors.GREEN,
        expand=True,
        content=ft.Row(
            [
                ft.ElevatedButton(text="Кнопка 1", expand=1),
                ft.ElevatedButton(text="Кнопка 2", expand=1),
                ft.ElevatedButton(text="Кнопка 3", expand=1),
            ]
        ),
    )

    blue_container = ft.Container(
        bgcolor=ft.Colors.BLUE,
        expand=True,
        content=ft.Row(
            [
                ft.ElevatedButton(text="Кнопка 1", expand=1),
                ft.ElevatedButton(text="Кнопка 2", expand=1),
                ft.ElevatedButton(text="Кнопка 3", expand=1),
            ]
        ),
    )

    # Словарь для хранения контейнеров
    containers = {
        "Красный": red_container,
        "Зеленый": green_container,
        "Синий": blue_container,
    }

    # Функция для обновления отображаемого контейнера
    def update_container(e):
        selected_color = e.control.value
        page.controls[1] = containers[
            selected_color
        ]  # Обновляем второй элемент управления
        page.update()  # Обновляем страницу

    # Создаем выпадающее меню для выбора цвета
    color_dropdown = ft.Dropdown(
        width=300,
        options=[
            ft.dropdown.Option("Красный"),
            ft.dropdown.Option("Зеленый"),
            ft.dropdown.Option("Синий"),
        ],
        on_change=update_container,
        label="Выберите контейнер",
    )

    # Добавляем элементы на страницу
    # Изначально показываем красный контейнер
    page.add(color_dropdown, red_container)


if __name__ == "__main__":
    ft.app(target=main)
