#Exercise1
word_list = []
print("Enter a comma-separated sequence of words.")
words_input = input("Begin writing:")
word_list = sorted(word.strip() for word in words_input.split(','))
print(','.join(word_list))

#Exercise2
def longest_word(sentence):
    words = sentence.split()
    words = [word.strip("',.") for word in words]
    longest = max(words, key=len)
    return longest

input_sentence = "Margaret's toy is a pretty doll."
result = longest_word(input_sentence)
print("Longest word:", result)
