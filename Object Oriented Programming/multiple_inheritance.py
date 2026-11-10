class Camera:
    def take_photo(self):
        print("Photo captured successfully")

class MusicPlayer:
    def play_music(self):
        print("Playing music")

class SmartPhone(Camera, MusicPlayer):
    def show_features(self):
        print("Smartphone Features")
        self.take_photo()
        self.play_music()

device = SmartPhone()
device.show_features()
