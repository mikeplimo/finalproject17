print("Hello and welcome to this year's version of Michael's Trivia! You will be asked a several questions about topics that Michael likes. Try your best to get as close to a 99.9 as possible!")
print("When you answer a question, answer with the letter only.")
print("Good Luck!")
list_of_questions = [
    "Where is tennis believed to be originated from?\na - England\nb - France\nc - Canada\n\n\n",
    "When was the US Open founded?\na - yesterday\nb - 2020\nc - 1881\n\n\n",
    "The longest tennis match took 11 hours and 5 minutes to complete.\na - True\nb - False\n\n\n",
    "Who invented the tiebreaker, or tiebreak?\na - James Van Alen\nb - Roberto\nc - Frank\n\n\n",
    "Who hit the fastest serve in men's tennis of 263.44 km/h?\na - Sam Groth\nb - Roger Federer\nc - Naruto\n\n\n",
    "What year did the prize money for Wimbledon winners become equal for men and women?\na - 2000\nb - 2007\nc - 2010\n\n\n",
    "How many tons of strawberries are consumed during Wimbledon?\na - 1\nb - 0\nc - 24\n\n\n",
    "When was The Association of Tennis Professionals formed?\na - 1980\nb - 1972\nc - 1800\n\n\n",
    "An estimated 54,250 tennis balls are used during Wimbledon\na - True\nb - False\n\n\n",
    "Who were the first set of sisters to ever win Olympic gold medals in tennis?\na - Venus and Serena Williams\nb - idk\nc - maybe 'a'\n\n\n",
    "Which artist released the song, 'Pop Style' in 2016?\na - Drake\nb - Kendrick\nc - Thomas the Tank Engine\n\n\n",
    "Which artist released the song, 'Forrest Gump' in 2012?\na - Frank Ocean\nb - Kanye\nc - Justin Beiber\n\n\n",
    "Which artist released the song, 'Location' in 2017?\na - Cardi B\nb - Khalid\nc - Selena Gomez\n\n\n",
    "Which artist released the song, 'Mercy.1' in 2012?\na - Drake\nb - Kanye\nc - Snoop Dogg\n\n\n",
    "Which artist released the song, 'Thinkin Bout You' in 2012?\na - Frank Ocean\nb - Logic\nc - Michael Jackson\n\n\n",
    "Which artist released the song, 'Space Bound' in 2010?\na - Kanye\nb - Justin Beiber\nc - Eminem\n\n\n",
    "Which artist released the song, 'Take Me to Church' in 2014?\na - Hozier\nb - Elvis Crespo\nc - Meghan Trainor\n\n\n",
    "Which artist released the song, 'Riptide' in 2014?\na - Drake\nb - Vance Joy\nc - Eminem\n\n\n",
    "Which artist released the song, 'Hood Politics' in 2015?\na - Kanye\nb - Kendrick Lamar\nc - Eminem\n\n\n",
    "Which artist released the song, 'Sober' in 2014?\na - Kanye\nb - Childish Gambino\nc - EDEN\n\n\n",
    "Which of the following characters in the Dragon Ball series is bald?\na - Nappa\nb - Goku\nc - Gohan\n\n\n",
    "Who is the strongest Z-fighter?\na - Krillin\nb - Goku\nc - Piccolo\n\n\n",
    "Who was able to defeat the villain Cell?\na - Piccolo\nb - Gohan\nc - Vegeta\n\n\n",
    "Who killed Krillin on Namek?\na - Frieza\nb - Nail\nc - Vegeta\n\n\n",
    "What is the name of the fusion between Goten and Trunks?\na - Golents\nb - Gotenks\nc - Troten\n\n\n",
    "What is the name of the form used by Goku to defeat Kefla?\na - Super Saiyan Blue\nb - Kaio Ken\nc - Ultra Instinct\n\n\n",
    "How old is Majin Buu?\na - 10 billion years\nb - 5 Billion years\nc - 2018 years\n\n\n",
    "Which character is believed to have the most potential according to Vegeta?\na - Piccolo\nb - Trunks\nc - Gohan\n\n\n",
    "The English voice actor for Goku passed out after his epic transformation to Super Saiyan 4?\na - True\nb - False\n\n\n",
    "What is the name of Goku's main ki attack?\na - Kamehameha\nb - pew-pew\nc - Galik gun\n\n\n"
]
class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
def trivia_quiz(questions):
        grade = 0
        for question in questions:
            response = input(question.question)
            if response == question.answer:
                grade += 3.33
        print("Wow a " + str(grade) + "out of 99.9! Better luck next time.")
Question
trivia_quiz
questions = [
        Question(list_of_questions[0], "b"),
        Question(list_of_questions[1], "c"),
        Question(list_of_questions[2], "a"),
        Question(list_of_questions[3], "a"),
        Question(list_of_questions[4], "a"),
        Question(list_of_questions[5], "b"),
        Question(list_of_questions[6], "c"),
        Question(list_of_questions[7], "b"),
        Question(list_of_questions[8], "a"),
        Question(list_of_questions[9], "a"),
        Question(list_of_questions[10], "a"),
        Question(list_of_questions[11], "a"),
        Question(list_of_questions[12], "b"),
        Question(list_of_questions[13], "b"),
        Question(list_of_questions[14], "a"),
        Question(list_of_questions[15], "c"),
        Question(list_of_questions[16], "a"),
        Question(list_of_questions[17], "b"),
        Question(list_of_questions[18], "b"),
        Question(list_of_questions[19], "b"),
        Question(list_of_questions[20], "a"),
        Question(list_of_questions[21], "b"),
        Question(list_of_questions[22], "b"),
        Question(list_of_questions[23], "a"),
        Question(list_of_questions[24], "b"),
        Question(list_of_questions[25], "c"),
        Question(list_of_questions[26], "b"),
        Question(list_of_questions[27], "c"),
        Question(list_of_questions[28], "a"),
        Question(list_of_questions[29], "a")
    ]
trivia_quiz(questions)
