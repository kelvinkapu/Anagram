# your code goes here!
class Anagram:
    def __init__(self, word="listen"):
        self.word = word

    def match(self, my_list):
        # self.word=word
        new_list = []
        sorted_word = sorted(self.word)
        for item in my_list:
            sorted_item = sorted(item)
            if sorted_item == sorted_word:
                new_list.append(item)
        return new_list
        

                
        
        
        # (char for char in word)








        # new_list = []
        # if sorted(char for char in word) == sorted(item for item in my_list)(item[0] += 1):
        #     return new_list.append(item)

        #   print([(sort(word) == sorted(item))for item in my_list item += 1]):
# print(match(['enlists', 'google', 'inlets', 'banana'],'listen'))


