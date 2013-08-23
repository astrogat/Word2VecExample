#figure out which word of a list doesn't belong!
#use word2vec for vectorization
#compute the mean of the vectors, find the one which is furthest!
import numpy as np
import os

def load_word2vec(dir):
        #new: since github has a 100M limit, load from a bunch of files in 
        #a directory
        word2vec = {}
        for path in os.listdir(dir):
                iword2vec = {}
                #load the word2vec features.
                with open(os.path.join(dir,path), 'r') as fin:
                        next(fin) #skip information on first line
                        for line in fin:
                                items = line.replace('\r','').replace('\n','').split(' ')
                                if len(items) < 10: continue
                                word = items[0]
                                vect = np.array([float(i) for i in items[1:] if len(i) > 1])
                                iword2vec[word] = vect
                
                word2vec.update(iword2vec)
                
        return word2vec
    
def get_furthest_word(words, word2vect):
        vectlist = []
        for word in words:
                #unknown word? 
                if word not in word2vect: return word
                vectlist.append(word2vect[word])
        mean = np.array(vectlist).mean(axis=0)

        #figure out which is furthest
        dists = [np.linalg.norm(v - mean) for v in vectlist]
        return words[np.argmax(dists)]

def a_is_to_b_as_x_is_to(a, b, x , word2vect):
        resultVect = x+(a-b)
        idx = (np.abs(word2vect-resultVect)).argmin()
        return array[idx]

def find_odd_one_out(word2vect):
        print "I try to find a word that is to c, as b is to a"
        print 'type three words seperated by spaces'
        while (True):
                words = raw_input('->').lower().split(' ')
                print 'I think ', a_is_to_b_as_x_is_to(words[1], words[2], words[3], word2vect), ' is to ', words[3], ' as ', word[2], ' is to ', word[1]
                
def a_is_to_b(word2vect):
        print "Hello human. I attempt to find a word in a list which doesn't belong."
        print 'Type several words separated by spaces. The more words you enter, the better I can guess.'
        
def main():
        print 'I have two modes of operation. I can find a word that doesn\'t belong.'
        print 'Or I can try to guess what word is similar to another, in the same was as two other words are similar'
        print 'loading knowledge from Wikipedia...should take 10-20 seconds'
        word2vec = load_word2vec('vectors')
        print 'For find the odd one out press 1. For a is to b, as c is to ? press 2.'
        while(true):
                choice = raw_input('->')
                if(choice == 1):
                        find_odd_one_out(word2vect)
                elif (choice == 2):
                        a_is_to_b(word2vect)
                
if __name__ == '__main__':
    main()
