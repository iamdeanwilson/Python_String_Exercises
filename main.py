# ---- Exercise 2: Bracket Notation Basics ----

text = 'Strings_are_sequences_of_characters.'
word = 'tomato'

# 1. Print a slice of the first 12 characters from 'text'.

print(text[0:11])

# 2. Print a slice of the last 12 characters from 'text'. You should NOT have to count the index values yourself!

print(text[-12:])

# 3. Print a slice of the middle 12 characters from 'text'.

print(text[12:24])

# ---- Exercise 3: Looping Through a String ----

# Use index values to loop backwards through 'word'.

# 1. Print 1 letter per line.

for i in range(len(word)):
  print(word[i])

# 2. Refactor the code to use the accumulator pattern to build up and print the reversed string. For example, if given 'good', print 'doog' on one line.
  
reversed_word = ''

for i in range(len(word)):
  reversed_word = word[i] + reversed_word

print(reversed_word)

# 3. Refactor the code to print a combination of the original and reversed string. For example, given 'tomato', print 'tomatootamot'. (If you want to be fancy, print 'tomato | otamot').

print(word + " | " + reversed_word)

# ---- String Methods and Data Types ----

num = 1001

# Throws an error:

#print(len(num))

# 1. Use type conversion to print the length (number of digits) of an integer.

print(len(str(5165144)))


# 2. Print the length of 'num'

print(len(str(num)))


# 3. Print the number of digits in a FLOAT value (e.g. num = 123.45 has 5 digits but a length of 6).

num = 123.45

print(len(str(num).replace('.', '')))


# 4. Experiment! What if num could be EITHER an integer or a decimal?  Add an if/else statement so your code can handle both cases. (Hint: Consider using the find() method or the in operator to check if num contains a decimal point).

if str(num).find('.') == -1:
  print(len(str(num)))
else:
  print(len(str(num).replace('.', '')))

# ---- Loops, Conditionals, and Strings! ----

word = 'bag'

# 1. Set up a loop to iterate through the string of lowercase vowels, 'aeiou'.

vowels = 'aeiou'

for vowel in vowels:
  print(vowel)


# 2 & 3. Inside the loop, create and print a new string from 'word', but with a different vowel. Use the replace() method.

for vowel in vowels:
  new_word = word.replace('a', vowel)
  print(new_word)

# 4. After you have your code working, try other words besides 'bag'.

# ---- Method Chaining Fun with DNA ----

dna = " TCG-TAC-gaC-TAC-CGT-CAG-ACT-TAa-CcA-GTC-cAt-AGA-GCT    "

# First, print out the dna strand in it's current state.

print(dna)

# 1. Use the strip() method to remove the leading and trailing whitespace, then print the result.

print(dna.strip(' '))


# 2. Change all of the letters in the dna string to UPPERCASE, then print the result.

print(dna.upper())

# 3. Note that after applying the methods above, the original, flawed string is still stored in dna. To fix this, we need to reassign the changes to back to dna.
# Apply these fixes to your code so that print(dna) shows the DNA strand in UPPERCASE with no whitespace.

dna = dna.upper().strip(' ')

print(dna)

# 4 a. Use replace() to remove the gene 'GCT', then print the altered strand. Don’t forget about the extra hyphen!

print(dna.replace('-GCT', ''))

# 4 b. Look for the gene 'CAT' with find(). If found print, 'CAT gene found', otherwise print, 'CAT gene NOT found'.

if dna.find('CAT') != -1:
  print('CAT gene found')
else:
  print('CAT gene NOT found')


# 4 c. Use count() to find the number of hyphens in the string, then print the number of genes (sets of 3 letters) in the dna strand. Note that the number of genes will be 1 more than the number of hyphens.

hyphen_count = dna.count('-')

print("Gene count = " + str(hyphen_count + 1))


# 4 d. Use an f-string to print the output "The DNA string is ___ characters long and contains ___ genes." Fill in the blanks with the length of the string and the number of genes.

print(f"The DNA string is {len(dna)} characters long and contains {hyphen_count + 1} genes.")


# ---- Debugging Practice ----

# 1.  Assign your favorite number and word to the two variables.

my_num = 7
my_word = 'Speghetti'

# a) Use format() and index values to print the string, "Here is my number: ___, and here is my word: ___, and here is my number again: ___."

print(f"Here is my number: {my_num}, and here is my word: {my_word}, and here is my number again: {my_num}.")


# b) Print the string, "Here is my word 3 times: ___/___/___, and here is my number squared: ___."

print(f"Here is my word 3 times: {my_word * 3}, and here is my number squared: {my_num ** 2}.")
