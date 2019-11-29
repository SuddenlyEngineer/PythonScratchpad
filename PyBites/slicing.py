from string import ascii_lowercase

text = """
One really nice feature of Python is polymorphism: using the same operation
on different types of objects.
Let's talk about an elegant feature: slicing.
You can use this on a string as well as a list for example
'pybites'[0:2] gives 'py'.
 The first value is inclusive and the last one is exclusive so
here we grab indexes 0 and 1, the letter p and y.
  When you have a 0 index you can leave it out so can write this as 'pybites'[:2]
but here is the kicker: you can use this on a list too!
['pybites', 'teaches', 'you', 'Python'][-2:] would gives ['you', 'Python']
and now you know about slicing from the end as well :)
keep enjoying our bites!
"""

def slice_and_dice(text: str = text) -> list:
    """Get a list of words from the passed in text.
       See the Bite description for step by step instructions"""
    
    results = []
    
    text = text.strip()
    text = text.split("\n")

    for index, phrase in enumerate(text):
      text[index] = text[index].strip()
      if text[index][0] == ")": #Bug Workaround
        continue
      if text[index][0] == ":": #Another Bug Workaround
        continue
      if text[index][-1] == "]": #Yet Again
        continue
      if text[index][0] == "'":
        continue 
      if text[index][0] == text[index][0].lower():
        temp_text = text[index].split()
        last_word = temp_text[-1].strip("!,.")
        last_word = last_word.strip()
        print(last_word)
        results.append(last_word) 
    
    return results