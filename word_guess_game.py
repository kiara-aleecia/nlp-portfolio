# kam180013 portfolio2 professor mazidi 4395
# https://github.com/kiara-aleecia/nlp-portfolio

import sys
import pathlib
import re
import nltk
import random
#from nltk import word_tokenize
#from nltk.corpus import stopwords

'''
to do:
open file, read in raw text
calculate lexical diversity of tokenized text -> output to 2 dec places
    [X]- lex div = # of unique tokens / total # of tokens
    - ****? before step b

preprocess raw text (separate function)
    [X]a. tokenize lowercase raw text
        - get rid of tokens that are nonalpha, stopwords, length <= 5
    [X]b. lemmatize tokens -> list of unique lemmas with set()
    [X]c. tag unique lemmas with pos -> print first 20 tagged
    [X]d. create list of noun lemmas
    [X]e. print # of tokens from (a) and # of nouns (d)
    [X]f. return tokens (not unique tokens) (step a) and nouns

make dict of {noun:# of noun in tokens}
    [X]- sort dict by frequency
    [X]- print 50 most common and their frequency
    [X]- save 50 most common to list -> game

guessing game (separate function)
    [X]- user starts with 5 points
    [X]- game ends when 0 points or "!" or finish guessing
    [X]- choose from list of 50 words
    [X]- display like hangman ( l o _ e r )
    [X]- add point to score for right guesses
    [X]- subtract from score for wrong guesses
    [X]- keep cumulative total score
    [X]- give user feedback for right and wrong guesses
link to project on github
'''

'''
calculate lexical diversity of tokenized text -> output to 2 dec places
    [X]- lex div = # of unique tokens / total # of tokens
'''
def calc_lexical_diversity(raw_text: str) -> int:
    # remove punctuation and numbers with a regular expression
    text = re.sub(r'[.?!,:;()\-\n\d]', ' ', raw_text.lower())
    #print(text)
    #tokens_incl_punct = nltk.word_tokenize(raw_text)
    tokens = nltk.word_tokenize(text)
    #print(f"tokens:\n\n\n\n\n {tokens}")

    unique_tokens = set(tokens)
    #print(f"unique tokens:\n\n\n\n\n {unique_tokens}")

    lex_div = round(len(unique_tokens)/len(tokens), 2)
    return lex_div

'''
preprocess raw text (separate function)
    [X]a. tokenize lowercase raw text
        - get rid of tokens that are nonalpha, stopwords, length <= 5
    [X]b. lemmatize tokens -> list of unique lemmas with set()
    [X]c. tag unique lemmas with pos -> print first 20 tagged
    [X]d. create list of noun lemmas
    [X]e. print # of tokens from (a) and # of nouns (d)
    [X]f. return tokens (not unique tokens) (step a) and nouns
'''
def preprocess_text(raw_text: str) -> tuple[list[str], list[tuple[str, str]]]:
    # PART A: get rid of tokens that are nonalpha, stopwords, length <= 5
    # remove punctuation and numbers with a regular expression
    text = re.sub(r'[.?!,:;()\-\n\d]', ' ', raw_text.lower())
    #print(text)
    tokens = nltk.word_tokenize(text)
    
    stop_words = set(nltk.corpus.stopwords.words('english'))
    pre_lemma = [w for w in tokens if not w in stop_words]
    #print(f"pre lemmatized tokens w/ len <= 5: {pre_lemma}")
    pre_lemma = [w for w in pre_lemma if len(w) > 5]
    #print(f"pre lemmatized tokens: {pre_lemma}")
    
    # PART B: lemmatize tokens
    wnl = nltk.stem.WordNetLemmatizer()
    lemmas = [wnl.lemmatize(w) for w in pre_lemma]
    #print(f"lemmatized: {lemmas}")
    unique_lemmas = set(lemmas)
    #print(f"unique lemmatized: {unique_lemmas}")

    # PART C: tag unique lemmas with pos and print first 20 
    unique_tagged = nltk.pos_tag(unique_lemmas)
    tagged = nltk.pos_tag(lemmas)
    print("\nUnique Lemmatized Tokens (no stopwords/no length<=5)")
    for w in range(20):
        print(f"{w+1}: {unique_tagged[w]}")
    print("\n")

    # PART D: create list of unique noun lemmas
    noun_unique_lemmas = [w for w in unique_tagged if "NN" in w[1]]
    noun_lemmas = [w for w in tagged if "NN" in w[1]]

    # PART E: print # of tokens from raw text (PART A) & # of nouns (PART D) 
    pre_lemma_l = len(pre_lemma)
    unique_noun_l = sum(map(len, noun_unique_lemmas))
    #noun_l = sum(map(len, noun_lemmas))

    print(f"Total number of word tokens: {pre_lemma_l}")
    print(f"Total number of unique nouns: {unique_noun_l}\n")
    #print(f"Total number of nouns: {noun_l}")

    # return tokens from step a and nouns (not set(nouns)) to be used later
    return pre_lemma, noun_lemmas

