import requests
from tkinter import Tk, Toplevel, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO

def get_random_dog_image():
    try:
        response = requests.get('https://dog.ceo/api/breeds/image/random')
        response.raise_for_status()
        data = response.json()
        return data['message']
    except requests.RequestException as e:
        messagebox.showerror("Ошибка", f"Ошибка при запросе к API: {e}")
        return None

def show_image():
    image_url = get_random_dog_image()

    if image_url:
        try:
            response = requests.get(image_url, stream=True)
            response.raise_for_status()
            img_data = BytesIO(response.content)
            img = Image.open(img_data)
            img_size = (int(width_spinbox.get()), int(height_spinbox.get()))
            img.thumbnail(img_size)
            img = ImageTk.PhotoImage(img)

            new_window = Toplevel(window)
            new_window.title("Случайное изображение пёсика")
            label = ttk.Label(new_window, image=img)
            label.image = img
            label.pack(padx=10, pady=10)

        except requests.RequestException as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить изображение: {e}")

def start_progress():
    progress['value'] = 0
    progress.start(30)
    window.after(3000, lambda: [progress.stop(), show_image()])

window = Tk()
window.title("Случайное изображение")

button = ttk.Button(window, text="Загрузить изображение", command=start_progress)
button.pack(padx=10, pady=10)

progress = ttk.Progressbar(window, mode='determinate', length=300)
progress.pack(padx=10, pady=5)


# Ширина
width_label = ttk.Label(text="Ширина:")
width_label.pack(side='left', padx=(10, 0))
width_spinbox = ttk.Spinbox(from_=200, to=500, increment=50, width=5)
width_spinbox.pack(side='left', padx=(0, 10))

# Высота
height_label = ttk.Label(text="Высота:")
height_label.pack(side='left', padx=(10, 0))
height_spinbox = ttk.Spinbox(from_=200, to=500, increment=50, width=5)
height_spinbox.pack(side='left', padx=(0, 10))


def show_image():
    try:
        # Получаем значения и удаляем возможные пробелы
        width_str = width_spinbox.get().strip()
        height_str = height_spinbox.get().strip()

        # Проверяем, что строки не пустые
        if not width_str or not height_str:
            raise ValueError("Поля ширины и высоты не могут быть пустыми")

        # Преобразуем в целые числа
        width = int(width_str)
        height = int(height_str)

        # Теперь можно использовать width и height
        img_size = (width, height)
        # ... остальной код ...

    except ValueError as e:
        # Обрабатываем ошибку: показываем сообщение пользователю
        messagebox.showerror("Ошибка ввода", f"Некорректный ввод: {e}. Введите целые числа.")

window.mainloop()




