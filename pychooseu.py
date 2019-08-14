import random
import os
import datetime

files = []
questions_dir = 'csvdata/'  # directory containing questions in csv
# grab all csv files from questions_dir
for f in os.listdir(questions_dir):
    if '.csv' in f:
        files.append(questions_dir+f)

# make output directory
if not os.path.exists('output'):
    os.makedirs('output')

# import all questions
questions_mix = []
for f in files:
    current_file = open(f, 'r')
    current_file.readline()  # skip header row; remove if no header row
    for row in current_file:
        questions_mix.append(row)
        inputs = row.split("|")

# randomize question order in list
random.shuffle(questions_mix)
running = True
correct = 0
incorrect = 0

write_output_to_file = True
output_text = ''

print("{} total questions from {} files ({})\n".format(len(questions_mix), len(files), files))
output_text += "{} total questions from {} files ({})\n".format(len(questions_mix), len(files), files)
print("Mixing questions up...")
output_text += "Mixing questions up..."

chosen_number_of_questions = input("How many questions do you want to try? (leave empty to try all)")
number_of_questions = len(questions_mix)

# get number of questions to display; newline will show all
if chosen_number_of_questions != '' and str.isdigit(chosen_number_of_questions) in range(1, len(questions_mix)):
    number_of_questions = int(chosen_number_of_questions)

print("Trying {} questions\n".format(number_of_questions))
output_text += "Trying {} questions\n\n".format(number_of_questions)

start_time = datetime.datetime.now()

for i in range(number_of_questions):
    question = questions_mix[i]
    parts = question.split("|")
    print("Question {}/{}\n{}\nA: {}\nB: {}\nC: {}\nD: {}"
          .format(i + 1, number_of_questions, parts[0], parts[1], parts[2], parts[3], parts[4]))
    output_text += "Question {}/{}\n{}\nA: {}\nB: {}\nC: {}\nD: {}"\
        .format(i + 1, number_of_questions, parts[0], parts[1], parts[2], parts[3], parts[4])

    correct_answer = str(parts[5][0]).upper()  # answer includes \n character; substring just the first character
    answer = ''
    while answer not in ['A', 'B', 'C', 'D', 'Q']:  # only allow A,B,C,D or Q to quit
        answer = str(input("Answer (q to quit): ")).upper()

    if 'Q' == answer:
        print("\nINCORRECT! (correct answer is {})\n".format(correct_answer))
        output_text += "\nINCORRECT! (correct answer is {})\n\n".format(correct_answer)
        break

    if correct_answer == answer:
        print("\nCORRECT!\n")
        output_text += "\nCORRECT!\n\n"
        correct += 1
    else:
        print("\nINCORRECT! (correct answer is {})\n".format(correct_answer))
        output_text += "\nINCORRECT! (correct answer is {})\n\n".format(correct_answer)
        incorrect += 1

end_time = datetime.datetime.now()
elapsed_time = end_time - start_time

print("\nScore: {}%\nYou answered {} correct and {} incorrect ({} total questions).".
      format(("{:.0f}".format(correct/number_of_questions*100)), correct, incorrect, number_of_questions))
output_text += "\nScore: {}%\nYou answered {} correct and {} incorrect ({} total questions)."\
    .format(("{:.0f}".format(correct/number_of_questions*100)), correct, incorrect, number_of_questions)

print("Elapsed time: {}".format(elapsed_time))
output_text += "\nElapsed time: {}".format(elapsed_time)

if write_output_to_file:
    output_file = open('output/output-{}.txt'.format(datetime.datetime.now().strftime('%m%d%Y-%H%M%S')), 'w')
    output_file.write(output_text)
    print('\nOutput written to {}'.format(output_file.name))
