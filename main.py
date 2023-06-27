from caesar_art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
end_program = False
while not end_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    def caesar(text, shift, direction):
        shift = shift % 26
        caesar_text = ""
        for ch in text:
            if ch not in alphabet:
                caesar_text+=ch
                continue
            pos = alphabet.index(ch)
            if direction == "encode":
                new_pos = (pos + shift)%26
            else:
                new_pos = (pos - shift + 26)%26
            caesar_text+=alphabet[new_pos]
        print(f"The caesar text is {caesar_text}")
    
    caesar(text, shift, direction)
    rerun = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
    if rerun == "no":
        end_program = True