class MediaFile:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def play(self):
        pass

class AudioFile(MediaFile):
    def play(self):
        print(f"Воспроизводится аудио: {self.title}, длительность {self.duration} минут")

class VideoFile(MediaFile):
    def play(self):
        print(f"Воспроизводится видео с изображением: {self.title}, длительность {self.duration} минут")

class Podcast(MediaFile):
    def play(self):
        print(f"Воспроизводится эпизод подкаста: {self.title}, длительность {self.duration} минут")

a = AudioFile("Песня", 2)
v = VideoFile("Фильм", 99)
p = Podcast("Эпизод №1", 66)

a.play()
v.play()
p.play()