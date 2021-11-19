class Hamming():

    def distance(self, var_1, var_2):

        result = 0

        for i in range(len(var_1)):
            result = result + 1-(var_1[i]==var_2[i])
        
        return result