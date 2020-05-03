#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname = input('Enter the file name: ') #ask the user for the file name
try:
    if len(fname)<1: fname='mbox-short.txt' #make this as the default file name when hitting Enter
    txt = open(fname) #open the file with a "try" to avoid crash for wrong names
except:
    print('File cannot be opened:', fname) #error message
    exit()
counts=dict() # make a dictionary
for line in txt: #go through the file line by line
    if line.startswith('From '): #find lines start with from
        l=line.split() # split the line into words and put them into l as a list
        time = l[5] #gets the email adress which always the second word after from
        hour = time.split(':') #split the time into a list
        h=hour[0] # gets only the hour
        counts[h] = counts.get(h,0)+1 #if this hour is not in the dictionary add it and if existed increase its value by one
t=list(counts.items()) #turn the dictionary into list
t.sort() #sort the list
for h,count in t: # go theough the list tuple by tuple
    print(h,count) #print the list by tuples.
