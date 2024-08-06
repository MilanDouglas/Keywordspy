#Reading and Writing files in Python

#READING FILES
#months = open('months.txt')
#print(months.read())
#print(months.mode)
#print(months.readable())
#print(months.readlines())
#for month in months:
  #print(month.strip())
#months.close()

#WRITING FILES

days = open('days.txt', "a")

days.write("\nWednesday")
days.close()

