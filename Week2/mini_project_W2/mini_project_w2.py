import os
from itertools import permutations
dir_path = os.path.dirname(os.path.realpath(__file__))

class AnagramChecker:
    def __init__(self,input_word):
        with open(dir_path + '\\sowpods.txt', 'r') as file_obj:
            self.word_list = set(word.strip().lower() for word in file_obj)
        self.input_word = input_word.strip().lower()

    def is_valid_word(self):
        if self.input_word in self.word_list:
            return True
        else:
            print("You input a non English word")

    def get_anagrams(self):
        if self.is_valid_word:
            input_length = len(self.input_word)
            perm_word = permutations(self.input_word)
            possible_words = []
            anagram_list = []
            for perm_word in list(perm_word):
                possible_words.append(''.join(perm_word))

            for word in self.word_list:
                if len(word) == input_length and word in possible_words:
                    anagram_list.append(word)
        print(f"Anagrams for your word: {', '.join(anagram_list)}")



Try = AnagramChecker('meat')
Try.is_valid_word()
Try.get_anagrams()
