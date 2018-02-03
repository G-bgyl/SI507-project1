import json

class Media:

    def __init__(self, title="No Title", author="No Author",release_year=1999,json = "sample_json.txt"):
        self.title = title
        self.author = author
        self.release_year = release_year
        self.json= json
        self.data_dict = self.media_data()
    def media_data(self):
        media_data = []
        with open(self.json) as inputData:
            for line in inputData:
                try:
                    media_data.append(json.loads(line.rstrip('\n')))
                except ValueError:
                    print("Skipping invalid line {0}".format(repr(line)))

        for each in media_data:
            if 'trackName' in each:
                self.title = each['trackName']
            if 'artistName' in each:
                self.author = each['artistName']
            if 'artistName' in each:
                self.release_year = each['releaseDate'][0:4]
            # print(self.title,self.author,self.release_year)


    def __str__(self):
        string_of_media = '{} by {} ({})'.format(self.title,self.author,self.release_year)
        return string_of_media

    def __len__(self):
        return 0

class Song(Media):
    def __init__(self,title="No Title", author="No Author",release_year=1999,
                 album='No Album', track_length=0,genre = 'No Genre'):
        super().__init__(title, author, release_year)
        self.album = album
        self.track_length = track_length
        self.genre = genre

    def song_data(self):
        for each in self.data_dict:
            if 'collectionName' in each:
                self.album = each['collectionName']
            if 'trackTimeMillis' in each:
                self.track_length = each['trackTimeMillis']
            if 'primaryGenreName' in each:
                self.genre = each['primaryGenreName']
    def __str__(self):
        string_of_media = super().__str__()+'[{}].'.format(self.genre)
        return string_of_media
    def __len__(self):
        # return track length in seconds
        length = round(self.track_length/1000)
        return self.track_length

class Movie(Media):
    def __init__(self,title="No Title", author="No Author",
                 release_year=1999,rating = 'No Rating',movie_length=0):
        super().__init__(title, author, release_year)
        self.rating = rating
        self.movie_length = movie_length

    def movie_data(self):
        for each in self.data_dict:
            if 'contentAdvisoryRating' in each:
                self.rating = each['contentAdvisoryRating']
            if 'trackTimeMillis' in each:
                self.movie_length = each['trackTimeMillis']
    def __str__(self):
        string_of_media = super().__str__() + '[{}].'.format(self.rating)
        return string_of_media
    def __len__(self):
        '''return movie length in minutes (rounded to nearest minute)'''
        length = round(self.movie_length/60000)
        return self.movie_length

if __name__ == "__main__":
    # your control code for Part 4 (interactive search) should go here
    media = Media()
