#Lists
movies = ["When Harry Met Sally", "The hangover", "The Perks of bieng a Wallflower", "The Exorcist"]


movies.append("Jaws")

movies.insert(2, "Hustle")
movies.pop(0)
amber_movies = ["Just Go With It", "50 First Dates"]
our_fav_movies = movies + amber_movies


grades = [["bob", 82], ["Alice", 90],["Jeff", 73]]
bobs_grade = grades[0][1]
grades[0][1] = 83

#Tuples -Don not change
grades = ("a", "b", "c", "d", "f")
#print(grades[1])

#Looping
#for loops - start to finish an iterate
vegetables = ["cucumber", "spinach", "cabbage"]
#for x in vegetables:
  #print(x)

#Ping an ip address  

#while loops -execute as long as True
#i = 1
#while i < 10:
     #print(i)
     #i += 1

#ADVANCE STRINGS
my_name = "Douglas"
#print(my_name[0])
#print(my_name[-1])

sentence = "This is a sentence"
#print(sentence[:4])
#print(sentence.split())
sentence_split = sentence.split()
#print(sentence_split)
sentence_join = ' '.join(sentence_split)
#print(sentence_join)

qoute = "He said, \"give me all your money\""
#print(qoute)

too_much_space = "              hello           "
#print(too_much_space.strip())

#print("A" in "Apple") #True
#print("a" in "Apple") #False

letter = "A"
word = "Apple"
#print(letter.lower() in word.lower()) #Improved

#String Formating
movie = "The Hangover"
print("My favorite movie is {}.".format(movie))
print("My favorite movie is %s." % movie)
print(f"My favorite movie is {movie}.")

