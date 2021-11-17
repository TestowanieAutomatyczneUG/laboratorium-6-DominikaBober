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
    def test_verses_11(self):
        assert_that(self.temp([11]), is_(song[11]))
    def test_verses_5_1(self):
        assert_that(self.temp([5, 1]), is_(song[5]+'\n\n'+song[1]))
    def test_verses_8_8_11(self):
        assert_that(self.temp([8, 8, 11]), is_(song[8]+'\n\n'+song[8]+'\n\n'+song[11]))
    def test_verses_6_3_3_0(self):
        assert_that(self.temp([6, 3, 3, 0]), is_(song[6]+'\n\n'+song[3]+'\n\n'+song[3]+'\n\n'+song[0]))
    def test_verses_2_1_12_12_9(self):
        assert_that(self.temp([2, 1, 12, 12, 9]), is_(song[2]+'\n\n'+song[1]+'\n\n'+song[12]+'\n\n'+song[12]+'\n\n'+song[9]))
    def test_verses_1_2_0_5_1_10(self):
        assert_that(self.temp([1, 2, 0, 5, 1, 10]), is_(song[1]+'\n\n'+song[2]+'\n\n'+song[0]+'\n\n'+song[5]+'\n\n'+song[1]+'\n\n'+song[10]))
    def test_verses_1_9_0_9_12_0_7(self):
        assert_that(self.temp([1, 9, 0, 9, 12, 0, 7]), is_(song[1]+'\n\n'+song[9]+'\n\n'+song[0]+'\n\n'+song[9]+'\n\n'+song[12]+'\n\n'+song[0]+'\n\n'+song[7]))
    def test_verses_4_5_12_0_9_5_8_6(self):
        assert_that(self.temp([4, 5, 12, 0, 9, 5, 8, 6]), is_(song[4]+'\n\n'+song[5]+'\n\n'+song[12]+'\n\n'+song[0]+'\n\n'+song[9]+'\n\n'+song[5]+'\n\n'+song[8]+'\n\n'+song[6]))
    def test_verses_11_11_4_1_10_0_4_3_11(self):
        assert_that(self.temp([11, 11, 4, 1, 10, 0, 4, 3, 11]), is_(song[11]+'\n\n'+song[11]+'\n\n'+song[4]+'\n\n'+song[1]+'\n\n'+song[10]+'\n\n'+song[0]+'\n\n'+song[4]+'\n\n'+song[3]+'\n\n'+song[11]))
    def test_verses_8_4_6_4_3_6_11_5_6_1(self):
        assert_that(self.temp([8, 4, 6, 4, 3, 6, 11, 5, 6, 1]), is_(song[8]+'\n\n'+song[4]+'\n\n'+song[6]+'\n\n'+song[4]+'\n\n'+song[3]+'\n\n'+song[6]+'\n\n'+song[11]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[1]))
    def test_verses_2_12_12_9_2_6_9_5_11_7_0(self):
        assert_that(self.temp([2, 12, 12, 9, 2, 6, 9, 5, 11, 7, 0]), is_(song[2]+'\n\n'+song[12]+'\n\n'+song[12]+'\n\n'+song[9]+'\n\n'+song[2]+'\n\n'+song[6]+'\n\n'+song[9]+'\n\n'+song[5]+'\n\n'+song[11]+'\n\n'+song[7]+'\n\n'+song[0]))
    def test_verses_3_5_11_0_12_7_9_0_2_7_7_0(self):
        assert_that(self.temp([3, 5, 11, 0, 12, 7, 9, 0, 2, 7, 7, 0]), is_(song[3]+'\n\n'+song[5]+'\n\n'+song[11]+'\n\n'+song[0]+'\n\n'+song[12]+'\n\n'+song[7]+'\n\n'+song[9]+'\n\n'+song[0]+'\n\n'+song[2]+'\n\n'+song[7]+'\n\n'+song[7]+'\n\n'+song[0]))
    def test_verses_7(self):
        assert_that(self.temp([7]), is_(song[7]))
    def test_verses_2_11(self):
        assert_that(self.temp([2, 11]), is_(song[2]+'\n\n'+song[11]))
    def test_verses_5_4_3(self):
        assert_that(self.temp([5, 4, 3]), is_(song[5]+'\n\n'+song[4]+'\n\n'+song[3]))
    def test_verses_5_1_4_10(self):
        assert_that(self.temp([5, 1, 4, 10]), is_(song[5]+'\n\n'+song[1]+'\n\n'+song[4]+'\n\n'+song[10]))
    def test_verses_0_3_10_12_3(self):
        assert_that(self.temp([0, 3, 10, 12, 3]), is_(song[0]+'\n\n'+song[3]+'\n\n'+song[10]+'\n\n'+song[12]+'\n\n'+song[3]))
    def test_verses_7_6_7_0_9_6(self):
        assert_that(self.temp([7, 6, 7, 0, 9, 6]), is_(song[7]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[0]+'\n\n'+song[9]+'\n\n'+song[6]))
    def test_verses_11_5_3_0_2_1_10(self):
        assert_that(self.temp([11, 5, 3, 0, 2, 1, 10]), is_(song[11]+'\n\n'+song[5]+'\n\n'+song[3]+'\n\n'+song[0]+'\n\n'+song[2]+'\n\n'+song[1]+'\n\n'+song[10]))
    def test_verses_3_0_8_7_2_8_11_5(self):
        assert_that(self.temp([3, 0, 8, 7, 2, 8, 11, 5]), is_(song[3]+'\n\n'+song[0]+'\n\n'+song[8]+'\n\n'+song[7]+'\n\n'+song[2]+'\n\n'+song[8]+'\n\n'+song[11]+'\n\n'+song[5]))
    def test_verses_10_11_7_12_10_3_2_9_9(self):
        assert_that(self.temp([10, 11, 7, 12, 10, 3, 2, 9, 9]), is_(song[10]+'\n\n'+song[11]+'\n\n'+song[7]+'\n\n'+song[12]+'\n\n'+song[10]+'\n\n'+song[3]+'\n\n'+song[2]+'\n\n'+song[9]+'\n\n'+song[9]))
    def test_verses_11_7_11_11_4_8_1_5_7_8(self):
        assert_that(self.temp([11, 7, 11, 11, 4, 8, 1, 5, 7, 8]), is_(song[11]+'\n\n'+song[7]+'\n\n'+song[11]+'\n\n'+song[11]+'\n\n'+song[4]+'\n\n'+song[8]+'\n\n'+song[1]+'\n\n'+song[5]+'\n\n'+song[7]+'\n\n'+song[8]))
    def test_verses_0_8_9_2_6_5_3_1_3_4_10(self):
        assert_that(self.temp([0, 8, 9, 2, 6, 5, 3, 1, 3, 4, 10]), is_(song[0]+'\n\n'+song[8]+'\n\n'+song[9]+'\n\n'+song[2]+'\n\n'+song[6]+'\n\n'+song[5]+'\n\n'+song[3]+'\n\n'+song[1]+'\n\n'+song[3]+'\n\n'+song[4]+'\n\n'+song[10]))
    def test_verses_1_3_2_3_6_11_9_9_2_8_7_5(self):
        assert_that(self.temp([1, 3, 2, 3, 6, 11, 9, 9, 2, 8, 7, 5]), is_(song[1]+'\n\n'+song[3]+'\n\n'+song[2]+'\n\n'+song[3]+'\n\n'+song[6]+'\n\n'+song[11]+'\n\n'+song[9]+'\n\n'+song[9]+'\n\n'+song[2]+'\n\n'+song[8]+'\n\n'+song[7]+'\n\n'+song[5]))
    def test_verses_3(self):
        assert_that(self.temp([3]), is_(song[3]))
    def test_verses_6_4(self):
        assert_that(self.temp([6, 4]), is_(song[6]+'\n\n'+song[4]))
    def test_verses_12_12_6(self):
        assert_that(self.temp([12, 12, 6]), is_(song[12]+'\n\n'+song[12]+'\n\n'+song[6]))
    def test_verses_6_10_2_4(self):
        assert_that(self.temp([6, 10, 2, 4]), is_(song[6]+'\n\n'+song[10]+'\n\n'+song[2]+'\n\n'+song[4]))
    def test_verses_7_8_11_8_12(self):
        assert_that(self.temp([7, 8, 11, 8, 12]), is_(song[7]+'\n\n'+song[8]+'\n\n'+song[11]+'\n\n'+song[8]+'\n\n'+song[12]))
    def test_verses_8_0_12_5_2_7(self):
        assert_that(self.temp([8, 0, 12, 5, 2, 7]), is_(song[8]+'\n\n'+song[0]+'\n\n'+song[12]+'\n\n'+song[5]+'\n\n'+song[2]+'\n\n'+song[7]))
    def test_verses_11_11_8_6_4_8_2(self):
        assert_that(self.temp([11, 11, 8, 6, 4, 8, 2]), is_(song[11]+'\n\n'+song[11]+'\n\n'+song[8]+'\n\n'+song[6]+'\n\n'+song[4]+'\n\n'+song[8]+'\n\n'+song[2]))
    def test_verses_2_11_3_10_4_2_1_11(self):
        assert_that(self.temp([2, 11, 3, 10, 4, 2, 1, 11]), is_(song[2]+'\n\n'+song[11]+'\n\n'+song[3]+'\n\n'+song[10]+'\n\n'+song[4]+'\n\n'+song[2]+'\n\n'+song[1]+'\n\n'+song[11]))
    def test_verses_0_11_3_9_9_1_9_0_5(self):
        assert_that(self.temp([0, 11, 3, 9, 9, 1, 9, 0, 5]), is_(song[0]+'\n\n'+song[11]+'\n\n'+song[3]+'\n\n'+song[9]+'\n\n'+song[9]+'\n\n'+song[1]+'\n\n'+song[9]+'\n\n'+song[0]+'\n\n'+song[5]))
    def test_verses_0_11_3_12_11_7_9_7_0_2(self):
        assert_that(self.temp([0, 11, 3, 12, 11, 7, 9, 7, 0, 2]), is_(song[0]+'\n\n'+song[11]+'\n\n'+song[3]+'\n\n'+song[12]+'\n\n'+song[11]+'\n\n'+song[7]+'\n\n'+song[9]+'\n\n'+song[7]+'\n\n'+song[0]+'\n\n'+song[2]))
    def test_verses_1_4_0_3_7_7_9_5_3_9_8(self):
        assert_that(self.temp([1, 4, 0, 3, 7, 7, 9, 5, 3, 9, 8]), is_(song[1]+'\n\n'+song[4]+'\n\n'+song[0]+'\n\n'+song[3]+'\n\n'+song[7]+'\n\n'+song[7]+'\n\n'+song[9]+'\n\n'+song[5]+'\n\n'+song[3]+'\n\n'+song[9]+'\n\n'+song[8]))
    def test_verses_7_3_2_11_1_12_10_0_3_0_2_8(self):
        assert_that(self.temp([7, 3, 2, 11, 1, 12, 10, 0, 3, 0, 2, 8]), is_(song[7]+'\n\n'+song[3]+'\n\n'+song[2]+'\n\n'+song[11]+'\n\n'+song[1]+'\n\n'+song[12]+'\n\n'+song[10]+'\n\n'+song[0]+'\n\n'+song[3]+'\n\n'+song[0]+'\n\n'+song[2]+'\n\n'+song[8]))
    def test_verses_0(self):
        assert_that(self.temp([0]), is_(song[0]))
    def test_verses_0_0(self):
        assert_that(self.temp([0, 0]), is_(song[0]+'\n\n'+song[0]))
    def test_verses_2_5_9(self):
        assert_that(self.temp([2, 5, 9]), is_(song[2]+'\n\n'+song[5]+'\n\n'+song[9]))
    def test_verses_10_1_5_8(self):
        assert_that(self.temp([10, 1, 5, 8]), is_(song[10]+'\n\n'+song[1]+'\n\n'+song[5]+'\n\n'+song[8]))



