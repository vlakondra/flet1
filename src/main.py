
import flet as ft
from controls.containers import red_container, blue_container,green_container

def main(page: ft.Page):
    page.appbar = ft.AppBar(
        title=ft.Text("Проект"),
        center_title=True,
        bgcolor=ft.Colors.BLUE,
    )
    
    # # Создаем три контейнера с разными цветами
    # red_container = ft.Container(
    #     bgcolor=ft.colors.RED,
    #     expand=True,
    #         content=ft.Row(
    #         [
    #             ft.ElevatedButton(text="Кнопка 1", expand=1),
    #             ft.ElevatedButton(text="Кнопка 2", expand=1),
    #             ft.ElevatedButton(text="Кнопка 3", expand=1),
    #         ]
    #     )
    # )
    
    # green_container = blue_container = ft.Container(
    #     bgcolor=ft.colors.GREEN,
    #     expand=True,
    #         content=ft.Row(
    #         [
    #             ft.ElevatedButton(text="Кнопка 1", expand=1),
    #             ft.ElevatedButton(text="Кнопка 2", expand=1),
    #             ft.ElevatedButton(text="Кнопка 3", expand=1),
    #         ]
    #     )
    # )
    
    # blue_container = ft.Container(
    #     bgcolor=ft.colors.BLUE,
    #     expand=True,
    #         content=ft.Row(
    #         [
    #             ft.ElevatedButton(text="Кнопка 1", expand=1),
    #             ft.ElevatedButton(text="Кнопка 2", expand=1),
    #             ft.ElevatedButton(text="Кнопка 3", expand=1),
    #         ]
    #     )
    # )
    
    # Словарь для хранения контейнеров
    containers = {
        "Красный": red_container,
        "Зеленый": green_container,
        "Синий": blue_container
    }
    
    # Функция для обновления отображаемого контейнера
    def update_container(e):
        selected_color = e.control.value
        page.controls[1] = containers[selected_color]  # Обновляем второй элемент управления
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
        label="Выберите контейнер"
    )
    
    # Добавляем элементы на страницу
    page.add(color_dropdown, red_container)  # Изначально показываем красный контейнер

if __name__ == "__main__":
    ft.app(target=main)