import flet as ft

from utils import parse_questions
from conts import menubar #,handle_color_click

def main(page: ft.Page):
    #Добавим главное меню
    page.add(
        ft.Row([menubar],rotate=0)
        )

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

    #Добавим кнопку  вызова file_picker
    file_type = ft.FilePickerFileType.CUSTOM
    page.add(ft.ElevatedButton("Открыть тест...",
    on_click=lambda _: file_picker.pick_files(file_type=file_type,  dialog_title='File', allowed_extensions=['txt'],  allow_multiple=False)))


    mbc = menubar.controls[0]
    sm = mbc.controls[0]
    sm.on_click = lambda _: file_picker.pick_files(file_type=file_type,  dialog_title='File', allowed_extensions=['txt'],  allow_multiple=False)#handle_color_click1


ft.app(main)