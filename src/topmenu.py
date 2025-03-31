import flet as ft

def handle_on_hover(e):
    print(f"{e.control.content.value}.on_hover")

def handle_file_click(e):
    print(f"{e.control.content.value}.on_click")

def handle_exit_click(e) -> None:
    print(f"{e.control.content.value}.on_click")

menubar = ft.MenuBar(
        expand=True,
        controls=[
            ft.SubmenuButton(
                content=ft.Text("Файл"),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Открыть тест"),
                        leading=ft.Icon(ft.Icons.FILE_DOWNLOAD),
                        style=ft.ButtonStyle(bgcolor={ft.ControlState.PRESSED: ft.Colors.BLUE_200}),
                        on_click=handle_file_click,
                        on_hover=handle_on_hover,
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Green"),
                        leading=ft.Icon(ft.Icons.COLORIZE),
                        style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.Colors.GREEN}),
                        #on_click=handle_color_click,
                        on_hover=handle_on_hover,
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Выход"),
                        leading=ft.Icon(ft.Icons.EXIT_TO_APP),
                        style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.Colors.RED}),
                        on_click=handle_exit_click,
                        on_hover=handle_on_hover,)
                ])
            ,ft.SubmenuButton(content=ft.Text('Правка')
                              ,controls=[
                                     ft.MenuItemButton(
                        content=ft.Text("Открыть тест"),
                        leading=ft.Icon(ft.Icons.FILE_DOWNLOAD),
                        style=ft.ButtonStyle(bgcolor={ft.ControlState.PRESSED: ft.Colors.BLUE_200}),
                        on_click=handle_file_click,
                        on_hover=handle_on_hover,
                    ),])
    ]
)