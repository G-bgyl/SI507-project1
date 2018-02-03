import unittest
import proj1_w18 as proj1
import json

#*************************** Begin of part 2***************************
file = "sample_json.txt"
media_data = []
with open(file) as inputData:
    for line in inputData:
        try:
            media_data.append(json.loads(line.rstrip("\n")))
        except ValueError:
            print("Skipping invalid line {0}".format(repr(line)))

for each in media_data:
    # print(type(each))
    if "kind" in each:
        if each["kind"] == "feature-movie":
            mo2 = proj1.Movie(json = each)
            # print(mo2)
            # print(mo2.__len__())
        elif each["kind"] == "song":
            s2 = proj1.Song(json = each)
            # print(s2)
            # print(s2.__len__())
    else:
        me3 = proj1.Media(json = each)
        # print(me3)
        # print(me3.__len__())

#*************************** End of part 2***************************

class TestMedia(unittest.TestCase):

    def testMedia(self):
        me1 = proj1.Media()
        me2 = proj1.Media("1999", "Prince", 1980)

        self.assertEqual(me1.title, "No Title")
        self.assertEqual(me1.author, "No Author")
        self.assertEqual(me2.title, "1999")
        self.assertEqual(me2.author, "Prince")#__str__
        self.assertEqual(me2.__str__(), "1999 by Prince (1980)")  #
        self.assertEqual(me2.__len__(), 0)

        self.assertRaises(AttributeError, lambda: me1.rating)

    def testSong(self):
        s1=proj1.Song(title="Just a Dream", author="Sam Tsui",
                      release_year=2011, album="Just A Dream",
                      track_length=120000, genre="Hip hop")
        self.assertEqual(s1.title, "Just a Dream")
        self.assertEqual(s1.author, "Sam Tsui")
        self.assertEqual(s1.genre, "Hip hop")
        self.assertEqual(s1.release_year, 2011)
        self.assertEqual(s1.track_length, 120)
        self.assertEqual(s1.__str__(), "Just a Dream by Sam Tsui (2011)[Hip hop].")  #
        self.assertEqual(s1.__len__(), 120)
        self.assertRaises(AttributeError,lambda :s1.rating)


    def testMovie(self):
        mo1 = proj1.Movie(title="Lady Bird", author="Greta Gerwig",
                 release_year="2017", rating="R", movie_length=5580000)
        self.assertEqual(mo1.title,"Lady Bird")
        self.assertEqual(mo1.author, "Greta Gerwig")
        self.assertEqual(mo1.release_year, "2017")
        self.assertEqual(mo1.rating, "R")
        self.assertEqual(mo1.__str__(), "Lady Bird by Greta Gerwig (2017)[R].")  #
        self.assertEqual(mo1.__len__(), 93)

    def testMedia2(self):


        self.assertEqual(me3.title, "No Title")
        self.assertEqual(me3.author, "Helen Fielding")#__str__
        self.assertEqual(me3.__str__(), "No Title by Helen Fielding (2012)")  #
        self.assertEqual(me3.__len__(), 0)

        self.assertRaises(AttributeError, lambda: me3.rating)

    def testSong2(self):

        self.assertEqual(s2.title, "Hey Jude")
        self.assertEqual(s2.author, "The Beatles")
        self.assertEqual(s2.genre, "Rock")
        self.assertEqual(s2.release_year, "1968")
        self.assertEqual(s2.track_length, 431)
        self.assertEqual(s2.__str__(), "Hey Jude by The Beatles (1968)[Rock].")  #
        self.assertEqual(s2.__len__(), 431)
        self.assertRaises(AttributeError,lambda :s2.rating)


    def testMovie2(self):
        self.assertEqual(mo2.title,"Jaws")
        self.assertEqual(mo2.author, "Steven Spielberg")
        self.assertEqual(mo2.release_year, "1975")
        self.assertEqual(mo2.rating, "PG")
        self.assertEqual(mo2.__str__(), "Jaws by Steven Spielberg (1975)[PG].")  #
        self.assertEqual(mo2.__len__(), 124)
## The following is a line to run all of the tests you include:
if __name__ == "__main__":
    unittest.main(verbosity=2)
## verbosity 2 to see detail about the tests the code fails/passes/etc.
