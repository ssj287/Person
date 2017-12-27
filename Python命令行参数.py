def break_words(stuff):
    """This function will break up words for us"""
    words=stuff.split(' ')
    return words
def sort_words(words):
    """Sorted the words"""
    return sorted(words)
def print_first_word(words):
    """Prints the last word after popping it off"""
    word=words.pop(0)
    print(word)
def print_last_word(words):
    word=words.pop(-1)
    print(word)
def sort_sentence(sentence):
    words=break_words(sentence)
    return sort_words(words)
def print_first_and_last(sentence):
    words=break_words(sentence)
    print_first_word(words)
    print_last_word(words)
def print_first_and_last_sorted(sentence):
    words=sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
#python命令行输入下列命令
# import ex1
# sentence="All good things come to those who wait."
# words=ex1.break_words(sentence)
# words
# sorted_words=ex1.sort_words(words)
# sorted_words
# ex1.print_first_word(words)
# ex1.print_last_word(words)
# words
# ex1.print_first_word(sorted_words)
# ex1.print_last_word(sorted_words)
# sorted_words
# sorted_words=ex1.sort_sentence(sentence)
# sorted_words
# ex1.print_first_and_last(sentence)
# ex1.print_first_and_last_sorted(sentence)