'''
make dict of {noun:# of noun in tokens}
    [X]- sort dict by frequency
    [X]- print 50 most common and their frequency
    [X]- save 50 most common to list -> game
'''
def noun_dict(tokens: list[str], nouns: list[tuple[str, str]]) -> tuple[str, int]:
    noun_count = {w[0]: tokens.count(w[0]) for w in nouns}

    # convert dict into list of tuples with .items()
    # use lamba function to send in first part of tuple and return value part
    sorted_noun_count = sorted(noun_count.items(), key=lambda x: x[1], reverse=True)

    # gets the first 50 most common words
    game_words = sorted_noun_count[:50]

    return game_words

'''
guessing game (separate function)
    [X]- user starts with 5 points
    [X]- game ends when 0 points or "!" or finish guessing
    [X]- choose from list of 50 words
    [X]- display like hangman ( l o _ e r )
    [X]- add point to score for right guesses
    [X]- subtract from score for wrong guesses
    [X]- keep cumulative total score
    [X]- give user feedback for right and wrong guesses
'''
def guessing_game(words: list[str]) -> None:
    print("\nLets play a word guessing game:\n")
    play = True
    score = 5
    #random.seed(1234) # for testing
    target = words[random.randint(0, 49)]
    target_chars = [c for c in target]
    guess_slots = "_" * len(target_chars)
    already_guessed = []

    while play:
        for i in range(len(guess_slots)):
            print(f"{guess_slots[i]} ", end='')

        guess = input("\nGuess a letter: ")

        if guess == "" or len(guess) != 1 or not guess.isalpha():
            print("Guesses should be one letter at a time")
            continue

        if guess in already_guessed:
            print(f"You've already guessed \"{guess}\"")
            continue
        else:
            already_guessed.append(guess)
            
        if guess == "!":
            play = False
            continue

        if guess in target:
            score += 1
            print(f"Right! Score is {score}")
            for c in range(len(guess_slots)):
                if target_chars[c] == guess:
                    guess_list = list(guess_slots)
                    guess_list[c] = guess
                    guess_slots = "".join(guess_list)
        else:
            score -= 1
            if score <= 0:
                print("Sorry, you lost!")
                play = False
                continue
            print(f"Sorry, guess again. Score is {score}")
            
        
        # reset for next game when all letters are guessed
        if "_" not in guess_slots:
            print("You solved it!")
            print(target)
            target = words[random.randint(0, 49)]
            target_chars = [c for c in target]
            guess_slots = "_" * len(target_chars)
            already_guessed = []
            continue

'''
main function (funct driver w/ minimal file processing and printing done)
'''
def main(filename):
    # manages execution of code with a "context manager" (in this case -> "open")
    # with statement also properly closes the file (even with an exception occurring)
    # code within the with statement executes with the file object as its context
    #with open(filename, "data.csv") as file:
    #    contents = file.read.splitlines()
    
    with open(pathlib.Path.cwd().joinpath(filename), 'r') as f:
        text_in = f.read()#.splitlines()
    
    lex_div = calc_lexical_diversity(text_in)
    print(f"lexical diversity: {lex_div}")

    # should return the two lists tokens from step a and unique nouns
    tokens, nouns = preprocess_text(text_in)

    game_nouns = noun_dict(tokens, nouns)
    print("Game Words:")

    for i in range(50):
        print(f"{i+1}: {game_nouns[i]}")
    
    guessing_game([w[0] for w in game_nouns])

    print("\n\nThanks for playing!!")
    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 word_guess_game.py filenamepath")
        quit()
        #sys.exit(1)
    #rel_path = sys.argv[1]


    # * is used to unpack the elements of a list (or any iterable) into
    # separate positional arguments

    main(*sys.argv[1:2])