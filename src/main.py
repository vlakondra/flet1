import flet as ft
from utils import parse_questions

from conts import ff, example

def main(page: ft.Page):
    #Определим функцию для обработки результата выбора файла
    def on_dialog_result(e: ft.FilePickerResultEvent):
        if e.files:
            #разберем файл с вопросами
            quests = parse_questions(e.files[0].path)    
            print(quests) 
            return quests 

    #Добавим FilePicker c обработчиком события выбора
    file_picker = ft.FilePicker(on_result = on_dialog_result)
    page.overlay.append(file_picker)
    page.update()

    #Добавим кнопку с обработчиком события для его вызова
    file_type = ft.FilePickerFileType.CUSTOM
    page.add(ft.ElevatedButton("Выберите файл...",
    on_click=lambda _: file_picker.pick_files(file_type=file_type,  dialog_title='File', allowed_extensions=['txt'],  allow_multiple=False)))

    if file_picker.result:
        print('RES!!')
    #Определим функцию для обработки результата выбора файла
    # def on_dialog_result(e: ft.FilePickerResultEvent):
    #     if e.files:
    #         #разберем файл с вопросами
    #         quests = parse_questions(e.files[0].path)    
    #         print(quests)    


    def check_item_clicked(e):

        e.control.checked = not e.control.checked
        page.update()

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.Icons.PALETTE),
        leading_width=40,
        title=ft.Text("AppBar Example" +str(ff())),
        center_title=False,
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        actions=[
            ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED),
            ft.IconButton(ft.Icons.FILTER_3),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Item 1"),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text="Checked item", checked=False, on_click=check_item_clicked
                    ),
                ]
            ),
        ],
    )
    page.add(ft.Text("Body!"))
    # cont.content=(ft.Text("qwe"))
    # cont.width = 900
    # page.add(cont)



ft.app(main)