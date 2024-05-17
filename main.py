def v_c_finder(word:str):
    vowel:list = ['a','e','i','o','u'] 
    count:int = 0
    for letter in word:
        if letter in vowel:
        # if letter not in vowel:
            count +=1
    print(f"Total vowels in {word} is {count}")
    # print(f"Total consonants in {word} is {count}")

v_c_finder('Bangladesh')

