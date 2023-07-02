#OOPPLAYLIST
class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.albums = []
        self.artist = artist
        self.duration = duration

    def __str__(self):
        return f"Title: {self.title}\nArtist: {self.artist}\nDuration: {self.duration} minutes"

class Playlist:
    def __init__(self, name, max_songs):
        self.name = name
        self.songs = []
        self.max_songs = max_songs

    def __str__(self):
        return f"Playlist Name: {self.name}\nNumber of Songs: {len(self.songs)}\nMax Songs: {self.max_songs}"

    def add_song(self, song):
        if len(self.songs) < self.max_songs:
            self.songs.append(song)
            song.albums.append(self)
            print(f"{song.title} added to {self.name} playlist.")
        else:
            print(f"Not enough space in {self.name} playlist.")

    def __add__(self, other):
        joined_playlist = Playlist(f"{self.name} + {other.name}", self.max_songs + other.max_songs)
        joined_playlist.songs = self.songs + other.songs
        return joined_playlist

# Example usage
song1 = Song("Song 1", "Artist 1", 3)
song2 = Song("Song 2", "Artist 2", 4)
song3 = Song("Song 3", "Artist 3", 5)
song4 = Song("Song 4", "Artist 4", 3)

playlist1 = Playlist("Playlist 1", 3)
playlist1.add_song(song1)
playlist1.add_song(song2)

playlist2 = Playlist("Playlist 2", 2)
playlist2.add_song(song3)
playlist2.add_song(song4)

print(playlist1)
print(playlist2)

joined_playlist = playlist1 + playlist2
print(joined_playlist)












#PARSERGOOGLE
import requests
from bs4 import BeautifulSoup
import os

# Read the HTML file
with open("sample.html") as file:
    html_content = file.read()

# Extract university names using Beautiful Soup
soup = BeautifulSoup(html_content, "html.parser")
university_list = []

# Find all the elements on the left side containing university names
university_elements = soup.select(".left-side .university")
for element in university_elements:
    university_list.append(element.text)

print("University Names:")
for university in university_list:
    print(university)

# Save the Google logo link
google_logo_link = soup.select_one("#google-logo").get("src")
print("Google Logo Link:", google_logo_link)

# Retrieve and save the image
response = requests.get(google_logo_link)
if response.status_code == 200:
    with open("google_logo.png", "wb") as image_file:
        image_file.write(response.content)
        print("Image saved successfully as google_logo.png.")
else:
    print("Failed to retrieve the image.")














#PARSERBTU
import requests
from bs4 import BeautifulSoup

# Read the HTML file
with open("sample.html") as file:
    html_content = file.read()

# Extract training programs using Beautiful Soup
soup = BeautifulSoup(html_content, "html.parser")
training_programs = []

# Find all elements containing training program information
program_elements = soup.select(".training-program")
for element in program_elements:
    training_programs.append(element.text)

print("Training Programs:")
for program in training_programs:
    print(program)

# Save the BTU logo link
btu_logo_link = soup.select_one("#btu-logo").get("src")
print("BTU Logo Link:", btu_logo_link)

# Retrieve and save the image
response = requests.get(btu_logo_link)
if response.status_code == 200:
    with open("btu_logo.png", "wb") as image_file:
        image_file.write(response.content)
        print("Image saved successfully as btu_logo.png.")
else:
    print("Failed to retrieve the image.")
