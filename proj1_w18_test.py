import unittest
import proj1_w18 as proj1
import json


class TestMedia(unittest.TestCase):

    file = "sample_json.txt"
    media_data = []
    with open(file) as inputData:
        for line in inputData:
            try:
                media_data.append(json.loads(line.rstrip("\n")))
            except ValueError:
                print("Skipping invalid line {0}".format(repr(line)))
    result_dict = proj1.classify_data(media_data)
    # print(result_dict["movie"][0])
    def setUp(self):

        self.mo2 =self.result_dict["movie"][0]
        self.me3 = self.result_dict["other media"][0]
        self.s2 = self.result_dict["song"][0]

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
        self.assertEqual(self.me3.title, "No Title")
        self.assertEqual(self.me3.author, "Helen Fielding")#__str__
        self.assertEqual(self.me3.__str__(), "No Title by Helen Fielding (2012)")  #
        self.assertEqual(self.me3.__len__(), 0)
        self.assertRaises(AttributeError, lambda: self.me3.rating)

    def testSong2(self):
        self.assertEqual(self.s2.title, "Hey Jude")
        self.assertEqual(self.s2.author, "The Beatles")
        self.assertEqual(self.s2.genre, "Rock")
        self.assertEqual(self.s2.release_year, "1968")
        self.assertEqual(self.s2.track_length, 431)
        self.assertEqual(self.s2.__str__(), "Hey Jude by The Beatles (1968)[Rock].")  #
        self.assertEqual(self.s2.__len__(), 431)
        self.assertRaises(AttributeError,lambda :self.s2.rating)

    def testMovie2(self):
        self.assertEqual(self.mo2.title,"Jaws")
        self.assertEqual(self.mo2.author, "Steven Spielberg")
        self.assertEqual(self.mo2.release_year, "1975")
        self.assertEqual(self.mo2.rating, "PG")
        self.assertEqual(self.mo2.__str__(), "Jaws by Steven Spielberg (1975)[PG].")  #
        self.assertEqual(self.mo2.__len__(), 124)

    def testData_from_iTunes(self):
        self.assertLessEqual(len(proj1.Data_from_iTunes("baby", 20).result_inst), 20)
        self.assertLessEqual(len(proj1.Data_from_iTunes("&@#!$", 20).result_inst), 20)
        self.assertLessEqual(len(proj1.Data_from_iTunes("helter skelter", 20).result_inst), 20)
        # semple = proj1.Data_from_iTunes("helter skelter", 20)
        # for each in sample



# The following is a line to run all of the tests you include:


if __name__ == "__main__":
    unittest.main(verbosity=2)

# verbosity 2 to see detail about the tests the code fails/passes/etc.
