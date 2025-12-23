name = input("Please enter your name : ")
age = int(input("Please enter your age : "))
while age <= 0:
        age = int(input("Please enter a valid age : "))
answer = "y"
numlist =
while answer == "y":
    FavNum = int(input("Please enter your favorite number : "))
    answer = input("Would you like to add another favorite number (Y/N) : ").lower()
    numlist = [numlist,FavNum]
    print(numlist)
profile = {"Name":name,"Age":age, "FavoriteNumber":numlist}
def isodd(num):
      if num % 2 == 0:
            return("even")
      else:
            return("odd")
print(f"Hello {profile['Name']}!\nYour age is an {isodd(profile["Age"])} number!\nFavorite Numbers Summary : \nSmallest: {min(numlist)}\nLargest: {max(numlist)}\nSum : {sum(numlist)}")