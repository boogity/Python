pyg = 'ay'
original = raw_input('Enter a word:')
word = original.lower()
first = word[0]
new_word = word[1:len(word)] + first + pyg

if len(original) > 0 and original.isalpha():
    print "Your word was " + original
    print "\n It shall be magically transformed into the piglatin word " + new_word + "! AMAZING!"
else:
    print 'empty'