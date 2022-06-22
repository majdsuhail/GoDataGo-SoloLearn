#This code is flexible, meaning you can add more values to every word then adding the year to show more data 
#And even adding new words with their own statistics

#1-To show all statistics type all.

#2-To show specific statistics, type the word you want to show statistics of.

#3-Seperate words with space if there are more than one word

#   ex1:all
#   ex2:C#
#   ex3:python java etc.


data= {"Javascript":[69.8,62.5],"SQL":[57.0,51.2],"Java":[45.3,39.7],"Python":[38.8,32.0],"C#":[34.4,34.1],"PHP":[30.7,28.1],"C++":[25.4,22.3],"C":[23.0,19.0],"Typescript":[17.4,9.5],"Ruby":[10.1,9.1],"Swift":[8.1,6.5],"Assembly":[7.4,5.0],"Go":[7.1,4.3],"Objective-C":[7.0,6.4],"VB.NET":[6.7,6.2],"R":[6.1,4.5],"Matlab":[5.8,4.3],"VBA":[4.9,4.3],"Scala":[4.4,3.6],"Groovy":[4.3,3.3],"Perl":[4.2,4.3]}


datalc= dict((k.lower(), v) for k, v in data.items()) 
#coverting data keys(words) to lowercase
kv= datalc.items()
#seperating keys(words) from values
pl= 25/100
#perfect length for big and small devices. *if you want statistic lines to be longer, change the first number to a higher number
years= [2018,2017]

ly= len(years)
#years count
ui= input()
#user input
uic= len(ui)
#user input count
uilc= ui.lower()
#converting user input to lowercase
ndl=[]
#no data list. words that aren't added to the database will be inserted to this list and then printed as """no data for (the words inside this list)"""


def data_processing(word):

    yc= 0
    #years count by order ex: year 1 ,year 2 etc.
    if word in datalc:
    #checking if the word exist in the database
        print (word.capitalize()+":")
        #printing the word with (:) after it
        for year in years:
        #this process will be executed for each year    
            v= datalc[word]
            #the value of the word
            vby= v[yc]
            #value according to the year
            usl= round(pl*vby)
            #underscore length which is based on multiplying the perfect length with the value of the year being proceeded
            yc+= 1
            #adding value to the year order variable(yc) so next time this loop being executed it will read the value of the next year by using the vby(value by year) variable
            vby= str(vby)   
            year= str(year)
            #converting int variables to str so they can be added to other strings in print brackets
                     
            print(year+"|",end="")
            #printing the year followed by (|) and making sure not to print a line break
            print("_"*usl,end="")
            #printing underscores multiplyed by the underscore length and making sure not to print a line break
            print(vby+"%")
            #printing the value according to year followed by (%)
            if yc == ly:
            #checking if year count (yc) is equal to the total count of years (ly) to print a line break for the next word statistics
                print("\n")
                
                
    else:
        ndl.append(word.capitalize())
        #adding unfound words in the database to the no data list(ndl)        
        
if uilc == "all":
    
    print("Most Popular Technologies in 2018 and 2017 According to Stack OverFlow Statistics:\n")
    
    for k,v in kv:            
    #processing all keys(words) in the data base through our function
        data_processing(k)
        
elif uic >= 1:

    uil= uilc.split()
    #placing words seperated by space into a list
    for word in uil:
    #processing words in the user input list(uil) through our function   
        data_processing(word)
    
    ndlc= len(ndl)
    if ndlc >= 1:
        print ("no data found for ({})...".format(", ".join(ndl)))
    #printing unfound words if any
             
else:
    
    print("no input.\nTo show all statistics type all.\n\nTo show specific statistics, type the word you want to show statistics of.\n\nSeperate words with space if there are more than one word\n\nex:python java etc.")
    
    
print ("\nupvote(^) if you like this code :)")    

