
import emoji

def emojize_text(text):
    return emoji.emojize(text, language='alias')

def main():
    Input = input("Input: ")
    emoji = emojize_text(Input)
    print(f"Output: {emoji}")

if __name__ == "__main__":
    main()
