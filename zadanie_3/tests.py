import unittest
from hamcrest import *
from function import dawaj_give, song_text, song_list

class DawajGiveTest(unittest.TestCase):

    testing = "all"

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
    def test_verses_2_2(self):
        assert_that(self.temp([2, 2]), is_(song_list[1]+'\n\n'+song_list[1]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_10_9_7(self):
        assert_that(self.temp([10, 9, 7]), is_(song_list[9]+'\n\n'+song_list[8]+'\n\n'+song_list[6]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_1_3_11_10(self):
        assert_that(self.temp([1, 3, 11, 10]), is_(song_list[0]+'\n\n'+song_list[2]+'\n\n'+song_list[10]+'\n\n'+song_list[9]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_7_5_2_8_11(self):
        assert_that(self.temp([7, 5, 2, 8, 11]), is_(song_list[6]+'\n\n'+song_list[4]+'\n\n'+song_list[1]+'\n\n'+song_list[7]+'\n\n'+song_list[10]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_2_9_1_2_12_2(self):
        assert_that(self.temp([2, 9, 1, 2, 12, 2]), is_(song_list[1]+'\n\n'+song_list[8]+'\n\n'+song_list[0]+'\n\n'+song_list[1]+'\n\n'+song_list[11]+'\n\n'+song_list[1]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_7_4_4_5_3_10_6(self):
        assert_that(self.temp([7, 4, 4, 5, 3, 10, 6]), is_(song_list[6]+'\n\n'+song_list[3]+'\n\n'+song_list[3]+'\n\n'+song_list[4]+'\n\n'+song_list[2]+'\n\n'+song_list[9]+'\n\n'+song_list[5]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_7_3_6_9_2_3_7_9(self):
        assert_that(self.temp([7, 3, 6, 9, 2, 3, 7, 9]), is_(song_list[6]+'\n\n'+song_list[2]+'\n\n'+song_list[5]+'\n\n'+song_list[8]+'\n\n'+song_list[1]+'\n\n'+song_list[2]+'\n\n'+song_list[6]+'\n\n'+song_list[8]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_8_10_8_10_9_11_7_5_4(self):
        assert_that(self.temp([8, 10, 8, 10, 9, 11, 7, 5, 4]), is_(song_list[7]+'\n\n'+song_list[9]+'\n\n'+song_list[7]+'\n\n'+song_list[9]+'\n\n'+song_list[8]+'\n\n'+song_list[10]+'\n\n'+song_list[6]+'\n\n'+song_list[4]+'\n\n'+song_list[3]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_2_10_11_3_7_9_12_6_4_7(self):
        assert_that(self.temp([2, 10, 11, 3, 7, 9, 12, 6, 4, 7]), is_(song_list[1]+'\n\n'+song_list[9]+'\n\n'+song_list[10]+'\n\n'+song_list[2]+'\n\n'+song_list[6]+'\n\n'+song_list[8]+'\n\n'+song_list[11]+'\n\n'+song_list[5]+'\n\n'+song_list[3]+'\n\n'+song_list[6]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_10_10_11_3_6_6_1_6_9_10_12(self):
        assert_that(self.temp([10, 10, 11, 3, 6, 6, 1, 6, 9, 10, 12]), is_(song_list[9]+'\n\n'+song_list[9]+'\n\n'+song_list[10]+'\n\n'+song_list[2]+'\n\n'+song_list[5]+'\n\n'+song_list[5]+'\n\n'+song_list[0]+'\n\n'+song_list[5]+'\n\n'+song_list[8]+'\n\n'+song_list[9]+'\n\n'+song_list[11]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_11_3_6_9_11_11_12_4_12_3_5_8(self):
        assert_that(self.temp([11, 3, 6, 9, 11, 11, 12, 4, 12, 3, 5, 8]), is_(song_list[10]+'\n\n'+song_list[2]+'\n\n'+song_list[5]+'\n\n'+song_list[8]+'\n\n'+song_list[10]+'\n\n'+song_list[10]+'\n\n'+song_list[11]+'\n\n'+song_list[3]+'\n\n'+song_list[11]+'\n\n'+song_list[2]+'\n\n'+song_list[4]+'\n\n'+song_list[7]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_6(self):
        assert_that(self.temp([6]), is_(song_list[5]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_9_4(self):
        assert_that(self.temp([9, 4]), is_(song_list[8]+'\n\n'+song_list[3]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_8_5_4(self):
        assert_that(self.temp([8, 5, 4]), is_(song_list[7]+'\n\n'+song_list[4]+'\n\n'+song_list[3]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_1_6_2_1(self):
        assert_that(self.temp([1, 6, 2, 1]), is_(song_list[0]+'\n\n'+song_list[5]+'\n\n'+song_list[1]+'\n\n'+song_list[0]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_6_6_8_11_5(self):
        assert_that(self.temp([6, 6, 8, 11, 5]), is_(song_list[5]+'\n\n'+song_list[5]+'\n\n'+song_list[7]+'\n\n'+song_list[10]+'\n\n'+song_list[4]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_11_4_6_5_4_11(self):
        assert_that(self.temp([11, 4, 6, 5, 4, 11]), is_(song_list[10]+'\n\n'+song_list[3]+'\n\n'+song_list[5]+'\n\n'+song_list[4]+'\n\n'+song_list[3]+'\n\n'+song_list[10]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_10_12_4_9_7_2_8(self):
        assert_that(self.temp([10, 12, 4, 9, 7, 2, 8]), is_(song_list[9]+'\n\n'+song_list[11]+'\n\n'+song_list[3]+'\n\n'+song_list[8]+'\n\n'+song_list[6]+'\n\n'+song_list[1]+'\n\n'+song_list[7]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_4_1_6_6_7_12_3_1(self):
        assert_that(self.temp([4, 1, 6, 6, 7, 12, 3, 1]), is_(song_list[3]+'\n\n'+song_list[0]+'\n\n'+song_list[5]+'\n\n'+song_list[5]+'\n\n'+song_list[6]+'\n\n'+song_list[11]+'\n\n'+song_list[2]+'\n\n'+song_list[0]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_4_11_7_12_5_8_7_8_8(self):
        assert_that(self.temp([4, 11, 7, 12, 5, 8, 7, 8, 8]), is_(song_list[3]+'\n\n'+song_list[10]+'\n\n'+song_list[6]+'\n\n'+song_list[11]+'\n\n'+song_list[4]+'\n\n'+song_list[7]+'\n\n'+song_list[6]+'\n\n'+song_list[7]+'\n\n'+song_list[7]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_9_3_6_10_9_3_11_4_4_11(self):
        assert_that(self.temp([9, 3, 6, 10, 9, 3, 11, 4, 4, 11]), is_(song_list[8]+'\n\n'+song_list[2]+'\n\n'+song_list[5]+'\n\n'+song_list[9]+'\n\n'+song_list[8]+'\n\n'+song_list[2]+'\n\n'+song_list[10]+'\n\n'+song_list[3]+'\n\n'+song_list[3]+'\n\n'+song_list[10]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_9_10_1_4_3_4_2_2_3_12_1(self):
        assert_that(self.temp([9, 10, 1, 4, 3, 4, 2, 2, 3, 12, 1]), is_(song_list[8]+'\n\n'+song_list[9]+'\n\n'+song_list[0]+'\n\n'+song_list[3]+'\n\n'+song_list[2]+'\n\n'+song_list[3]+'\n\n'+song_list[1]+'\n\n'+song_list[1]+'\n\n'+song_list[2]+'\n\n'+song_list[11]+'\n\n'+song_list[0]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_4_12_6_8_1_7_7_3_11_6_5_7(self):
        assert_that(self.temp([4, 12, 6, 8, 1, 7, 7, 3, 11, 6, 5, 7]), is_(song_list[3]+'\n\n'+song_list[11]+'\n\n'+song_list[5]+'\n\n'+song_list[7]+'\n\n'+song_list[0]+'\n\n'+song_list[6]+'\n\n'+song_list[6]+'\n\n'+song_list[2]+'\n\n'+song_list[10]+'\n\n'+song_list[5]+'\n\n'+song_list[4]+'\n\n'+song_list[6]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_8(self):
        assert_that(self.temp([8]), is_(song_list[7]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_11_11(self):
        assert_that(self.temp([11, 11]), is_(song_list[10]+'\n\n'+song_list[10]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_5_11_7(self):
        assert_that(self.temp([5, 11, 7]), is_(song_list[4]+'\n\n'+song_list[10]+'\n\n'+song_list[6]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_12_7_8_1(self):
        assert_that(self.temp([12, 7, 8, 1]), is_(song_list[11]+'\n\n'+song_list[6]+'\n\n'+song_list[7]+'\n\n'+song_list[0]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_10_2_1_9_6(self):
        assert_that(self.temp([10, 2, 1, 9, 6]), is_(song_list[9]+'\n\n'+song_list[1]+'\n\n'+song_list[0]+'\n\n'+song_list[8]+'\n\n'+song_list[5]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_9_5_10_7_11_5(self):
        assert_that(self.temp([9, 5, 10, 7, 11, 5]), is_(song_list[8]+'\n\n'+song_list[4]+'\n\n'+song_list[9]+'\n\n'+song_list[6]+'\n\n'+song_list[10]+'\n\n'+song_list[4]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_1_9_6_12_7_10_1(self):
        assert_that(self.temp([1, 9, 6, 12, 7, 10, 1]), is_(song_list[0]+'\n\n'+song_list[8]+'\n\n'+song_list[5]+'\n\n'+song_list[11]+'\n\n'+song_list[6]+'\n\n'+song_list[9]+'\n\n'+song_list[0]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_8_5_6_5_7_10_7_5(self):
        assert_that(self.temp([8, 5, 6, 5, 7, 10, 7, 5]), is_(song_list[7]+'\n\n'+song_list[4]+'\n\n'+song_list[5]+'\n\n'+song_list[4]+'\n\n'+song_list[6]+'\n\n'+song_list[9]+'\n\n'+song_list[6]+'\n\n'+song_list[4]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_9_8_6_5_8_7_5_8_9(self):
        assert_that(self.temp([9, 8, 6, 5, 8, 7, 5, 8, 9]), is_(song_list[8]+'\n\n'+song_list[7]+'\n\n'+song_list[5]+'\n\n'+song_list[4]+'\n\n'+song_list[7]+'\n\n'+song_list[6]+'\n\n'+song_list[4]+'\n\n'+song_list[7]+'\n\n'+song_list[8]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_8_6_2_1_4_9_4_11_10_6(self):
        assert_that(self.temp([8, 6, 2, 1, 4, 9, 4, 11, 10, 6]), is_(song_list[7]+'\n\n'+song_list[5]+'\n\n'+song_list[1]+'\n\n'+song_list[0]+'\n\n'+song_list[3]+'\n\n'+song_list[8]+'\n\n'+song_list[3]+'\n\n'+song_list[10]+'\n\n'+song_list[9]+'\n\n'+song_list[5]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_5_5_12_3_3_11_6_5_3_3_5(self):
        assert_that(self.temp([5, 5, 12, 3, 3, 11, 6, 5, 3, 3, 5]), is_(song_list[4]+'\n\n'+song_list[4]+'\n\n'+song_list[11]+'\n\n'+song_list[2]+'\n\n'+song_list[2]+'\n\n'+song_list[10]+'\n\n'+song_list[5]+'\n\n'+song_list[4]+'\n\n'+song_list[2]+'\n\n'+song_list[2]+'\n\n'+song_list[4]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_2_11_12_2_12_1_2_7_1_3_8_7(self):
        assert_that(self.temp([2, 11, 12, 2, 12, 1, 2, 7, 1, 3, 8, 7]), is_(song_list[1]+'\n\n'+song_list[10]+'\n\n'+song_list[11]+'\n\n'+song_list[1]+'\n\n'+song_list[11]+'\n\n'+song_list[0]+'\n\n'+song_list[1]+'\n\n'+song_list[6]+'\n\n'+song_list[0]+'\n\n'+song_list[2]+'\n\n'+song_list[7]+'\n\n'+song_list[6]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_11(self):
        assert_that(self.temp([11]), is_(song_list[10]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_12_4(self):
        assert_that(self.temp([12, 4]), is_(song_list[11]+'\n\n'+song_list[3]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_1_11_5(self):
        assert_that(self.temp([1, 11, 5]), is_(song_list[0]+'\n\n'+song_list[10]+'\n\n'+song_list[4]))
    @unittest.skipIf(testing!= "test_verses_from_list" and testing!="all", "TDD")
    def test_verses_12_9_4_2(self):
        assert_that(self.temp([12, 9, 4, 2]), is_(song_list[11]+'\n\n'+song_list[8]+'\n\n'+song_list[3]+'\n\n'+song_list[1]))



unittest.main()
