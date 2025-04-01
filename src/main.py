import flet as ft
from components.app_bar import app_bar 
from components.mybutton import MyButton
from controls.containers import green_container, cl_test


from flet import  TextField

def main(page: ft.Page):
    page.func =lambda x: print(x)

    page.appbar = app_bar
    text_field = ft.TextField( label="Введите текст")

    mybutt = MyButton("Кнопка",lambda _:print('bla-bla'))
    # page.add(text_field)
    page.controls.append(text_field)
    page.controls.append(mybutt)

    page.add(green_container)

    page.update()
    page.control_dict={'tf':text_field}


if __name__ == "__main__":
    ft.app(target=main)