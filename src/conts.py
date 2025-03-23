import flet as ft

def ff():
    '''test'''

    return 333



def example():

    container_1 = ft.Container(
        content=ft.Text("Center"),
        alignment=ft.alignment.center,
        bgcolor=ft.Colors.BLUE_GREY_100,
        width=150,
        height=150,
    )
    return container_1