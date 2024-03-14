# Instructions :
# The goal of the exercise is to create a class that will help you analyze a specific text. A text can be just a simple string, like “Today, is a happy day” or it can be an external text file.
#
#
#
# Part I
# First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”
#
# Create a class called Text that takes a string as an argument and store the text in a attribute.
# Hint: You need to manually copy-paste the text, straight into the code
#
# Implement the following methods:
# a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message.
# a method that returns the most common word in the text.
# a method that returns a list of all the unique words in the text.
#
#
# Part II
# Then, we will analyze a text coming from an external text file. Download the_stranger.txt file.
#
# Implement a classmethod that returns a Text instance but with a text file:
#
#     >>> Text.from_file('the_stranger.txt')
# Hint: You need to open and read the text from the text file.
#
#
# Now, use the provided the_stranger.txt file and try using the class you created above.


from collections import Counter
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
class Text:

    def __init__(self,text):
        self.text = text
        self.list_text = self.text.split()  # Broke string into a list of words.
        self.unique_words = set(self.list_text)  # Converted to string so to have uniques values.

    def frequency(self):
        repeated_words = [word for word in self.unique_words if self.list_text.count(word) > 1]
        # Created repeated list only with values grater to 1 so to know they are repeated.
        for words in self.unique_words:
            if words in repeated_words:  # Checking which words need this message
                print(f"Frequency of {words} : {self.list_text.count(words)}")
            else:
                print(f"Frequency of {words} : {None}")

    def most_common(self):
        count = Counter(self.list_text) # Function imported from the collection method.
        # Allows me to create a dictionary list, sort the words based on their repetition from grater to lower.
        highest_number = count.most_common(1)[0][1]  # Browse the dictionary for the highest value, always the 1st.
        most_frequent_word = [word for word,freq in count.items() if freq == highest_number]
        # I loop in the dictionary with the highest value looking for keys with same values

        print(f"Most common words in text is '{most_frequent_word}', with {highest_number} repetitions")

    def unique(self):
        unique_words_list = [word for word in self.unique_words if self.list_text.count(word) == 1]
        # Similar to frequency, here checking to equal 1.
        print(f"The following words are nor repeated: {unique_words_list}")

    @classmethod
    def get_words_from_file(cls, file_name):
        with open(dir_path + f'\\{file_name}', 'r') as file_obj:
            words_in_file = file_obj.read()
        return cls(text=words_in_file)


sample_text = "A good book would sometimes cost as much as a good house."
text_object = Text(sample_text)
text_object.frequency()
text_object.most_common()
text_object.unique()
print('>'*30)

#Exercise 2

the_stranger = Text.get_words_from_file('the_stranger.txt')
the_stranger.most_common()
the_stranger.unique()
the_stranger.frequency()


















