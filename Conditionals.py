userReply = input("Do you need to ship a package?  (Enter yes or no) ")

if userReply == "yes":
    print("We can help you ship that package!")
    
else:
    print("Please come back when you need to ship a package. Thank you.")   
  
    
userReply = input("Which stationery would you like to buy? (Enter stamps, envelope, or copy): ")

# Respond based on input
if userReply.lower() == "stamps":
    print("You chose to buy stamps.")
elif userReply.lower() == "envelope":
    print("You chose to buy an envelope.")
elif userReply.lower() == "copy":
    print("You chose to make a copy.")
else:
    print("Invalid choice. Please enter stamps, envelope, or copy.")   

    