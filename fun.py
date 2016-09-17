def mike():
  for i in range(0,1):
    print("Choose your own adventure")
    print("Dad's trip to work")
    print("-*-*-*-*-*-*-*-*-*-*-*-*")
    print("Lisa gone, Mike could finally start a new adventure.")
    print("Should he?")
    
    response_1 = raw_input("Reply: (Y)es (N)o: ")
    if response_1.lower == "y":
      print("So he set off.")
    else:
      print("Instead of an adventure, he took a nap on the couch.")


mike()