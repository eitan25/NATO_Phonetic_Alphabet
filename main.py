import pandas

nato_df = pandas.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

while 1:
    word = input('insert a word: ').upper()
    try:
        nato_word = [nato_dict[i] for i in word]
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
    else:
        break
print(nato_word)
