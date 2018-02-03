import json

class Media:

    def __init__(self, title="No Title", author="No Author",release_year=1999,json =None):
        self.title = title
        self.author = author
        self.release_year = release_year
        # the whole dictionary:
        self.json= json
        # update the data in class:
        self.media_data()

    def media_data(self):
        if self.json is not None:
            if "trackName" in self.json:
                self.title = self.json["trackName"]
            if "artistName" in self.json:
                self.author = self.json["artistName"]
            if "artistName" in self.json:
                self.release_year = self.json["releaseDate"][0:4]
            # print(self.title,self.author,self.release_year)

    def __str__(self):
        string_of_media = "{} by {} ({})".format(self.title,self.author,self.release_year)
        return string_of_media

    def __len__(self):
        return 0

class Song(Media):
    def __init__(self,title="No Title", author="No Author",release_year=1999,
                 album="No Album", track_length=0,genre = "No Genre",json =None):
        super().__init__(title, author, release_year,json)
        self.album = album
        self.track_length = round(track_length / 1000)
        self.genre = genre
        self.song_data()

    def song_data(self):
        if self.json is not None:
            if "collectionName" in self.json:
                self.album = self.json["collectionName"]
            if "trackTimeMillis" in self.json:
                self.track_length = round(int(self.json["trackTimeMillis"])/1000)
            if "primaryGenreName" in self.json:
                self.genre = self.json["primaryGenreName"]
    def __str__(self):
        string_of_media = super().__str__()+"[{}].".format(self.genre)
        return string_of_media
    def __len__(self):
        # return track length in seconds

        return self.track_length

class Movie(Media):
    def __init__(self,title="No Title", author="No Author",
                 release_year=1999,rating = "No Rating",movie_length=0,json =None):
        super().__init__(title, author, release_year,json)
        self.rating = rating
        self.movie_length = round(movie_length / 60000)
        self.movie_data()

    def movie_data(self):
        if self.json is not None:
            if "contentAdvisoryRating" in self.json:
                self.rating = self.json["contentAdvisoryRating"]
            else:
                print("something wrong with rting")
            if "trackTimeMillis" in self.json:
                self.movie_length = round(int(self.json["trackTimeMillis"])/60000)
    def __str__(self):
        string_of_media = super().__str__() + "[{}].".format(self.rating)
        return string_of_media
    def __len__(self):
        """""""return movie length in minutes (rounded to nearest minute)"""

        return self.movie_length

if __name__ == "__main__":
    pass
    # your control code for Part 4 (interactive search) should go here
    # media = Media()
    # song = Song(track_length=12000)
    # print(song.__len__())