def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
        num_words = countWords(file_contents)
        print(" -- Begin report of " + path + " -- ")
        print(f"{num_words} words were found in the document\n")
        chars = countChars(file_contents)
        char_list = []
        for c in chars:
            char_list.append({"name":c,"count":chars[c]})
        char_list.sort(reverse=True,key=sort_on)
        for ch in char_list:
            letter = ch["name"]
            count = ch["count"]
            print(f"The '{letter}' character was found {count} times")

        print(" -- End Report -- ")



def sort_on(dict):
    return dict["count"]

def countWords(book):
    words = book.split()
    return len(words)

def countChars(book):
    book = book.lower()
    counts = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
    # for c in book:
    #     if(c.isalpha):
    #         counts[c]+=1
    for x in counts:
        counts[x] = book.count(x)
    return counts

main()