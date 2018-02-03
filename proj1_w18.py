import json
import requests
import webbrowser

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
            if "trackViewUrl" in self.json:
                self.trackViewURL = self.json["trackViewUrl"]
            elif "previewUrl" in self.json:
                self.trackViewURL = self.json["previewUrl"]
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

#*************************** Begin Part 2 ***************************
def classify_data(media_data):
    result_dict ={"song":[],"movie":[],"other media":[]}
    i=0
    for each in media_data:
        i+=1
        # print(type(each))
        if "kind" in each:
            if each["kind"] == "feature-movie":
                mo2 = Movie(json = each)
                result_dict["movie"].append(mo2)
                # print(mo2)
                # print('the length of ',mo2.title,':',mo2.__len__())
                # print("\n")
            elif each["kind"] == "song":
                s2 = Song(json = each)
                result_dict["song"].append(s2)
                # print(s2)
                # print('the length of ',s2.title,':',s2.__len__())
                # print("\n")
        else:
            me3 = Media(json = each)
            # print(me3)
            # print('the length of ',me3.title,':',me3.__len__())
            # print("\n")
            result_dict["other media"].append(me3)
    return result_dict



#*************************** End of part 2 ***************************

#*************************** Begin Part 3 ****************************
class Data_from_iTunes ():
    def __init__(self,keyword,num):
        #print(most_common_word)
        self.result_inst={}
        if keyword== ' ' or keyword =='':
            self.keyword='blank'
        else:
            self.keyword= keyword
        self.num = num
        self.get_from_itunes()


    def get_from_itunes(self):
        base_url = "https://itunes.apple.com/search"
        parameters= {}
        parameters['term']=self.keyword
        parameters['limit'] = self.num
        # parameters['entity']= "song"
        result = requests.get(base_url, params =parameters)
        self.result_inst = json.loads(result.text)['results']
        # print(self.result_inst)


if __name__ == "__main__":

    # input:
    keyword = input("please input key word, or type \"exit\" for quit:")

    exit=False
    while not exit:

        if keyword == 'exit':
            exit = True
            break

        else:


            correct = False

            num = input("please input number of results you want to display(no bigger than 100):")
            try:
                num = int(num)
                correct = True
            except:
                num = input("Please type in valid number:")

            while not correct:
                try:
                    num = int(num)
                    correct = True
                except:
                    num = input("Please type in valid number:")

            # process data
            target_data = Data_from_iTunes(keyword, num).result_inst
            print("\n")
            dict = classify_data(target_data)
            # print result
            j = 0
            result = []
            for each in dict:
                print("There are {} {}s.".format(len(dict[each]),each))
                for i in range(len(dict[each])):
                    j += 1
                    result.append(dict[each][i])
                    print(j,dict[each][i])
                print('\n')
            stop = False
            while not stop:
                keyword = input("Enter a number for more info, or another search term, or exit:")
                if keyword == 'exit':
                    stop= True
                    exit = True
                    break
                elif keyword.isdigit():
                    url =result[int(keyword)-1].trackViewURL
                    print('Launching',url,"\n in web browser...")
                    webbrowser.open(url)
                else:
                    stop = True

    print("Bye!")



    # your control code for Part 4 (interactive search) should go here
    # media = Media()
    # song = Song(track_length=12000)
    # print(song.__len__())