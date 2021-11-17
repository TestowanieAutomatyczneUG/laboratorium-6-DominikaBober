import unittest
from hamcrest import *
from function import dawaj_give, song
song_text = open("laboratorium-6-DominikaBober/zadanie_3/song.txt","r+").read()

class DawajGiveTest(unittest.TestCase):

    def setUp(self):
        self.temp = dawaj_give

    def test_one_verse_1(self):
        assert_that(self.temp(1), is_(song[1]))
    
    # one verse tests
    def test_one_verse_1(self):
        assert_that(self.temp(1), is_(song[1]))
    def test_one_verse_2(self):
        assert_that(self.temp(2), is_(song[2]))
    def test_one_verse_3(self):
        assert_that(self.temp(3), is_(song[3]))
    def test_one_verse_4(self):
        assert_that(self.temp(4), is_(song[4]))
    def test_one_verse_5(self):
        assert_that(self.temp(5), is_(song[5]))
    def test_one_verse_6(self):
        assert_that(self.temp(6), is_(song[6]))
    def test_one_verse_7(self):
        assert_that(self.temp(7), is_(song[7]))
    def test_one_verse_8(self):
        assert_that(self.temp(8), is_(song[8]))
    def test_one_verse_9(self):
        assert_that(self.temp(9), is_(song[9]))
    def test_one_verse_10(self):
        assert_that(self.temp(10), is_(song[10]))
    def test_one_verse_11(self):
        assert_that(self.temp(11), is_(song[11]))
    def test_one_verse_12(self):
        assert_that(self.temp(12), is_(song[12]))
    
    # verses from a to b tests
    def test_verses_from_1_to_2(self):
        assert_that(self.temp(0, 1), is_(song[0]+'\n\n'+song[1]))
    def test_verses_from_1_to_3(self):
        assert_that(self.temp(0, 2), is_(song[0]+'\n\n'+song[1]+'\n\n'+song[2]))
    def test_verses_from_1_to_4(self):
        assert_that(self.temp(0, 3), is_(song[0]+'\n\n'+song[1]+'\n\n'+song[2]+'\n\n'+song[3]))
    def test_verses_from_1_to_5(self):
        assert_that(self.temp(0, 4), is_(song[0]+'\n\n'+song[1]+'\n\n'+song[2]+'\n\n'+song[3]+'\n\n'+song[4]))
    def test_verses_from_1_to_6(self):
        assert_that(self.temp(0, 5), is_(song[0]+'\n\n'+song[1]+'\n\n'+song[2]+'\n\n'+song[3]+'\n\n'+song[4]+'\n\n'+song[5]))
    def test_verses_from_1_to_7(self):
        assert_that(self.temp(0, 6), is_(song[0]+'\n\n'+song[1]+'\n\n'+song[2]+'\n\n'+song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]))
    def test_verses_from_1_to_8(self):
        assert_that(self.temp(0, 7), is_(song[0]+'\n\n'+song[1]+'\n\n'+song[2]+'\n\n'+song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]))
    def test_verses_from_1_to_9(self):
        assert_that(self.temp(0, 8), is_(song[0]+'\n\n'+song[1]+'\n\n'+song[2]+'\n\n'+song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]))
    def test_verses_from_1_to_10(self):
        assert_that(self.temp(0, 9), is_(song[0]+'\n\n'+song[1]+'\n\n'+song[2]+'\n\n'+song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]))
    def test_verses_from_1_to_11(self):
        assert_that(self.temp(0, 10), is_(song[0]+'\n\n'+song[1]+'\n\n'+song[2]+'\n\n'+song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]+'\n\n'+song[10]))
    def test_verses_from_1_to_12(self):
        assert_that(self.temp(0, 11), is_(song[0]+'\n\n'+song[1]+'\n\n'+song[2]+'\n\n'+song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]+'\n\n'+song[10]+'\n\n'+song[11]))
    def test_verses_from_2_to_3(self):
        assert_that(self.temp(1, 2), is_(song[1]+'\n\n'+song[2]))
    def test_verses_from_2_to_4(self):
        assert_that(self.temp(1, 3), is_(song[1]+'\n\n'+song[2]+'\n\n'+song[3]))
    def test_verses_from_2_to_5(self):
        assert_that(self.temp(1, 4), is_(song[1]+'\n\n'+song[2]+'\n\n'+song[3]+'\n\n'+song[4]))
    def test_verses_from_2_to_6(self):
        assert_that(self.temp(1, 5), is_(song[1]+'\n\n'+song[2]+'\n\n'+song[3]+'\n\n'+song[4]+'\n\n'+song[5]))
    def test_verses_from_2_to_7(self):
        assert_that(self.temp(1, 6), is_(song[1]+'\n\n'+song[2]+'\n\n'+song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]))
    def test_verses_from_2_to_8(self):
        assert_that(self.temp(1, 7), is_(song[1]+'\n\n'+song[2]+'\n\n'+song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]))
    def test_verses_from_2_to_9(self):
        assert_that(self.temp(1, 8), is_(song[1]+'\n\n'+song[2]+'\n\n'+song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]))
    def test_verses_from_2_to_10(self):
        assert_that(self.temp(1, 9), is_(song[1]+'\n\n'+song[2]+'\n\n'+song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]))
    def test_verses_from_2_to_11(self):
        assert_that(self.temp(1, 10), is_(song[1]+'\n\n'+song[2]+'\n\n'+song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]+'\n\n'+song[10]))
    def test_verses_from_2_to_12(self):
        assert_that(self.temp(1, 11), is_(song[1]+'\n\n'+song[2]+'\n\n'+song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]+'\n\n'+song[10]+'\n\n'+song[11]))
    def test_verses_from_3_to_4(self):
        assert_that(self.temp(2, 3), is_(song[2]+'\n\n'+song[3]))
    def test_verses_from_3_to_5(self):
        assert_that(self.temp(2, 4), is_(song[2]+'\n\n'+song[3]+'\n\n'+song[4]))
    def test_verses_from_3_to_6(self):
        assert_that(self.temp(2, 5), is_(song[2]+'\n\n'+song[3]+'\n\n'+song[4]+'\n\n'+song[5]))
    def test_verses_from_3_to_7(self):
        assert_that(self.temp(2, 6), is_(song[2]+'\n\n'+song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]))
    def test_verses_from_3_to_8(self):
        assert_that(self.temp(2, 7), is_(song[2]+'\n\n'+song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]))
    def test_verses_from_3_to_9(self):
        assert_that(self.temp(2, 8), is_(song[2]+'\n\n'+song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]))
    def test_verses_from_3_to_10(self):
        assert_that(self.temp(2, 9), is_(song[2]+'\n\n'+song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]))
    def test_verses_from_3_to_11(self):
        assert_that(self.temp(2, 10), is_(song[2]+'\n\n'+song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]+'\n\n'+song[10]))
    def test_verses_from_3_to_12(self):
        assert_that(self.temp(2, 11), is_(song[2]+'\n\n'+song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]+'\n\n'+song[10]+'\n\n'+song[11]))
    def test_verses_from_4_to_5(self):
        assert_that(self.temp(3, 4), is_(song[3]+'\n\n'+song[4]))
    def test_verses_from_4_to_6(self):
        assert_that(self.temp(3, 5), is_(song[3]+'\n\n'+song[4]+'\n\n'+song[5]))
    def test_verses_from_4_to_7(self):
        assert_that(self.temp(3, 6), is_(song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]))
    def test_verses_from_4_to_8(self):
        assert_that(self.temp(3, 7), is_(song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]))
    def test_verses_from_4_to_9(self):
        assert_that(self.temp(3, 8), is_(song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]))
    def test_verses_from_4_to_10(self):
        assert_that(self.temp(3, 9), is_(song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]))
    def test_verses_from_4_to_11(self):
        assert_that(self.temp(3, 10), is_(song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]+'\n\n'+song[10]))
    def test_verses_from_4_to_12(self):
        assert_that(self.temp(3, 11), is_(song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]+'\n\n'+song[10]+'\n\n'+song[11]))
    def test_verses_from_5_to_6(self):
        assert_that(self.temp(4, 5), is_(song[4]+'\n\n'+song[5]))
    def test_verses_from_5_to_7(self):
        assert_that(self.temp(4, 6), is_(song[4]+'\n\n'+song[5]+'\n\n'+song[6]))
    def test_verses_from_5_to_8(self):
        assert_that(self.temp(4, 7), is_(song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]))
    def test_verses_from_5_to_9(self):
        assert_that(self.temp(4, 8), is_(song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]))
    def test_verses_from_5_to_10(self):
        assert_that(self.temp(4, 9), is_(song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]))
    def test_verses_from_5_to_11(self):
        assert_that(self.temp(4, 10), is_(song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]+'\n\n'+song[10]))
    def test_verses_from_5_to_12(self):
        assert_that(self.temp(4, 11), is_(song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]+'\n\n'+song[10]+'\n\n'+song[11]))
    def test_verses_from_6_to_7(self):
        assert_that(self.temp(5, 6), is_(song[5]+'\n\n'+song[6]))
    def test_verses_from_6_to_8(self):
        assert_that(self.temp(5, 7), is_(song[5]+'\n\n'+song[6]+'\n\n'+song[7]))
    def test_verses_from_6_to_9(self):
        assert_that(self.temp(5, 8), is_(song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]))
    def test_verses_from_6_to_10(self):
        assert_that(self.temp(5, 9), is_(song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]))
    def test_verses_from_6_to_11(self):
        assert_that(self.temp(5, 10), is_(song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]+'\n\n'+song[10]))
    def test_verses_from_6_to_12(self):
        assert_that(self.temp(5, 11), is_(song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]+'\n\n'+song[10]+'\n\n'+song[11]))
    def test_verses_from_7_to_8(self):
        assert_that(self.temp(6, 7), is_(song[6]+'\n\n'+song[7]))
    def test_verses_from_7_to_9(self):
        assert_that(self.temp(6, 8), is_(song[6]+'\n\n'+song[7]+'\n\n'+song[8]))
    def test_verses_from_7_to_10(self):
        assert_that(self.temp(6, 9), is_(song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]))
    def test_verses_from_7_to_11(self):
        assert_that(self.temp(6, 10), is_(song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]+'\n\n'+song[10]))
    def test_verses_from_7_to_12(self):
        assert_that(self.temp(6, 11), is_(song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]+'\n\n'+song[10]+'\n\n'+song[11]))
    def test_verses_from_8_to_9(self):
        assert_that(self.temp(7, 8), is_(song[7]+'\n\n'+song[8]))
    def test_verses_from_8_to_10(self):
        assert_that(self.temp(7, 9), is_(song[7]+'\n\n'+song[8]+'\n\n'+song[9]))
    def test_verses_from_8_to_11(self):
        assert_that(self.temp(7, 10), is_(song[7]+'\n\n'+song[8]+'\n\n'+song[9]+'\n\n'+song[10]))
    def test_verses_from_8_to_12(self):
        assert_that(self.temp(7, 11), is_(song[7]+'\n\n'+song[8]+'\n\n'+song[9]+'\n\n'+song[10]+'\n\n'+song[11]))
    def test_verses_from_9_to_10(self):
        assert_that(self.temp(8, 9), is_(song[8]+'\n\n'+song[9]))
    def test_verses_from_9_to_11(self):
        assert_that(self.temp(8, 10), is_(song[8]+'\n\n'+song[9]+'\n\n'+song[10]))
    def test_verses_from_9_to_12(self):
        assert_that(self.temp(8, 11), is_(song[8]+'\n\n'+song[9]+'\n\n'+song[10]+'\n\n'+song[11]))
    def test_verses_from_10_to_11(self):
        assert_that(self.temp(9, 10), is_(song[9]+'\n\n'+song[10]))
    def test_verses_from_10_to_12(self):
        assert_that(self.temp(9, 11), is_(song[9]+'\n\n'+song[10]+'\n\n'+song[11]))
    def test_verses_from_11_to_12(self):
        assert_that(self.temp(10, 11), is_(song[10]+'\n\n'+song[11]))

    # whole song test
    def test_whole_song(self):
        assert_that(self.temp("all"), is_(song_text))

    # verses from list tests
    def test_verses_8(self):
        assert_that(self.temp([8]), is_(song[8]))
    def test_verses_7_2(self):
        assert_that(self.temp([7, 1]), is_(song[7]+'\n\n'+song[1]))
    def test_verses_5_4_6(self):
        assert_that(self.temp([5, 3, 5]), is_(song[5]+'\n\n'+song[3]+'\n\n'+song[5]))
    def test_verses_6_5_8_11(self):
        assert_that(self.temp([6, 4, 7, 10]), is_(song[6]+'\n\n'+song[4]+'\n\n'+song[7]+'\n\n'+song[10]))
    def test_verses_2_5_1_2_2(self):
        assert_that(self.temp([2, 4, 0, 1, 1]), is_(song[2]+'\n\n'+song[4]+'\n\n'+song[0]+'\n\n'+song[1]+'\n\n'+song[1]))
    def test_verses_9_3_2_7_5_8(self):
        assert_that(self.temp([9, 2, 1, 6, 4, 7]), is_(song[9]+'\n\n'+song[2]+'\n\n'+song[1]+'\n\n'+song[6]+'\n\n'+song[4]+'\n\n'+song[7]))
    def test_verses_11_9_4_12_13_5_3(self):
        assert_that(self.temp([11, 8, 3, 11, 12, 4, 2]), is_(song[11]+'\n\n'+song[8]+'\n\n'+song[3]+'\n\n'+song[11]+'\n\n'+song[12]+'\n\n'+song[4]+'\n\n'+song[2]))
    def test_verses_1_12_8_12_1_12_12_3(self):
        assert_that(self.temp([1, 11, 7, 11, 0, 11, 11, 2]), is_(song[1]+'\n\n'+song[11]+'\n\n'+song[7]+'\n\n'+song[11]+'\n\n'+song[0]+'\n\n'+song[11]+'\n\n'+song[11]+'\n\n'+song[2]))
    def test_verses_0_8_4_12_11_8_11_11_10(self):
        assert_that(self.temp([0, 7, 3, 11, 10, 7, 10, 10, 9]), is_(song[0]+'\n\n'+song[7]+'\n\n'+song[3]+'\n\n'+song[11]+'\n\n'+song[10]+'\n\n'+song[7]+'\n\n'+song[10]+'\n\n'+song[10]+'\n\n'+song[9]))
    def test_verses_11_5_4_12_1_2_7_8_8_5(self):
        assert_that(self.temp([11, 4, 3, 11, 0, 1, 6, 7, 7, 4]), is_(song[11]+'\n\n'+song[4]+'\n\n'+song[3]+'\n\n'+song[11]+'\n\n'+song[0]+'\n\n'+song[1]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[7]+'\n\n'+song[4]))
    def test_verses_9_2_9_2_5_2_5_3_4_10_11(self):
        assert_that(self.temp([9, 1, 8, 1, 4, 1, 4, 2, 3, 9, 10]), is_(song[9]+'\n\n'+song[1]+'\n\n'+song[8]+'\n\n'+song[1]+'\n\n'+song[4]+'\n\n'+song[1]+'\n\n'+song[4]+'\n\n'+song[2]+'\n\n'+song[3]+'\n\n'+song[9]+'\n\n'+song[10]))
    def test_verses_11_6_5_6_10_6_1_7_7_1_12_4(self):
        assert_that(self.temp([11, 5, 4, 5, 9, 5, 0, 6, 6, 0, 11, 3]), is_(song[11]+'\n\n'+song[5]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[9]+'\n\n'+song[5]+'\n\n'+song[0]+'\n\n'+song[6]+'\n\n'+song[6]+'\n\n'+song[0]+'\n\n'+song[11]+'\n\n'+song[3]))
    def test_verses_5(self):
        assert_that(self.temp([5]), is_(song[5]))
    def test_verses_0_1(self):
        assert_that(self.temp([0, 0]), is_(song[0]+'\n\n'+song[0]))
    def test_verses_9_1_11(self):
        assert_that(self.temp([9, 0, 10]), is_(song[9]+'\n\n'+song[0]+'\n\n'+song[10]))
    def test_verses_1_6_2_12(self):
        assert_that(self.temp([1, 5, 1, 11]), is_(song[1]+'\n\n'+song[5]+'\n\n'+song[1]+'\n\n'+song[11]))
    def test_verses_6_9_7_10_10(self):
        assert_that(self.temp([6, 8, 6, 9, 9]), is_(song[6]+'\n\n'+song[8]+'\n\n'+song[6]+'\n\n'+song[9]+'\n\n'+song[9]))
    def test_verses_2_13_8_9_12_3(self):
        assert_that(self.temp([2, 12, 7, 8, 11, 2]), is_(song[2]+'\n\n'+song[12]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[11]+'\n\n'+song[2]))
    def test_verses_9_9_3_11_11_13_1(self):
        assert_that(self.temp([9, 8, 2, 10, 10, 12, 0]), is_(song[9]+'\n\n'+song[8]+'\n\n'+song[2]+'\n\n'+song[10]+'\n\n'+song[10]+'\n\n'+song[12]+'\n\n'+song[0]))
    def test_verses_0_3_8_10_11_8_12_8(self):
        assert_that(self.temp([0, 2, 7, 9, 10, 7, 11, 7]), is_(song[0]+'\n\n'+song[2]+'\n\n'+song[7]+'\n\n'+song[9]+'\n\n'+song[10]+'\n\n'+song[7]+'\n\n'+song[11]+'\n\n'+song[7]))
    def test_verses_2_5_6_9_6_11_2_3_11(self):
        assert_that(self.temp([2, 4, 5, 8, 5, 10, 1, 2, 10]), is_(song[2]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[8]+'\n\n'+song[5]+'\n\n'+song[10]+'\n\n'+song[1]+'\n\n'+song[2]+'\n\n'+song[10]))
    def test_verses_12_11_2_2_5_11_10_8_5_1(self):
        assert_that(self.temp([12, 10, 1, 1, 4, 10, 9, 7, 4, 0]), is_(song[12]+'\n\n'+song[10]+'\n\n'+song[1]+'\n\n'+song[1]+'\n\n'+song[4]+'\n\n'+song[10]+'\n\n'+song[9]+'\n\n'+song[7]+'\n\n'+song[4]+'\n\n'+song[0]))
    def test_verses_10_4_8_12_10_3_5_11_12_6_10(self):
        assert_that(self.temp([10, 3, 7, 11, 9, 2, 4, 10, 11, 5, 9]), is_(song[10]+'\n\n'+song[3]+'\n\n'+song[7]+'\n\n'+song[11]+'\n\n'+song[9]+'\n\n'+song[2]+'\n\n'+song[4]+'\n\n'+song[10]+'\n\n'+song[11]+'\n\n'+song[5]+'\n\n'+song[9]))
    def test_verses_8_5_9_3_7_6_4_10_5_1_1_9(self):
        assert_that(self.temp([8, 4, 8, 2, 6, 5, 3, 9, 4, 0, 0, 8]), is_(song[8]+'\n\n'+song[4]+'\n\n'+song[8]+'\n\n'+song[2]+'\n\n'+song[6]+'\n\n'+song[5]+'\n\n'+song[3]+'\n\n'+song[9]+'\n\n'+song[4]+'\n\n'+song[0]+'\n\n'+song[0]+'\n\n'+song[8]))
    def test_verses_6(self):
        assert_that(self.temp([6]), is_(song[6]))
    def test_verses_6_7(self):
        assert_that(self.temp([6, 6]), is_(song[6]+'\n\n'+song[6]))
    def test_verses_0_4_8(self):
        assert_that(self.temp([0, 3, 7]), is_(song[0]+'\n\n'+song[3]+'\n\n'+song[7]))
    def test_verses_12_8_6_9(self):
        assert_that(self.temp([12, 7, 5, 8]), is_(song[12]+'\n\n'+song[7]+'\n\n'+song[5]+'\n\n'+song[8]))
    def test_verses_5_10_4_6_1(self):
        assert_that(self.temp([5, 9, 3, 5, 0]), is_(song[5]+'\n\n'+song[9]+'\n\n'+song[3]+'\n\n'+song[5]+'\n\n'+song[0]))
    def test_verses_7_3_6_10_5_3(self):
        assert_that(self.temp([7, 2, 5, 9, 4, 2]), is_(song[7]+'\n\n'+song[2]+'\n\n'+song[5]+'\n\n'+song[9]+'\n\n'+song[4]+'\n\n'+song[2]))
    def test_verses_12_13_10_11_9_4_13(self):
        assert_that(self.temp([12, 12, 9, 10, 8, 3, 12]), is_(song[12]+'\n\n'+song[12]+'\n\n'+song[9]+'\n\n'+song[10]+'\n\n'+song[8]+'\n\n'+song[3]+'\n\n'+song[12]))
    def test_verses_3_2_2_12_3_8_6_8(self):
        assert_that(self.temp([3, 1, 1, 11, 2, 7, 5, 7]), is_(song[3]+'\n\n'+song[1]+'\n\n'+song[1]+'\n\n'+song[11]+'\n\n'+song[2]+'\n\n'+song[7]+'\n\n'+song[5]+'\n\n'+song[7]))
    def test_verses_3_1_13_11_7_8_3_2_6(self):
        assert_that(self.temp([3, 0, 12, 10, 6, 7, 2, 1, 5]), is_(song[3]+'\n\n'+song[0]+'\n\n'+song[12]+'\n\n'+song[10]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[2]+'\n\n'+song[1]+'\n\n'+song[5]))
    def test_verses_3_4_7_5_13_11_9_6_9_2(self):
        assert_that(self.temp([3, 3, 6, 4, 12, 10, 8, 5, 8, 1]), is_(song[3]+'\n\n'+song[3]+'\n\n'+song[6]+'\n\n'+song[4]+'\n\n'+song[12]+'\n\n'+song[10]+'\n\n'+song[8]+'\n\n'+song[5]+'\n\n'+song[8]+'\n\n'+song[1]))
    def test_verses_12_10_6_11_4_1_2_11_9_6_10(self):
        assert_that(self.temp([12, 9, 5, 10, 3, 0, 1, 10, 8, 5, 9]), is_(song[12]+'\n\n'+song[9]+'\n\n'+song[5]+'\n\n'+song[10]+'\n\n'+song[3]+'\n\n'+song[0]+'\n\n'+song[1]+'\n\n'+song[10]+'\n\n'+song[8]+'\n\n'+song[5]+'\n\n'+song[9]))
    def test_verses_6_5_12_12_5_13_10_7_10_7_10_12(self):
        assert_that(self.temp([6, 4, 11, 11, 4, 12, 9, 6, 9, 6, 9, 11]), is_(song[6]+'\n\n'+song[4]+'\n\n'+song[11]+'\n\n'+song[11]+'\n\n'+song[4]+'\n\n'+song[12]+'\n\n'+song[9]+'\n\n'+song[6]+'\n\n'+song[9]+'\n\n'+song[6]+'\n\n'+song[9]+'\n\n'+song[11]))
    def test_verses_12(self):
        assert_that(self.temp([12]), is_(song[12]))
    def test_verses_8_4(self):
        assert_that(self.temp([8, 3]), is_(song[8]+'\n\n'+song[3]))
    def test_verses_7_6_10(self):
        assert_that(self.temp([7, 5, 9]), is_(song[7]+'\n\n'+song[5]+'\n\n'+song[9]))
    def test_verses_0_11_5_12(self):
        assert_that(self.temp([0, 10, 4, 11]), is_(song[0]+'\n\n'+song[10]+'\n\n'+song[4]+'\n\n'+song[11]))





