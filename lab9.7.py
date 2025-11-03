class TextFile:
    def open(self):
        print("Открыт текстовый файл. Отображается содержимое текста")

class ImageFile:
    def open(self):
        print("Открыт графический файл. Показано изображение")

class AudioFile:
    def open(self):
        print("Открыт аудиофайл. Воспроизведение звука началось")

def open_all(files):
    for f in files:
        f.open()

if __name__ == "__main__":
    files = [TextFile(), ImageFile(), AudioFile()]
    open_all(files)