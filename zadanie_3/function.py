song_text = open("laboratorium-6-DominikaBober/zadanie_3/song.txt","r+").read()
song_list = open("laboratorium-6-DominikaBober/zadanie_3/song.txt","r+").read().split("\n\n")

def dawaj_give(ver_1, ver_2 = None):

    try:

        if ver_1 == "all":
            return song_text
        elif type(ver_1) is int and type(ver_2) is int:
            result = ""
            list_verses = song_list[ver_1-1:ver_2]
            for i in range(len(list_verses)):
                if i == 0:
                    result = result + list_verses[i]
                else:
                    result = result + "\n\n" + list_verses[i]
            return result
        elif type(ver_1) is int:
            return song_list[ver_1-1]
        elif type(ver_1) is list:
            result = ""
            for i in range(len(ver_1)):
                if i == 0:
                    result = result + song_list[ver_1[i]-1]
                else:
                    result = result + "\n\n" + song_list[ver_1[i]-1]
            
            return result
        else:
            raise Exception("Wrong variable for verses")
    
    except ConnectionError:
        raise Exception("Wrong variable for verses")
