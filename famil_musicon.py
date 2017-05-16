import xlsxwriter
import Tkinter as tk
import random
import wx

root = tk.Tk()
questionlist = ["room quality", "food quality", "value for money","h", 'i', 'u', 'f', 'w', 'i', 'o', 'q', 'y', 't', 'r','v', 'p']
answers = []
# 187
print xlsxwriter.__file__
print tk.__file__
def ShowChoice():
    save_file = open('fam_musicon_results.csv', 'a')
    save_file.write('participant id, ')
    list_answers = []
    for q,v in answers:
        list_answers.append((q, v.get()))
        save_file.write(str(v.get())+',')
    save_file.write('\n')

    create_conditions_file(list_answers)

    root.destroy()


def create_conditions_file(list_answers):
    list_of_words = """position
heat
seashore
attack
trucks
doctor
sugar
purpose
ducks
authority
distribution
furniture
dinner
moon
sofa
morning
change
hydrant
mine
hair
sink
country
nest
eggs
calendar
tank
rabbits
degree
plantation
tub
girls
birth
plot
bite
women
mitten
skirt
pull
profit
reward
hot
cracker
power
queen
relation
jelly
need
look
humor
crack
bag
fog
robin
plate
art
maid
carpenter
coach
rain
finger
thing
property
worm
root
hate
chance
acoustics
respect
recess
sail
cobweb
rat
arch
error
squirrel
poison
geese
horse
blow
carriage
cent
collar
tail
oil
yarn
fear
spring
ink
cow
window
babies
structure
trees
addition
quiet
spade
mint
thrill
snail
taste""".split()
    notes = 'A B C D E F'.split()

    list_answers = sorted(list_answers, key=lambda tup: tup[1])
    quartile = len(list_answers) / 4
    id = 'something_1234.xlsx'
    random_conditions = random.sample(range(0, 6, 2), 3)
    mt = xlsxwriter.Workbook(id)
    mt_worksheet = mt.add_worksheet()
    id_of_random_word = random.sample(range(0, len(list_of_words)-1), quartile*3)

    mt_worksheet.write(0, 1, 'words1')
    mt_worksheet.write(0, 3, 'words2')
    mt_worksheet.write(0, 5, 'words3')
    mt_worksheet.write(0, random_conditions[0], 'NonFamMusicons')
    mt_worksheet.write(0, random_conditions[1], 'FamMusicons')
    mt_worksheet.write(0, random_conditions[2], 'Notes')

    note_id = random.sample(range(0, len(notes) - 1), quartile)

    for ans in range(quartile):
        mt_worksheet.write(ans+1, random_conditions[0], list_answers[ans][0])
        mt_worksheet.write(ans+1, 1, list_of_words[id_of_random_word[ans]])
        mt_worksheet.write(ans+1, random_conditions[1], list_answers[quartile*3 + ans][0])
        mt_worksheet.write(ans+1, 3, list_of_words[id_of_random_word[quartile + ans]])
        mt_worksheet.write(ans+1, random_conditions[2], notes[note_id[ans]] )
        mt_worksheet.write(ans+1, 5, list_of_words[id_of_random_word[quartile*2 + ans]])
    mt.close()


for counter, question in enumerate(questionlist, 1):
    tk.Label(root, text=question).grid(row=counter, column = 0)
    var = tk.IntVar()
    for i in range(1,6):
        button = tk.Radiobutton(root, variable = var, value = i)
        button.grid(row = counter, column = i)
    answers.append((question, var))
Submit = tk.Button(text="Submit", command=ShowChoice)
Submit.grid(row=counter+1 , columnspan=2)

root.mainloop()