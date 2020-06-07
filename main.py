import iqpgFunction

# Main Function
def main():
    print("-----Intelligent Question Paper Generator By Aanchal and Anchal-----\n")
    # Creating an iqpg object
    iqpg = iqpgFunction.IntelligentQuestionPaperGenerator()

    """inputTextPath = "InputX.txt"
    readFile = open(inputTextPath, 'r+', encoding="utf8")
    inputText = readFile.read()"""

    inputText = input("Enter the input text:  ")

    questionList = iqpg.iqpgParse(inputText)
    iqpg.display(questionList)
   
    return 0

# Calling Main Function
if __name__ == "__main__":
    main()
    input()
