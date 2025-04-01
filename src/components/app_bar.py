import flet as ft
from flet import AppBar,Ref
from flet.core.control_event import Event
from flet.core.types import EventType

def check_item_clicked(e):
    e.control.checked = not e.control.checked
    print('dict',e.page.control_dict)
    tf = e.page.controls[0] 
    tf.value += 'qwerty'
    e.page.update()
 
def test_click(e):
    print("Button clicked")

app_bar:AppBar = ft.AppBar(
    leading=ft.Icon(ft.Icons.PALETTE),
    leading_width=40,
    title=ft.Text("Простой AppBar"),
    center_title=False,
    bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
    actions=[
        ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED,on_click = test_click),
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
