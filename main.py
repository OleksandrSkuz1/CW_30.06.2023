if __name__ == "__main__":
    someArray = [1, "test", True, 1.6, "hey"]
    # get element by index
    print(someArray[4])

    # lenght array
    print(len(someArray))   # kilkist' symvoliv v masyvi

    # last element array
    print(someArray[len(someArray) - 1]) # ostanniy symvol v masyvi

    # add elements to array
    someArray.append("hi!")
    print(someArray)            # dodavannia elementu do masyvu

    # Remove elements
    someArray.pop(1)
    print(someArray)            # vydalennia elementu
    someArray.remove("hey")
    print(someArray)

    # find element in array
    targetElement = someArray.index(1.6)
    print(targetElement)                         # poshuk

    # replace
    targetElementIndex = someArray.index(1.6)
    someArray[targetElementIndex] = "test3"
    print(someArray)                            # zamina elementa po yogo indexu

    # reverse
    someArray.reverse()
    print(someArray)

    # clear array
    someArray.clear()
    print(someArray)

    



