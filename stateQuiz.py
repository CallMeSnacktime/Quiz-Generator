#! python3

# randomQuizGenerator.py - Creates quizzes with questions and answers in
   # random order, along with the answer key.
import random

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico':
    'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia' : 'Richmond', 'Washington': 'Olympia', 'WestVirginia':
    'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
#Generate 35 quiz files
for quizNum in range(10):
    #Create the quiz and answer key files.
    quizFile = open(f'capitalsquiz{quizNum+1}.txt', 'w')
    answerKeyFile =  open(f'capitalsquiz_answers{quizNum + 1}.txt', 'w')


    #Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + f'State Capitals Quiz (Form{quizNum + 1})')
    quizFile.write('\n\n')

    #Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

    #Loop through all 50 states, making random question for each
    for questionNum in range(50):
        right = capitals[states[questionNum]]
        wrong = list(capitals.values())
        del wrong [wrong.index(right)]
        wrong = random.sample(wrong, 3)
        answerOptions = wrong + [right]
        random.shuffle(answerOptions)

        #Write the question and answer option to the quiz file.
        quizFile.write(f'{questionNum+1} What is the capital of {states[questionNum]}?\n')
        for i in range(4):
            quizFile.write(f"{'ABCD'[i]}. {answerOptions[i]}\n")

        quizFile.write('\n')

        #write the answer key to a file
        answerKeyFile.write(f"{questionNum+1}. {'ABCD'[answerOptions.index(right)]}")
    quizFile.close()
    answerKeyFile.close()

