from random import Random
class Hangman:
    FILENAME = 'words.txt'
    def __init__(self, guesses = 12):
        self.word_bank = []
        self.word = self.select_word()
        self.guesses = guesses
        self.guess_str = '_ '*len(self.word)
    

    def open_file(self, filename):
        file_object=open(filename,'r')
        return file_object

    def read_file(self):
        file_object = self.open_file(hangman.FILENAME)

        for line in file_object:
            word = line.split()
            self.word_bank.append(word)


    def select_word(self):
        self.read_file()
        rand = Random()
        i = rand.randint(0,len(self.word_bank)-1)

        word = self.word_bank[i]
        return word[0]

    
    def get_guess(self):
        while True:
            guess = (input("\nWhat's your guess? Write any letter: ")).lower()
            
            while guess.isdigit():
                guess = (input('Please write a letter, not a digit: ')).lower()
            
            if guess in self.word:
                print('\nYou guessed correctly!')
                for i in range(len(self.word)):
                    if self.word[i] == guess:
                        a_list = list(self.guess_str)
                        a_list[i*2] = guess
                        self.guess_str = ''.join(a_list)
                
                if '_' not in self.guess_str:
                    print('Congratulations, you won! The word is: ', self.word)
                    return 'won'
                else:
                    print('The word is now: ', self.guess_str)
                    whole_word = input('Do you want to guess the whole word? Press y for yes, anything else for no: ').lower()
                    if whole_word == 'y':
                        ans = self.guess_whole_word()
                        if ans == 'won' or ans == 'lose':
                            return ans
            
            else:
                if self.guessed_wrong() == 'lose':
                    return 'lose'
    
    def guessed_wrong(self):
        self.guesses -= 1
        if self.guesses > 0:
            print('\nYou guessed wrong! Number of guesses left: ', self.guesses)
            print(self.guess_str)
        elif self.guesses <= 0:
            print('\nYou guessed wrong! You are out of guesses :(')
            return 'lose'

    def guess_whole_word(self):
        guessed_word = input('Type in the word you want to guess: ').lower()

        if guessed_word == self.word:
            print('Congratulations, you won! The word is: ', self.word)
            return 'won'
        
        else:
            if self.guessed_wrong() == 'lose':
                return 'lose'
    
    def add_word(self, word):
        self.word_bank.append(word)
        
        for word 



    def write_file(self):
        file_object=open(hangman.FILENAME,'w')
        return file_object

    def read_file(self):
        file_object = self.open_file('word_bank.txt')

        for line in file_object:
            word = line.split()
            self.word_bank.append(word)

def count_wins(a_list):
    wins = 0
    losses = 0
    for word in a_list:
        if word == 'won':
            wins += 1
        else:
            losses += 1
    
    return wins, losses


if __name__ == '__main__':
    wins_and_losses = []
    while True:
        number_of_guesses = input('\nSelect the number of guesses: ')
        if number_of_guesses.isdigit():
            h = Hangman(int(number_of_guesses))
            h.display_word()
            win_or_loss = h.get_guess()
            wins_and_losses.append(win_or_loss)
            ans = input("Do you want to play again? Put 'n' for no, anything else for yes: ").lower()
            if ans == 'n':
                break

        else:
            print('Please write an integer number!')
    
    wins, losses = count_wins(wins_and_losses)
    print('Number of wins: ', wins)
    print('Number of losses: ', losses)