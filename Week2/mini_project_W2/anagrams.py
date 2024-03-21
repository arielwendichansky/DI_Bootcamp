from mini_project_w2 import AnagramChecker


def blue(text, style='normal'):
 styles = {
  'normal': '\033[94m',  # Blue color
  'bold': '\033[94;1m'  # Blue color with bold text
 }
 return f"{styles.get(style, styles['normal'])}{text}\033[0m"

while True:  # Continue until exit or invalid answer
 print("Welcome to the Anagram's!! Select your choice to begin: ")
 print("1 - I want to input a word.")
 print("2 - I want to exit.")
 answ = int(input(">>> "))
 if answ == 1:
  user_word_raw = input("Which word you want to use? '\n'"
                    ">>> ")
  user_word = user_word_raw.rstrip().lstrip()  # Cleaning the user input by taking spaces to right and left
  for chr in user_word:
   if ' 'in user_word or chr.isalpha() == False:  # Check for valid input
    print("You can only input one word man and letters NO numbers or special characters!")
    break
   else:
    playing = AnagramChecker(user_word)
    print('*' * 50)
    print(blue(f"YOUR WORD: {user_word.upper()}\n"
          f"This is a valid English word.",'bold'))
    playing.get_anagrams()
    print('*'*50)
    break
 elif answ == 2:
  print("Thanks for playing!")
  break
 else:
  print("You enter something wrong dude! bye!")
  break

