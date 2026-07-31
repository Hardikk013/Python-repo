import random
import string

menu = input("1.Encode\n2.Decode\n3.Exit\n\nEnter Your Choice : ").lower()
characters = string.ascii_letters

match menu:
    case "1" | "encode":
        en_inp = input("Enter Your Messege For Encoding : ")
        text = en_inp.split()

        encoded = []

        for word in text:
            if len(word)>=3 :
                shifted_words = word[1:] + word[0]

                front_random = "".join(random.choices(characters,k=3))
                end_random = "".join(random.choices(characters,k=3))

                final_block = (front_random + shifted_words + end_random)
                encoded.append(final_block)

            else:
                 encoded.append(word[::-1])

        print(" ".join(encoded))


    case "2" | "decode":
        de_inp = input("Enter Your Messege For Decoding : ")
        text1 = de_inp.split()
        decoded = []

        for word1 in text1:
            if len(word1)>=9:
                first_remove = word1[3:]
                second_remove = first_remove[:-3]
                last_st = second_remove[-1] + second_remove[:-1]
                decoded.append(last_st)
            else:
                decoded.append(word1[::-1])

        print(" ".join(decoded))

    case _:
        print("Invalid Choice!!!")