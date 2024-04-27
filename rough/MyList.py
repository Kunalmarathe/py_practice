#Heterogenous 
#Mutabel
#allow duplicates
#indexed
#ordered

def main():
    Arr = ["Kunal", 24, "Hello", "Marvellous", 23.4, True]

    print(Arr[3])

    Arr[4] = "Marathe"
    print(Arr)

    Arr.append("bhai")
    print(Arr)

    Arr.remove(True)
    print(Arr)

    Arr2 = ["Book", "NoteBook","Hello", "Kunal"]
    Arr.extend(Arr2)
    print(Arr)    

    Arr.pop(0)
    print(Arr)

    print(Arr.count("Kunal"))
    print(Arr.count("Hello"))

    Arr3 = Arr.copy()
    print(Arr3)

if __name__ == "__main__":
    main()