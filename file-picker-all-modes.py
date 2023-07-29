import flet as ft
from flet import (
    ElevatedButton,
    FilePicker,
    FilePickerResultEvent,
    Page,
    Row,
    Text,
    icons,
)


def main(page: Page):
    # Pick files dialog
    def pick_files_result(e: FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        selected_files.update()

    pick_files_dialog = FilePicker(on_result=pick_files_result)
    selected_files = Text()

    # Save file dialog
    def save_file_result(e: FilePickerResultEvent):
        save_file_path.value = e.path if e.path else "Cancelled!"
        save_file_path.update()

    save_file_dialog = FilePicker(on_result=save_file_result)
    save_file_path = Text()

    # Open directory dialog
    def get_directory_result(e: FilePickerResultEvent):
        directory_path.value = e.path if e.path else "Cancelled!"
        directory_path.update()

    get_directory_dialog = FilePicker(on_result=get_directory_result)
    directory_path = Text()

    # hide all dialogs in overlay
    page.overlay.extend([pick_files_dialog, save_file_dialog, get_directory_dialog])

    page.add(
        Row(
            [
                ElevatedButton(
                    "Pick files",
                    icon=icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=True
                    ),
                ),
                selected_files,
            ]
        ),
        Row(
            [
                ElevatedButton(
                    "Save file",
                    icon=icons.SAVE,
                    on_click=lambda _: save_file_dialog.save_file(),
                    disabled=page.web,
                ),
                save_file_path,
            ]
        ),
        Row(
            [
                ElevatedButton(
                    "Open directory",
                    icon=icons.FOLDER_OPEN,
                    on_click=lambda _: get_directory_dialog.get_directory_path(),
                    disabled=page.web,
                ),
                directory_path,
            ]
        ),
    )

    i = ft.Image(src="https://picsum.photos/150/150", width=500, height=500)

    page.add(i)

    page.client_storage.set("key", "value")
    page.client_storage.set("number.settings", 12345)
    page.client_storage.set("bool_setting", True)
    page.client_storage.set("favorite_colors", ["red", "green", "blue"])
    
    value = page.client_storage.get("key")
    
    colors = page.client_storage.get("favorite_colors")
    print(colors)
    
    # import os
    # from flet.security import encrypt, decrypt
    
    # secret_key = os.getenv("MY_APP_SECRET_KEY")
    
    # plain_text = "This is a secret message"
    # encrypted_text = encrypt(plain_text, secret_key)
    # print(encrypted_text)
    # decrypted_text = decrypt(encrypted_text, secret_key)
    # print(decrypted_text)
   
    page.clean()
    
    page.title = "Flet Chat"
    
    messages = ft.Column()
    
    def on_message(msg):
        messages.controls.append(ft.Text(msg))
        page.update()
        
    page.pubsub.subscribe(on_message)
    
    def send_click(e):
        page.pubsub.send_all(f"{user.value}: {message.value}")
        
        message.value = ""
        page.update()
        
    user = ft.TextField(hint_text="Your name", width=150)
    message = ft.TextField(hint_text="Your message...", expand=True)
    send = ft.ElevatedButton("Send", on_click=send_click)
    page.add(messages, ft.Row(controls=[user, message, send]))
    page.update()


ft.app(target=main, view = ft.AppView.WEB_BROWSER)