import unittest
import proj1_w18 as proj1

class TestMedia(unittest.TestCase):

    def testMedia(self):
        m1 = proj1.Media()
        m2 = proj1.Media("1999", "Prince", 1980)

        self.assertEqual(m1.title, "No Title")
        self.assertEqual(m1.author, "No Author")
        self.assertEqual(m2.title, "1999")
        self.assertEqual(m2.author, "Prince")#__str__
        self.assertEqual(m2.__str__(), "1999 by Prince (1980)")  #
        self.assertEqual(m2.__len__(), 0)

        self.assertRaises(AttributeError, lambda: m1.rating)

    def testSong(self):
        s1=proj1.Song(title="Just a Dream", author="Sam Tsui",
                      release_year=2011, album='Just A Dream',
                      track_length=120, genre="Hip hop")
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
                 release_year=2017, rating='R', movie_length=93)
        self.assertEqual(mo1.title,"Lady Bird")
        self.assertEqual(mo1.author, "Greta Gerwig")
        self.assertEqual(mo1.release_year, 2017)
        self.assertEqual(mo1.rating, 'R')
        self.assertEqual(mo1.__str__(), "Lady Bird by Greta Gerwig (2017)[R].")  #
        self.assertEqual(mo1.__len__(), 93)


## The following is a line to run all of the tests you include:
if __name__ == "__main__":
    unittest.main(verbosity=2)
## verbosity 2 to see detail about the tests the code fails/passes/etc.
