import pickle

def get_word_set() -> set:
    
    
    """
    ###opening a text file with 5000ish 5 letter words to put into our  
    f = open("5_letter_words.txt", "r")
    word_set = set(f.read().split("\n"))
    
    ###how we store datastructures with pickle
    with open('5_letter_words.pickle', 'wb') as handle:
        pickle.dump(word_set, handle, protocol=pickle.HIGHEST_PROTOCOL)
    """

    word_set = None
        
    with open('5_letter_words.pickle', 'rb') as handle:
        word_set = pickle.load(handle)

    return word_set
