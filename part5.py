# Task 3: Light Show Technician Loop
# Using the range() function, loop through the genres list by index. 
# For each genre, print out the track number and a message that the light show is ready. 
# Modify the loop to skip a genre if it's not suitable for the light show, for instance Classical genre.

# Our playlist of genres

#task 1
# genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
# num = 0 
# for genre in (genres):
#     num+=1
#     print("This song is the best of",genre , ":track #", num)

# genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
# num = 0
# index = 0 

#task2
# while index < len(genres):
#     genre = genres[index]
#     num+=1
#     index += 1
    
#     if genre != "Hip-hop":
#         print("This song is the best of",genre , ":track #", num)
#     else:
#         break

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
num = 0 

for i in range(4):            #task 3
    for genre in genres:
        if genre == "Rock" or genre == "Hip-hop":
            num+=1
            print("This is the to hits of " + (genre) + " the lightshow is ready: track ", (num))