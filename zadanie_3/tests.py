import unittest
from hamcrest import *
from function import dawaj_give, song_text, song_list

class DawajGiveTest(unittest.TestCase):

    testing = "test_whole_song"

    def setUp(self):
        self.temp = dawaj_give
    
    # one verse tests
    @unittest.skipIf(testing!= "test_one_verse" and testing!="all", "TDD")
    def test_one_verse_1(self):
        assert_that(self.temp(1), is_(song_list[0]))
    @unittest.skipIf(testing!= "test_one_verse" and testing!="all", "TDD")
    def test_one_verse_2(self):
        assert_that(self.temp(2), is_(song_list[1]))
    @unittest.skipIf(testing!= "test_one_verse" and testing!="all", "TDD")
    def test_one_verse_3(self):
        assert_that(self.temp(3), is_(song_list[2]))
    @unittest.skipIf(testing!= "test_one_verse" and testing!="all", "TDD")
    def test_one_verse_4(self):
        assert_that(self.temp(4), is_(song_list[3]))
    @unittest.skipIf(testing!= "test_one_verse" and testing!="all", "TDD")
    def test_one_verse_5(self):
        assert_that(self.temp(5), is_(song_list[4]))
    @unittest.skipIf(testing!= "test_one_verse" and testing!="all", "TDD")
    def test_one_verse_6(self):
        assert_that(self.temp(6), is_(song_list[5]))
    @unittest.skipIf(testing!= "test_one_verse" and testing!="all", "TDD")
    def test_one_verse_7(self):
        assert_that(self.temp(7), is_(song_list[6]))
    @unittest.skipIf(testing!= "test_one_verse" and testing!="all", "TDD")
    def test_one_verse_8(self):
        assert_that(self.temp(8), is_(song_list[7]))
    @unittest.skipIf(testing!= "test_one_verse" and testing!="all", "TDD")
    def test_one_verse_9(self):
        assert_that(self.temp(9), is_(song_list[8]))
    @unittest.skipIf(testing!= "test_one_verse" and testing!="all", "TDD")
    def test_one_verse_10(self):
        assert_that(self.temp(10), is_(song_list[9]))
    @unittest.skipIf(testing!= "test_one_verse" and testing!="all", "TDD")
    def test_one_verse_11(self):
        assert_that(self.temp(11), is_(song_list[10]))
    @unittest.skipIf(testing!= "test_one_verse" and testing!="all", "TDD")
    def test_one_verse_12(self):
        assert_that(self.temp(12), is_(song_list[11]))
    
    # verses from a to b tests
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_1_to_2(self):
        assert_that(self.temp(1, 2), is_(song_list[0]+'\n\n'+song_list[1]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_1_to_3(self):
        assert_that(self.temp(1, 3), is_(song_list[0]+'\n\n'+song_list[1]+'\n\n'+song_list[2]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_1_to_4(self):
        assert_that(self.temp(1, 4), is_(song_list[0]+'\n\n'+song_list[1]+'\n\n'+song_list[2]+'\n\n'+song_list[3]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_1_to_5(self):
        assert_that(self.temp(1, 5), is_(song_list[0]+'\n\n'+song_list[1]+'\n\n'+song_list[2]+'\n\n'+song_list[3]+'\n\n'+song_list[4]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_1_to_6(self):
        assert_that(self.temp(1, 6), is_(song_list[0]+'\n\n'+song_list[1]+'\n\n'+song_list[2]+'\n\n'+song_list[3]+'\n\n'+song_list[4]+'\n\n'+song_list[5]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_1_to_7(self):
        assert_that(self.temp(1, 7), is_(song_list[0]+'\n\n'+song_list[1]+'\n\n'+song_list[2]+'\n\n'+song_list[3]+'\n\n'+song_list[4]+'\n\n'+song_list[5]+'\n\n'+song_list[6]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_1_to_8(self):
        assert_that(self.temp(1, 8), is_(song_list[0]+'\n\n'+song_list[1]+'\n\n'+song_list[2]+'\n\n'+song_list[3]+'\n\n'+song_list[4]+'\n\n'+song_list[5]+'\n\n'+song_list[6]+'\n\n'+song_list[7]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_1_to_9(self):
        assert_that(self.temp(1, 9), is_(song_list[0]+'\n\n'+song_list[1]+'\n\n'+song_list[2]+'\n\n'+song_list[3]+'\n\n'+song_list[4]+'\n\n'+song_list[5]+'\n\n'+song_list[6]+'\n\n'+song_list[7]+'\n\n'+song_list[8]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_1_to_10(self):
        assert_that(self.temp(1, 10), is_(song_list[0]+'\n\n'+song_list[1]+'\n\n'+song_list[2]+'\n\n'+song_list[3]+'\n\n'+song_list[4]+'\n\n'+song_list[5]+'\n\n'+song_list[6]+'\n\n'+song_list[7]+'\n\n'+song_list[8]+'\n\n'+song_list[9]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_1_to_11(self):
        assert_that(self.temp(1, 11), is_(song_list[0]+'\n\n'+song_list[1]+'\n\n'+song_list[2]+'\n\n'+song_list[3]+'\n\n'+song_list[4]+'\n\n'+song_list[5]+'\n\n'+song_list[6]+'\n\n'+song_list[7]+'\n\n'+song_list[8]+'\n\n'+song_list[9]+'\n\n'+song_list[10]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_1_to_12(self):
        assert_that(self.temp(1, 12), is_(song_list[0]+'\n\n'+song_list[1]+'\n\n'+song_list[2]+'\n\n'+song_list[3]+'\n\n'+song_list[4]+'\n\n'+song_list[5]+'\n\n'+song_list[6]+'\n\n'+song_list[7]+'\n\n'+song_list[8]+'\n\n'+song_list[9]+'\n\n'+song_list[10]+'\n\n'+song_list[11]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_2_to_3(self):
        assert_that(self.temp(2, 3), is_(song_list[1]+'\n\n'+song_list[2]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_2_to_4(self):
        assert_that(self.temp(2, 4), is_(song_list[1]+'\n\n'+song_list[2]+'\n\n'+song_list[3]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_2_to_5(self):
        assert_that(self.temp(2, 5), is_(song_list[1]+'\n\n'+song_list[2]+'\n\n'+song_list[3]+'\n\n'+song_list[4]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_2_to_6(self):
        assert_that(self.temp(2, 6), is_(song_list[1]+'\n\n'+song_list[2]+'\n\n'+song_list[3]+'\n\n'+song_list[4]+'\n\n'+song_list[5]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_2_to_7(self):
        assert_that(self.temp(2, 7), is_(song_list[1]+'\n\n'+song_list[2]+'\n\n'+song_list[3]+'\n\n'+song_list[4]+'\n\n'+song_list[5]+'\n\n'+song_list[6]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_2_to_8(self):
        assert_that(self.temp(2, 8), is_(song_list[1]+'\n\n'+song_list[2]+'\n\n'+song_list[3]+'\n\n'+song_list[4]+'\n\n'+song_list[5]+'\n\n'+song_list[6]+'\n\n'+song_list[7]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_2_to_9(self):
        assert_that(self.temp(2, 9), is_(song_list[1]+'\n\n'+song_list[2]+'\n\n'+song_list[3]+'\n\n'+song_list[4]+'\n\n'+song_list[5]+'\n\n'+song_list[6]+'\n\n'+song_list[7]+'\n\n'+song_list[8]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_2_to_10(self):
        assert_that(self.temp(2, 10), is_(song_list[1]+'\n\n'+song_list[2]+'\n\n'+song_list[3]+'\n\n'+song_list[4]+'\n\n'+song_list[5]+'\n\n'+song_list[6]+'\n\n'+song_list[7]+'\n\n'+song_list[8]+'\n\n'+song_list[9]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_2_to_11(self):
        assert_that(self.temp(2, 11), is_(song_list[1]+'\n\n'+song_list[2]+'\n\n'+song_list[3]+'\n\n'+song_list[4]+'\n\n'+song_list[5]+'\n\n'+song_list[6]+'\n\n'+song_list[7]+'\n\n'+song_list[8]+'\n\n'+song_list[9]+'\n\n'+song_list[10]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_2_to_12(self):
        assert_that(self.temp(2, 12), is_(song_list[1]+'\n\n'+song_list[2]+'\n\n'+song_list[3]+'\n\n'+song_list[4]+'\n\n'+song_list[5]+'\n\n'+song_list[6]+'\n\n'+song_list[7]+'\n\n'+song_list[8]+'\n\n'+song_list[9]+'\n\n'+song_list[10]+'\n\n'+song_list[11]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_3_to_4(self):
        assert_that(self.temp(3, 4), is_(song_list[2]+'\n\n'+song_list[3]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_3_to_5(self):
        assert_that(self.temp(3, 5), is_(song_list[2]+'\n\n'+song_list[3]+'\n\n'+song_list[4]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_3_to_6(self):
        assert_that(self.temp(3, 6), is_(song_list[2]+'\n\n'+song_list[3]+'\n\n'+song_list[4]+'\n\n'+song_list[5]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_3_to_7(self):
        assert_that(self.temp(3, 7), is_(song_list[2]+'\n\n'+song_list[3]+'\n\n'+song_list[4]+'\n\n'+song_list[5]+'\n\n'+song_list[6]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_3_to_8(self):
        assert_that(self.temp(3, 8), is_(song_list[2]+'\n\n'+song_list[3]+'\n\n'+song_list[4]+'\n\n'+song_list[5]+'\n\n'+song_list[6]+'\n\n'+song_list[7]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_3_to_9(self):
        assert_that(self.temp(3, 9), is_(song_list[2]+'\n\n'+song_list[3]+'\n\n'+song_list[4]+'\n\n'+song_list[5]+'\n\n'+song_list[6]+'\n\n'+song_list[7]+'\n\n'+song_list[8]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_3_to_10(self):
        assert_that(self.temp(3, 10), is_(song_list[2]+'\n\n'+song_list[3]+'\n\n'+song_list[4]+'\n\n'+song_list[5]+'\n\n'+song_list[6]+'\n\n'+song_list[7]+'\n\n'+song_list[8]+'\n\n'+song_list[9]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_3_to_11(self):
        assert_that(self.temp(3, 11), is_(song_list[2]+'\n\n'+song_list[3]+'\n\n'+song_list[4]+'\n\n'+song_list[5]+'\n\n'+song_list[6]+'\n\n'+song_list[7]+'\n\n'+song_list[8]+'\n\n'+song_list[9]+'\n\n'+song_list[10]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_3_to_12(self):
        assert_that(self.temp(3, 12), is_(song_list[2]+'\n\n'+song_list[3]+'\n\n'+song_list[4]+'\n\n'+song_list[5]+'\n\n'+song_list[6]+'\n\n'+song_list[7]+'\n\n'+song_list[8]+'\n\n'+song_list[9]+'\n\n'+song_list[10]+'\n\n'+song_list[11]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_4_to_5(self):
        assert_that(self.temp(4, 5), is_(song_list[3]+'\n\n'+song_list[4]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_4_to_6(self):
        assert_that(self.temp(4, 6), is_(song_list[3]+'\n\n'+song_list[4]+'\n\n'+song_list[5]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_4_to_7(self):
        assert_that(self.temp(4, 7), is_(song_list[3]+'\n\n'+song_list[4]+'\n\n'+song_list[5]+'\n\n'+song_list[6]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_4_to_8(self):
        assert_that(self.temp(4, 8), is_(song_list[3]+'\n\n'+song_list[4]+'\n\n'+song_list[5]+'\n\n'+song_list[6]+'\n\n'+song_list[7]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_4_to_9(self):
        assert_that(self.temp(4, 9), is_(song_list[3]+'\n\n'+song_list[4]+'\n\n'+song_list[5]+'\n\n'+song_list[6]+'\n\n'+song_list[7]+'\n\n'+song_list[8]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_4_to_10(self):
        assert_that(self.temp(4, 10), is_(song_list[3]+'\n\n'+song_list[4]+'\n\n'+song_list[5]+'\n\n'+song_list[6]+'\n\n'+song_list[7]+'\n\n'+song_list[8]+'\n\n'+song_list[9]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_4_to_11(self):
        assert_that(self.temp(4, 11), is_(song_list[3]+'\n\n'+song_list[4]+'\n\n'+song_list[5]+'\n\n'+song_list[6]+'\n\n'+song_list[7]+'\n\n'+song_list[8]+'\n\n'+song_list[9]+'\n\n'+song_list[10]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_4_to_12(self):
        assert_that(self.temp(4, 12), is_(song_list[3]+'\n\n'+song_list[4]+'\n\n'+song_list[5]+'\n\n'+song_list[6]+'\n\n'+song_list[7]+'\n\n'+song_list[8]+'\n\n'+song_list[9]+'\n\n'+song_list[10]+'\n\n'+song_list[11]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_5_to_6(self):
        assert_that(self.temp(5, 6), is_(song_list[4]+'\n\n'+song_list[5]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_5_to_7(self):
        assert_that(self.temp(5, 7), is_(song_list[4]+'\n\n'+song_list[5]+'\n\n'+song_list[6]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_5_to_8(self):
        assert_that(self.temp(5, 8), is_(song_list[4]+'\n\n'+song_list[5]+'\n\n'+song_list[6]+'\n\n'+song_list[7]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_5_to_9(self):
        assert_that(self.temp(5, 9), is_(song_list[4]+'\n\n'+song_list[5]+'\n\n'+song_list[6]+'\n\n'+song_list[7]+'\n\n'+song_list[8]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_5_to_10(self):
        assert_that(self.temp(5, 10), is_(song_list[4]+'\n\n'+song_list[5]+'\n\n'+song_list[6]+'\n\n'+song_list[7]+'\n\n'+song_list[8]+'\n\n'+song_list[9]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_5_to_11(self):
        assert_that(self.temp(5, 11), is_(song_list[4]+'\n\n'+song_list[5]+'\n\n'+song_list[6]+'\n\n'+song_list[7]+'\n\n'+song_list[8]+'\n\n'+song_list[9]+'\n\n'+song_list[10]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_5_to_12(self):
        assert_that(self.temp(5, 12), is_(song_list[4]+'\n\n'+song_list[5]+'\n\n'+song_list[6]+'\n\n'+song_list[7]+'\n\n'+song_list[8]+'\n\n'+song_list[9]+'\n\n'+song_list[10]+'\n\n'+song_list[11]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_6_to_7(self):
        assert_that(self.temp(6, 7), is_(song_list[5]+'\n\n'+song_list[6]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_6_to_8(self):
        assert_that(self.temp(6, 8), is_(song_list[5]+'\n\n'+song_list[6]+'\n\n'+song_list[7]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_6_to_9(self):
        assert_that(self.temp(6, 9), is_(song_list[5]+'\n\n'+song_list[6]+'\n\n'+song_list[7]+'\n\n'+song_list[8]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_6_to_10(self):
        assert_that(self.temp(6, 10), is_(song_list[5]+'\n\n'+song_list[6]+'\n\n'+song_list[7]+'\n\n'+song_list[8]+'\n\n'+song_list[9]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_6_to_11(self):
        assert_that(self.temp(6, 11), is_(song_list[5]+'\n\n'+song_list[6]+'\n\n'+song_list[7]+'\n\n'+song_list[8]+'\n\n'+song_list[9]+'\n\n'+song_list[10]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_6_to_12(self):
        assert_that(self.temp(6, 12), is_(song_list[5]+'\n\n'+song_list[6]+'\n\n'+song_list[7]+'\n\n'+song_list[8]+'\n\n'+song_list[9]+'\n\n'+song_list[10]+'\n\n'+song_list[11]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_7_to_8(self):
        assert_that(self.temp(7, 8), is_(song_list[6]+'\n\n'+song_list[7]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_7_to_9(self):
        assert_that(self.temp(7, 9), is_(song_list[6]+'\n\n'+song_list[7]+'\n\n'+song_list[8]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_7_to_10(self):
        assert_that(self.temp(7, 10), is_(song_list[6]+'\n\n'+song_list[7]+'\n\n'+song_list[8]+'\n\n'+song_list[9]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_7_to_11(self):
        assert_that(self.temp(7, 11), is_(song_list[6]+'\n\n'+song_list[7]+'\n\n'+song_list[8]+'\n\n'+song_list[9]+'\n\n'+song_list[10]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_7_to_12(self):
        assert_that(self.temp(7, 12), is_(song_list[6]+'\n\n'+song_list[7]+'\n\n'+song_list[8]+'\n\n'+song_list[9]+'\n\n'+song_list[10]+'\n\n'+song_list[11]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_8_to_9(self):
        assert_that(self.temp(8, 9), is_(song_list[7]+'\n\n'+song_list[8]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_8_to_10(self):
        assert_that(self.temp(8, 10), is_(song_list[7]+'\n\n'+song_list[8]+'\n\n'+song_list[9]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_8_to_11(self):
        assert_that(self.temp(8, 11), is_(song_list[7]+'\n\n'+song_list[8]+'\n\n'+song_list[9]+'\n\n'+song_list[10]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_8_to_12(self):
        assert_that(self.temp(8, 12), is_(song_list[7]+'\n\n'+song_list[8]+'\n\n'+song_list[9]+'\n\n'+song_list[10]+'\n\n'+song_list[11]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_9_to_10(self):
        assert_that(self.temp(9, 10), is_(song_list[8]+'\n\n'+song_list[9]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_9_to_11(self):
        assert_that(self.temp(9, 11), is_(song_list[8]+'\n\n'+song_list[9]+'\n\n'+song_list[10]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_9_to_12(self):
        assert_that(self.temp(9, 12), is_(song_list[8]+'\n\n'+song_list[9]+'\n\n'+song_list[10]+'\n\n'+song_list[11]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_10_to_11(self):
        assert_that(self.temp(10, 11), is_(song_list[9]+'\n\n'+song_list[10]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_10_to_12(self):
        assert_that(self.temp(10, 12), is_(song_list[9]+'\n\n'+song_list[10]+'\n\n'+song_list[11]))
    @unittest.skipIf(testing!= "test_verses_from_a_to_b" and testing!="all", "TDD")
    def test_verses_from_11_to_12(self):
        assert_that(self.temp(11, 12), is_(song_list[10]+'\n\n'+song_list[11]))


    # whole song_list test
    @unittest.skipIf(testing!= "test_whole_song" and testing!="all", "TDD")
    def test_whole_song_list(self):
        assert_that(self.temp("all"), is_(song_text))

    # verses from list tests
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_empty_list(self):
        assert_that(self.temp([]), is_(""))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_4(self):
        assert_that(self.temp([4]), is_(song_list[3]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_12_13(self):
        assert_that(self.temp([12, 13]), is_(song_list[11]+'\n\n'+song_list[12]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_10_9_11(self):
        assert_that(self.temp([10, 9, 11]), is_(song_list[9]+'\n\n'+song_list[8]+'\n\n'+song_list[10]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_4_3_3_12(self):
        assert_that(self.temp([4, 3, 3, 12]), is_(song_list[3]+'\n\n'+song_list[2]+'\n\n'+song_list[2]+'\n\n'+song_list[11]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_8_5_7_13_12(self):
        assert_that(self.temp([8, 5, 7, 13, 12]), is_(song_list[7]+'\n\n'+song_list[4]+'\n\n'+song_list[6]+'\n\n'+song_list[12]+'\n\n'+song_list[11]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_3_4_8_11_6_3(self):
        assert_that(self.temp([3, 4, 8, 11, 6, 3]), is_(song_list[2]+'\n\n'+song_list[3]+'\n\n'+song_list[7]+'\n\n'+song_list[10]+'\n\n'+song_list[5]+'\n\n'+song_list[2]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_5_10_11_6_9_12_10(self):
        assert_that(self.temp([5, 10, 11, 6, 9, 12, 10]), is_(song_list[4]+'\n\n'+song_list[9]+'\n\n'+song_list[10]+'\n\n'+song_list[5]+'\n\n'+song_list[8]+'\n\n'+song_list[11]+'\n\n'+song_list[9]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_7_11_2_3_4_12_2_8(self):
        assert_that(self.temp([7, 11, 2, 3, 4, 12, 2, 8]), is_(song_list[6]+'\n\n'+song_list[10]+'\n\n'+song_list[1]+'\n\n'+song_list[2]+'\n\n'+song_list[3]+'\n\n'+song_list[11]+'\n\n'+song_list[1]+'\n\n'+song_list[7]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_1_7_5_13_8_4_3_1_1(self):
        assert_that(self.temp([1, 7, 5, 13, 8, 4, 3, 1, 1]), is_(song_list[0]+'\n\n'+song_list[6]+'\n\n'+song_list[4]+'\n\n'+song_list[12]+'\n\n'+song_list[7]+'\n\n'+song_list[3]+'\n\n'+song_list[2]+'\n\n'+song_list[0]+'\n\n'+song_list[0]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_12_12_9_8_9_2_12_7_11_2(self):
        assert_that(self.temp([12, 12, 9, 8, 9, 2, 12, 7, 11, 2]), is_(song_list[11]+'\n\n'+song_list[11]+'\n\n'+song_list[8]+'\n\n'+song_list[7]+'\n\n'+song_list[8]+'\n\n'+song_list[1]+'\n\n'+song_list[11]+'\n\n'+song_list[6]+'\n\n'+song_list[10]+'\n\n'+song_list[1]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_6_11_7_10_12_5_10_13_4_5_5(self):
        assert_that(self.temp([6, 11, 7, 10, 12, 5, 10, 13, 4, 5, 5]), is_(song_list[5]+'\n\n'+song_list[10]+'\n\n'+song_list[6]+'\n\n'+song_list[9]+'\n\n'+song_list[11]+'\n\n'+song_list[4]+'\n\n'+song_list[9]+'\n\n'+song_list[12]+'\n\n'+song_list[3]+'\n\n'+song_list[4]+'\n\n'+song_list[4]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_10_9_4_7_7_1_9_8_9_13_6_7(self):
        assert_that(self.temp([10, 9, 4, 7, 7, 1, 9, 8, 9, 13, 6, 7]), is_(song_list[9]+'\n\n'+song_list[8]+'\n\n'+song_list[3]+'\n\n'+song_list[6]+'\n\n'+song_list[6]+'\n\n'+song_list[0]+'\n\n'+song_list[8]+'\n\n'+song_list[7]+'\n\n'+song_list[8]+'\n\n'+song_list[12]+'\n\n'+song_list[5]+'\n\n'+song_list[6]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_3(self):
        assert_that(self.temp([3]), is_(song_list[2]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_7_13(self):
        assert_that(self.temp([7, 13]), is_(song_list[6]+'\n\n'+song_list[12]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_5_10_1(self):
        assert_that(self.temp([5, 10, 1]), is_(song_list[4]+'\n\n'+song_list[9]+'\n\n'+song_list[0]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_5_9_4_13(self):
        assert_that(self.temp([5, 9, 4, 13]), is_(song_list[4]+'\n\n'+song_list[8]+'\n\n'+song_list[3]+'\n\n'+song_list[12]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_3_12_8_1_2(self):
        assert_that(self.temp([3, 12, 8, 1, 2]), is_(song_list[2]+'\n\n'+song_list[11]+'\n\n'+song_list[7]+'\n\n'+song_list[0]+'\n\n'+song_list[1]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_13_10_11_13_12_11(self):
        assert_that(self.temp([13, 10, 11, 13, 12, 11]), is_(song_list[12]+'\n\n'+song_list[9]+'\n\n'+song_list[10]+'\n\n'+song_list[12]+'\n\n'+song_list[11]+'\n\n'+song_list[10]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_12_11_3_2_7_5_1(self):
        assert_that(self.temp([12, 11, 3, 2, 7, 5, 1]), is_(song_list[11]+'\n\n'+song_list[10]+'\n\n'+song_list[2]+'\n\n'+song_list[1]+'\n\n'+song_list[6]+'\n\n'+song_list[4]+'\n\n'+song_list[0]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_13_10_4_1_13_6_4_3(self):
        assert_that(self.temp([13, 10, 4, 1, 13, 6, 4, 3]), is_(song_list[12]+'\n\n'+song_list[9]+'\n\n'+song_list[3]+'\n\n'+song_list[0]+'\n\n'+song_list[12]+'\n\n'+song_list[5]+'\n\n'+song_list[3]+'\n\n'+song_list[2]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_7_12_10_13_12_4_12_13_1(self):
        assert_that(self.temp([7, 12, 10, 13, 12, 4, 12, 13, 1]), is_(song_list[6]+'\n\n'+song_list[11]+'\n\n'+song_list[9]+'\n\n'+song_list[12]+'\n\n'+song_list[11]+'\n\n'+song_list[3]+'\n\n'+song_list[11]+'\n\n'+song_list[12]+'\n\n'+song_list[0]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_5_5_13_10_1_12_3_11_6_11(self):
        assert_that(self.temp([5, 5, 13, 10, 1, 12, 3, 11, 6, 11]), is_(song_list[4]+'\n\n'+song_list[4]+'\n\n'+song_list[12]+'\n\n'+song_list[9]+'\n\n'+song_list[0]+'\n\n'+song_list[11]+'\n\n'+song_list[2]+'\n\n'+song_list[10]+'\n\n'+song_list[5]+'\n\n'+song_list[10]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_3_9_2_5_9_8_12_3_8_8_5(self):
        assert_that(self.temp([3, 9, 2, 5, 9, 8, 12, 3, 8, 8, 5]), is_(song_list[2]+'\n\n'+song_list[8]+'\n\n'+song_list[1]+'\n\n'+song_list[4]+'\n\n'+song_list[8]+'\n\n'+song_list[7]+'\n\n'+song_list[11]+'\n\n'+song_list[2]+'\n\n'+song_list[7]+'\n\n'+song_list[7]+'\n\n'+song_list[4]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_10_13_5_8_8_5_10_5_8_12_13_6(self):
        assert_that(self.temp([10, 13, 5, 8, 8, 5, 10, 5, 8, 12, 13, 6]), is_(song_list[9]+'\n\n'+song_list[12]+'\n\n'+song_list[4]+'\n\n'+song_list[7]+'\n\n'+song_list[7]+'\n\n'+song_list[4]+'\n\n'+song_list[9]+'\n\n'+song_list[4]+'\n\n'+song_list[7]+'\n\n'+song_list[11]+'\n\n'+song_list[12]+'\n\n'+song_list[5]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_1(self):
        assert_that(self.temp([1]), is_(song_list[0]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_10_9(self):
        assert_that(self.temp([10, 9]), is_(song_list[9]+'\n\n'+song_list[8]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_9_6_6(self):
        assert_that(self.temp([9, 6, 6]), is_(song_list[8]+'\n\n'+song_list[5]+'\n\n'+song_list[5]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_6_7_7_2(self):
        assert_that(self.temp([6, 7, 7, 2]), is_(song_list[5]+'\n\n'+song_list[6]+'\n\n'+song_list[6]+'\n\n'+song_list[1]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_13_8_13_12_13(self):
        assert_that(self.temp([13, 8, 13, 12, 13]), is_(song_list[12]+'\n\n'+song_list[7]+'\n\n'+song_list[12]+'\n\n'+song_list[11]+'\n\n'+song_list[12]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_2_8_11_4_6_11(self):
        assert_that(self.temp([2, 8, 11, 4, 6, 11]), is_(song_list[1]+'\n\n'+song_list[7]+'\n\n'+song_list[10]+'\n\n'+song_list[3]+'\n\n'+song_list[5]+'\n\n'+song_list[10]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_10_7_8_6_3_12_9(self):
        assert_that(self.temp([10, 7, 8, 6, 3, 12, 9]), is_(song_list[9]+'\n\n'+song_list[6]+'\n\n'+song_list[7]+'\n\n'+song_list[5]+'\n\n'+song_list[2]+'\n\n'+song_list[11]+'\n\n'+song_list[8]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_10_11_6_10_12_7_10_13(self):
        assert_that(self.temp([10, 11, 6, 10, 12, 7, 10, 13]), is_(song_list[9]+'\n\n'+song_list[10]+'\n\n'+song_list[5]+'\n\n'+song_list[9]+'\n\n'+song_list[11]+'\n\n'+song_list[6]+'\n\n'+song_list[9]+'\n\n'+song_list[12]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_5_6_2_13_7_10_10_10_6(self):
        assert_that(self.temp([5, 6, 2, 13, 7, 10, 10, 10, 6]), is_(song_list[4]+'\n\n'+song_list[5]+'\n\n'+song_list[1]+'\n\n'+song_list[12]+'\n\n'+song_list[6]+'\n\n'+song_list[9]+'\n\n'+song_list[9]+'\n\n'+song_list[9]+'\n\n'+song_list[5]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_5_11_12_10_11_11_8_4_3_12(self):
        assert_that(self.temp([5, 11, 12, 10, 11, 11, 8, 4, 3, 12]), is_(song_list[4]+'\n\n'+song_list[10]+'\n\n'+song_list[11]+'\n\n'+song_list[9]+'\n\n'+song_list[10]+'\n\n'+song_list[10]+'\n\n'+song_list[7]+'\n\n'+song_list[3]+'\n\n'+song_list[2]+'\n\n'+song_list[11]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_2_8_3_13_13_12_9_1_4_3_5(self):
        assert_that(self.temp([2, 8, 3, 13, 13, 12, 9, 1, 4, 3, 5]), is_(song_list[1]+'\n\n'+song_list[7]+'\n\n'+song_list[2]+'\n\n'+song_list[12]+'\n\n'+song_list[12]+'\n\n'+song_list[11]+'\n\n'+song_list[8]+'\n\n'+song_list[0]+'\n\n'+song_list[3]+'\n\n'+song_list[2]+'\n\n'+song_list[4]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_2_9_3_8_8_4_6_8_4_1_5_4(self):
        assert_that(self.temp([2, 9, 3, 8, 8, 4, 6, 8, 4, 1, 5, 4]), is_(song_list[1]+'\n\n'+song_list[8]+'\n\n'+song_list[2]+'\n\n'+song_list[7]+'\n\n'+song_list[7]+'\n\n'+song_list[3]+'\n\n'+song_list[5]+'\n\n'+song_list[7]+'\n\n'+song_list[3]+'\n\n'+song_list[0]+'\n\n'+song_list[4]+'\n\n'+song_list[3]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_1(self):
        assert_that(self.temp([1]), is_(song_list[0]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_12_7(self):
        assert_that(self.temp([12, 7]), is_(song_list[11]+'\n\n'+song_list[6]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_6_12_11(self):
        assert_that(self.temp([6, 12, 11]), is_(song_list[5]+'\n\n'+song_list[11]+'\n\n'+song_list[10]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_12_7_8_3(self):
        assert_that(self.temp([12, 7, 8, 3]), is_(song_list[11]+'\n\n'+song_list[6]+'\n\n'+song_list[7]+'\n\n'+song_list[2]))



unittest.main()
