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
        assert_that(self.temp(1, 2), is_(song[1]+'\n\n'+song[2]))
    def test_verses_from_1_to_3(self):
        assert_that(self.temp(1, 3), is_(song[1]+'\n\n'+song[2]+'\n\n'+song[3]))
    def test_verses_from_1_to_4(self):
        assert_that(self.temp(1, 4), is_(song[1]+'\n\n'+song[2]+'\n\n'+song[3]+'\n\n'+song[4]))
    def test_verses_from_1_to_5(self):
        assert_that(self.temp(1, 5), is_(song[1]+'\n\n'+song[2]+'\n\n'+song[3]+'\n\n'+song[4]+'\n\n'+song[5]))
    def test_verses_from_1_to_6(self):
        assert_that(self.temp(1, 6), is_(song[1]+'\n\n'+song[2]+'\n\n'+song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]))
    def test_verses_from_1_to_7(self):
        assert_that(self.temp(1, 7), is_(song[1]+'\n\n'+song[2]+'\n\n'+song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]))
    def test_verses_from_1_to_8(self):
        assert_that(self.temp(1, 8), is_(song[1]+'\n\n'+song[2]+'\n\n'+song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]))
    def test_verses_from_1_to_9(self):
        assert_that(self.temp(1, 9), is_(song[1]+'\n\n'+song[2]+'\n\n'+song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]))
    def test_verses_from_1_to_10(self):
        assert_that(self.temp(1, 10), is_(song[1]+'\n\n'+song[2]+'\n\n'+song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]+'\n\n'+song[10]))
    def test_verses_from_1_to_11(self):
        assert_that(self.temp(1, 11), is_(song[1]+'\n\n'+song[2]+'\n\n'+song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]+'\n\n'+song[10]+'\n\n'+song[11]))
    def test_verses_from_1_to_12(self):
        assert_that(self.temp(1, 12), is_(song[1]+'\n\n'+song[2]+'\n\n'+song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]+'\n\n'+song[10]+'\n\n'+song[11]+'\n\n'+song[12]))
    def test_verses_from_2_to_3(self):
        assert_that(self.temp(2, 3), is_(song[2]+'\n\n'+song[3]))
    def test_verses_from_2_to_4(self):
        assert_that(self.temp(2, 4), is_(song[2]+'\n\n'+song[3]+'\n\n'+song[4]))
    def test_verses_from_2_to_5(self):
        assert_that(self.temp(2, 5), is_(song[2]+'\n\n'+song[3]+'\n\n'+song[4]+'\n\n'+song[5]))
    def test_verses_from_2_to_6(self):
        assert_that(self.temp(2, 6), is_(song[2]+'\n\n'+song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]))
    def test_verses_from_2_to_7(self):
        assert_that(self.temp(2, 7), is_(song[2]+'\n\n'+song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]))
    def test_verses_from_2_to_8(self):
        assert_that(self.temp(2, 8), is_(song[2]+'\n\n'+song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]))
    def test_verses_from_2_to_9(self):
        assert_that(self.temp(2, 9), is_(song[2]+'\n\n'+song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]))
    def test_verses_from_2_to_10(self):
        assert_that(self.temp(2, 10), is_(song[2]+'\n\n'+song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]+'\n\n'+song[10]))
    def test_verses_from_2_to_11(self):
        assert_that(self.temp(2, 11), is_(song[2]+'\n\n'+song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]+'\n\n'+song[10]+'\n\n'+song[11]))
    def test_verses_from_2_to_12(self):
        assert_that(self.temp(2, 12), is_(song[2]+'\n\n'+song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]+'\n\n'+song[10]+'\n\n'+song[11]+'\n\n'+song[12]))
    def test_verses_from_3_to_4(self):
        assert_that(self.temp(3, 4), is_(song[3]+'\n\n'+song[4]))
    def test_verses_from_3_to_5(self):
        assert_that(self.temp(3, 5), is_(song[3]+'\n\n'+song[4]+'\n\n'+song[5]))
    def test_verses_from_3_to_6(self):
        assert_that(self.temp(3, 6), is_(song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]))
    def test_verses_from_3_to_7(self):
        assert_that(self.temp(3, 7), is_(song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]))
    def test_verses_from_3_to_8(self):
        assert_that(self.temp(3, 8), is_(song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]))
    def test_verses_from_3_to_9(self):
        assert_that(self.temp(3, 9), is_(song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]))
    def test_verses_from_3_to_10(self):
        assert_that(self.temp(3, 10), is_(song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]+'\n\n'+song[10]))
    def test_verses_from_3_to_11(self):
        assert_that(self.temp(3, 11), is_(song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]+'\n\n'+song[10]+'\n\n'+song[11]))
    def test_verses_from_3_to_12(self):
        assert_that(self.temp(3, 12), is_(song[3]+'\n\n'+song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]+'\n\n'+song[10]+'\n\n'+song[11]+'\n\n'+song[12]))
    def test_verses_from_4_to_5(self):
        assert_that(self.temp(4, 5), is_(song[4]+'\n\n'+song[5]))
    def test_verses_from_4_to_6(self):
        assert_that(self.temp(4, 6), is_(song[4]+'\n\n'+song[5]+'\n\n'+song[6]))
    def test_verses_from_4_to_7(self):
        assert_that(self.temp(4, 7), is_(song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]))
    def test_verses_from_4_to_8(self):
        assert_that(self.temp(4, 8), is_(song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]))
    def test_verses_from_4_to_9(self):
        assert_that(self.temp(4, 9), is_(song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]))
    def test_verses_from_4_to_10(self):
        assert_that(self.temp(4, 10), is_(song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]+'\n\n'+song[10]))
    def test_verses_from_4_to_11(self):
        assert_that(self.temp(4, 11), is_(song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]+'\n\n'+song[10]+'\n\n'+song[11]))
    def test_verses_from_4_to_12(self):
        assert_that(self.temp(4, 12), is_(song[4]+'\n\n'+song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]+'\n\n'+song[10]+'\n\n'+song[11]+'\n\n'+song[12]))
    def test_verses_from_5_to_6(self):
        assert_that(self.temp(5, 6), is_(song[5]+'\n\n'+song[6]))
    def test_verses_from_5_to_7(self):
        assert_that(self.temp(5, 7), is_(song[5]+'\n\n'+song[6]+'\n\n'+song[7]))
    def test_verses_from_5_to_8(self):
        assert_that(self.temp(5, 8), is_(song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]))
    def test_verses_from_5_to_9(self):
        assert_that(self.temp(5, 9), is_(song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]))
    def test_verses_from_5_to_10(self):
        assert_that(self.temp(5, 10), is_(song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]+'\n\n'+song[10]))
    def test_verses_from_5_to_11(self):
        assert_that(self.temp(5, 11), is_(song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]+'\n\n'+song[10]+'\n\n'+song[11]))
    def test_verses_from_5_to_12(self):
        assert_that(self.temp(5, 12), is_(song[5]+'\n\n'+song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]+'\n\n'+song[10]+'\n\n'+song[11]+'\n\n'+song[12]))
    def test_verses_from_6_to_7(self):
        assert_that(self.temp(6, 7), is_(song[6]+'\n\n'+song[7]))
    def test_verses_from_6_to_8(self):
        assert_that(self.temp(6, 8), is_(song[6]+'\n\n'+song[7]+'\n\n'+song[8]))
    def test_verses_from_6_to_9(self):
        assert_that(self.temp(6, 9), is_(song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]))
    def test_verses_from_6_to_10(self):
        assert_that(self.temp(6, 10), is_(song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]+'\n\n'+song[10]))
    def test_verses_from_6_to_11(self):
        assert_that(self.temp(6, 11), is_(song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]+'\n\n'+song[10]+'\n\n'+song[11]))
    def test_verses_from_6_to_12(self):
        assert_that(self.temp(6, 12), is_(song[6]+'\n\n'+song[7]+'\n\n'+song[8]+'\n\n'+song[9]+'\n\n'+song[10]+'\n\n'+song[11]+'\n\n'+song[12]))
    def test_verses_from_7_to_8(self):
        assert_that(self.temp(7, 8), is_(song[7]+'\n\n'+song[8]))
    def test_verses_from_7_to_9(self):
        assert_that(self.temp(7, 9), is_(song[7]+'\n\n'+song[8]+'\n\n'+song[9]))
    def test_verses_from_7_to_10(self):
        assert_that(self.temp(7, 10), is_(song[7]+'\n\n'+song[8]+'\n\n'+song[9]+'\n\n'+song[10]))
    def test_verses_from_7_to_11(self):
        assert_that(self.temp(7, 11), is_(song[7]+'\n\n'+song[8]+'\n\n'+song[9]+'\n\n'+song[10]+'\n\n'+song[11]))
    def test_verses_from_7_to_12(self):
        assert_that(self.temp(7, 12), is_(song[7]+'\n\n'+song[8]+'\n\n'+song[9]+'\n\n'+song[10]+'\n\n'+song[11]+'\n\n'+song[12]))
    def test_verses_from_8_to_9(self):
        assert_that(self.temp(8, 9), is_(song[8]+'\n\n'+song[9]))
    def test_verses_from_8_to_10(self):
        assert_that(self.temp(8, 10), is_(song[8]+'\n\n'+song[9]+'\n\n'+song[10]))
    def test_verses_from_8_to_11(self):
        assert_that(self.temp(8, 11), is_(song[8]+'\n\n'+song[9]+'\n\n'+song[10]+'\n\n'+song[11]))
    def test_verses_from_8_to_12(self):
        assert_that(self.temp(8, 12), is_(song[8]+'\n\n'+song[9]+'\n\n'+song[10]+'\n\n'+song[11]+'\n\n'+song[12]))
    def test_verses_from_9_to_10(self):
        assert_that(self.temp(9, 10), is_(song[9]+'\n\n'+song[10]))
    def test_verses_from_9_to_11(self):
        assert_that(self.temp(9, 11), is_(song[9]+'\n\n'+song[10]+'\n\n'+song[11]))
    def test_verses_from_9_to_12(self):
        assert_that(self.temp(9, 12), is_(song[9]+'\n\n'+song[10]+'\n\n'+song[11]+'\n\n'+song[12]))
    def test_verses_from_10_to_11(self):
        assert_that(self.temp(10, 11), is_(song[10]+'\n\n'+song[11]))
    def test_verses_from_10_to_12(self):
        assert_that(self.temp(10, 12), is_(song[10]+'\n\n'+song[11]+'\n\n'+song[12]))
    def test_verses_from_11_to_12(self):
        assert_that(self.temp(11, 12), is_(song[11]+'\n\n'+song[12]))

    # whole song test
    def test_whole_song(self):
        assert_that(self.temp("all"), is_(song_text))



help = open("help.txt","w+")
for i in range(1,13):
    for j in range(i+1, 13):
        result = f"song[{i}]"
        for k in range(i+1,j+1):
            result = result + f"+'\\n\\n'+song[{k}]"
        help.writelines(f"    def test_verses_from_{i}_to_{j}(self):\n        assert_that(self.temp({i}, {j}), is_({result}))\n")
help.close()

