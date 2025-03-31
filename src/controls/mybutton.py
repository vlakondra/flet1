"""import flet"""
import flet as ft
class MyButton(ft.ElevatedButton):
    '''button'''
    def __init__(self, text,onclick):
        super().__init__()
        self.bgcolor = ft.Colors.ORANGE_300
        self.color = ft.Colors.GREEN_800
        self.text = text
        self.on_click = onclick
        