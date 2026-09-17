import art
print(art.logo)
alphabet="abcdefghijklmnopqrstuvwxyz"
while True:
    direction=input("Type encode for encrypt or decode for decrypt: \n").lower()
    text=input("Type your massage: \n").lower()
    shift=int(input("Type shift number: \n"))

    def caesar(text_massages,shift_amount,encode_or_decode):
        output_text= ""
        if encode_or_decode=="decode":
            shift_amount*= -1
        for letter in text_massages:
             shifted_position=alphabet.index(letter) + shift_amount
             shifted_position%=len(alphabet)
             output_text+=alphabet[shifted_position]
        print(f"Here is the {encode_or_decode}d result:{output_text}")
    caesar(text_massages=text,shift_amount=shift,encode_or_decode=direction)
    again=input("Do want to use the caesar again ? type yes or no: ").lower()   
    if again=="no":
        print("Goodbye!")
        break  


                
             
               
    
    