song_text = open("laboratorium-6-DominikaBober/zadanie_3/song.txt","r+").read()
song_list = open("laboratorium-6-DominikaBober/zadanie_3/song.txt","r+").read().split("\n\n")

def dawaj_give(ver_1):

    try:

        if ver_1 == "all":
            return song_text
    
    except ConnectionError:
        raise Exception("Wrong variable for verses")
