def convert(emoticons):
    emoticons=emoticons.replace(":)","🙂")
    emoticons=emoticons.replace(":(","🙁")
    return emoticons

def main():
    a=input("Enter your emoticon : ")
    emoji=convert(a)
    print(emoji)

if __name__=="__main__":
    main()
