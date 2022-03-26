# maliah ratcliff
# march 26, 2022 
# How to get dressed

# I originally started with a program that would output song recommendations
# however, my MAC wouldnt compile anything today so I coudlnt debug and had to scrap the idea around 3:20 pm 
# Sadly, wasted too much time on the old program to try to make a good new one since i couldnt test if it worked excpet for in my head :/ 

# the program I did make is used to tell someone the order they should get dressed 
# which is very unuseful considering this is not automation and they dont even input their own clothes 

def main(): 
    sortclothes() 

def sortclothes(): 
    clothes = [("t-shirt", ["jacket", "hat"]),("socks", ["shoes"]), 
    ("pants", ["shoes"]), ("jacket", ["scarf"]), ("underpants", ["pants"]),
    ("hat",[]), ("scarf",[]), ("shoes",[])] 
    NewClothes = [] 
    while len(clothes) > 0: 
        for i in clothes: 
            if findNode(clothes, i[0]) == True: 
                NewClothes.append(i[0]) 
                clothes.remove(i)
    print("Get dresed in this order: ", NewClothes)

def findNode(clothes,item): 
    for i in clothes: 
        if item in i[1]: 
            return False 
    return True 

if __name__ == "__main__":
    main()

# my original program was created to generate a list of songs for a user to explore new music 
# this would have helped individuals find new music without having to manually search for similar artists 

# # creating a song to categorize things songs have in common
#     def getSong(song):
#         song.data = None
#         song.u = None 
#         song.k = None 
#         song.songMatrix = None 
#         makeMatrix(data, u, k)

#     # make the matrix to compare songs 
#     def makeMatrix(song, uSong, kSong): 
#         uSongUsers = []
#         for i in range(0, len(kSong)): 
#             songData = song.data[song.data[song.k == kSong[i]]
#             usr = set(songData[song.u].unique())
#             for j in range(0, len(uSong)):
#                 usrj = uSongUsers[j] 
#                 usrIntersect = usr.intersectoin(usrj)
#                 songMatrix[j,i] = float(len(usrIntersect))/float(len/usrunion))
#         return songMatrix

#     # store results based upon song similarity 
#     def topResults(song, user, matrix, kSong, uSong): 
#         # use matrix to get the results 
#         return data

# # run the program (theoretically since it wont work)
# if __name__ == "__main__":
#     print(cvs_song_file)
#     song = input("Please enter a song from the given file: ")
#     data = getSong(song)  
#     tres = topResults(song, user, data, kSong, uSong)
#     print("Song recommendedations:" tres)

