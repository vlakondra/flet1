import flet as ft
red_container = ft.Container(
        bgcolor=ft.colors.RED,
        padding=50,
        expand=True,
            content=ft.Row(
            [
                ft.ElevatedButton(text="Кнопка 1", expand=1),
                ft.ElevatedButton(text="Кнопка 2", expand=1),
                ft.ElevatedButton(text="Кнопка 3", expand=1),
            ]
        )
    )

green_container = blue_container = ft.Container(
        bgcolor=ft.colors.GREEN,
        padding=100,
        expand=True,
            content=ft.Row(
            [
                ft.ElevatedButton(text="Кнопка 1", expand=1),
                ft.ElevatedButton(text="Кнопка 2", expand=1),

            ]
        )
    )

blue_container = ft.Container(
        bgcolor=ft.colors.BLUE,
        expand=True,
            content=ft.Row(
            [
                ft.ElevatedButton(text="Кнопка 2", width=150),
            ]
        )
    )
