# #Exercise1
# import random
#
#
# def display_message():
#     print("Im learning data analytics in DI")
#
# print('>'*30)
# display_message()
# #Exercise2
# def favorite_book (title):
#     print(f"One of my favorite books is {title}")
#
# favorite_book("harry potter")
# print('>'*30)
# #Exercise3
# def describe_city(city,country = "Argentina"):
#     print(f"{city} is in {country}")
#
# describe_city("NY","USA")
# print('>'*30)
# #Exercise4
# import random
# def randomize (number):
#     if number in range(1,101):
#         print(f"The value you input is {number} and it randomize to {random.randrange(0
#                                                                                       ,100)}")
#     else:
#         print(f"The chosen number: {number} doesn't fall in the range")
# randomize(100)
# print('>'*30)
# #Exercise5
# def make_shirt(size="L",text="I love Python"):
#     size = input("what's your size? ")
#     shirt = (f"The size of the shirt is {size} and the text is {text}")
#     print(shirt)
#     return size,text,shirt
#
# make_shirt()
# print('>'*6)
#
# def make_shirt(*args):
#     size = input("what's your size? ")
#     text = input("what you want your shirt to say? ")
#     print(f"The size of the shirt is {size} and the text is {text}")
#     return(size,text)
#
# make_shirt()
#
# print('>'*30)
#Exercise6
# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# def show_magicians():
#     for magician in magician_names:
#         print (magician)
# show_magicians()
#
# the_great=[]
# def make_great():
#    while len(magician_names) != 0:
#        making_great = magician_names.pop() + " the great"
#        the_great.append(making_great)
#
#    print(the_great)
# make_great()
# print('>'*30)
#Exercise7
import random
# def season_month (season_month,months = None):
#     if months is None:
#         months = {"summer":(7,8,9,10),"fall":(11,12),"winter":(1,2,3,4),"spring":(5,6)}
#     month_season = months[season_month]
#
#
# def get_random_temp(season, seasons_ranges=None):
#     if seasons_ranges is None:
#         seasons_ranges = {"summer": (24, 40), "spring": (16, 23), "fall": (0, 16), "winter": (-10, -1)}
#     temp_range = seasons_ranges[season]
#     return random.randrange(*temp_range)
#
#
#
# def main():
#     select_season = input("Choose a season you want to know?")
#     lower_select_season = select_season.lower()
#     temperature = float(get_random_temp(lower_select_season))
#     print(f"The temperature at the moment is {temperature} Celsius degrees")
#     if temperature < 0:
#         print("Brrr, that’s freezing! Wear some extra layers today")
#     elif 0 <= temperature <= 16:
#         print("Quite chilly! Don't forget your coat")
#     elif 16 <= temperature <= 23:
#         print("Feel like summer is coming! But take a sweater with you")
#     elif 24 <= temperature <= 32:
#         print("Summer time sweet!")
#     elif 32 <= temperature <= 40:
#         print("You know a swimming pool where to go?!")
# main()

# print('>'*30)
#Exercise8

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

# print(data[0]["answer"])
correct=[]
wrong_answer=[]
def questions():
    for question,answer in enumerate(data):
        print(data[question]["question"])
        user_answer = input("Answer: ")
        if data[question]["answer"].lower() == user_answer.lower():
            correct.append(data[question]["answer"])
        else:
            wrong_answer.append(data[question]["answer"])

def score (*args):
    correct_ans = len(correct)
    incorrect_ans = len(wrong_answer)
    return (correct_ans,incorrect_ans)
def print_results():
    print(f"You've answer {correct_ans} correct")
    print(f"You've have {incorrect_ans} answers, these are {wrong_answer}")

questions()
score()
correct_ans,incorrect_ans = score()
print_results()

while correct_ans < 3:
    print("Lets try it once again.")
    questions()
    print_results()

