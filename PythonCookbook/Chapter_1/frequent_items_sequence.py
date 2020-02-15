from collections import Counter

words = [
   'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
   'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
   'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
   'my', 'eyes', "you're", 'under'
]

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three) #Outputs [('eyes', 8), ('the', 5), ('look', 4)]

#Counter objects can be fed any sequence of hashable input items.
#Counters are dictionaries that map items to number of occurrences

word_counts['eyes'] #8

more_words = ['why','are','you','not','looking','in','my','eyes']
#for word in more_words:
#    word_counts[word] += 1

word_counts.update(more_words) #Updates counts instead of replacing them like a dict

word_counts['eyes'] #9

a = Counter(words)
b = Counter(more_words)

a
b

c = a+b #Combine counts
c
d = a-b #Subtact counts
d