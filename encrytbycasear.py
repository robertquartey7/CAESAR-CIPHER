
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
shift =0
word = ""
word_choice =""



def encrpt(w, s):
    new_word =""
    for x in word:
       if x == " ":
            new_word +=x
       else:
            letter_position = alphabet_list.index(x)
            new_letter_p = ((letter_position)+shift)%26
            new_word += alphabet_list[new_letter_p]
        
    print(new_word) 
   




def decrpt(w, s):
    new_word =""
    for x in word:
        if x == " ":
            new_word +=x
        else:
            letter_position = alphabet_list.index(x)
            new_letter_p = ((letter_position)-shift)%26
            new_word += alphabet_list[new_letter_p]
        
    print(new_word) 


while(word != "quit"):
    word_choice = input("Encryt/Decryt: ").lower()
    word = input("Enter your word/words: ").lower()
    shift = int(input("Shift by how many"))

    if word_choice =="encryt":
        encrpt(word,shift)
    elif word_choice == "decryt":
        decrpt(word_choice, shift)
    else:
        print("--error check spelling!!!--")



