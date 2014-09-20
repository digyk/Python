import random


class Scramble:

    word_list = [''' look at comment above ''']
    count = 0
    attempts = 0
    correct = 0
    wrong = 0

    def __init__(s):
        print("Welcome to Scramble!")
        while s.play():
            word = s.new_ran_word()
            scrambled = s.scramble(word)

            s.count += 1
            s.attempts += 1

            print("--------")
            print("Round", s.count)
            phrase = "Guess the scrambled word:\n" + scrambled + "\n> "
            guess = input(phrase)

            while s.attempts < 4:
                if guess.lower() == word:
                    s.correct_ans()
                    break
                elif s.attempts == 3:
                    print("Oops! The word was", word, "\n")
                    s.wrong += 1
                    s.attempts = 0
                    break
                else:
                    guess = input("Try again!\n> ")
                    s.attempts += 1

    def play(self):
        a = input("Press [enter] to continue or [any key][enter] to exit\n")
        if a != '':
            print("--------Stats--------")
            print("Words attempted:  ", self.count)
            print("Correct guesses:  ", self.correct)
            print("Incorrect guesses:", self.wrong)
            score = self.get_score()
            print("You scored " + score + "%")
            print("\nThanks for playing!\n")
            return False
        return True

    def new_ran_word(self):
        l = self.word_list
        return l[random.randrange(len(l))].lower()

    def scramble(self, w):
        pos_taken = []
        new = list(w)

        for x in w:
            new_pos = random.randrange(len(w))
            while new_pos in pos_taken:
                new_pos = random.randrange(len(w))

            pos_taken.append(new_pos)
            new[new_pos] = x

        s = ""
        for c in new:
            s += c

        if s == w:
            return self.scramble(w)
        else:
            return s

    def correct_ans(s):
        print("Well done!")
        print("You got it in", s.attempts, "attempt(s)!\n")
        s.attempts = 0
        s.correct += 1

    def get_score(s):
        try:
            return str(int(s.correct*100/s.count))
        except ZeroDivisionError:
            return "0"

scramble = Scramble()