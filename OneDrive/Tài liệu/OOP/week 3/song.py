import random as rd
class Song:
    def __init__(self, title, artist, album, duration, genre):
        self.title = title
        self.artist = artist
        self.album = album
        self.duration = duration 
        self.genre
        
    def play(self):
        print(f"{self.title}, {self.artist}, {self.album}, {self.duration}, {self.genre}")
        
    def __str__(self):
        return f"{self.title}, {self.artist}, {self.album}, {self.duration}, {self.genre}"

class Playlist:
    def __init__(self, name, current_song=0, shuffled=False):
        self.songs = []
        self.name = name
        self.current_song = current_song
        self.shuffled = shuffled
        
    def Add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)
        else:
            print("song cannot be added twice")
            
    def Remove_song(self, song):
        if song not in self.songs:
            print("song not in a list. Cannot remove")
        else:
            self.songs.remove(song)
            
    def Playing(self):
        print(f"{self.name} is being played")
        if self.shuffled == False:
            return self.songs[self.current_song]
        else:
            random_index = rd.randint(0, len(self.songs)-1)
            if random_index == self.current_song:
                random_index = rd.randint(0, len(self.songs)-1)
            random_song = self.songs[random_index]
            self.current_song = random_index
            return random_song

    def Next_track(self):
        self.current_song += 1
        return self.current_song
    
    def Previous_track(self):
        self.current_song -= 1
        return self.current_song
    
    def __str__(self):
        return f" List: {self.songs}\n Playlist: {self.name}\n Playing Song: {self.Playing()}\n Current song: {self.current_song}\n Shuffled: {self.shuffled}"  
          
playlist = Playlist("Happy Birthday collections", 0, True)
playlist.Add_song("happy0")
playlist.Remove_song("happy1")
playlist.Remove_song("happy2")
playlist.Remove_song("happy3")
playlist.Remove_song("happy4")


print(playlist)


