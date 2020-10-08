# type your code here
import re
def create_account(user_name, password, secret_word):
    if len(password) >= 6 and re.findall("[A-Z]", password) and re.findall("[a-z]", password) and \
        re.findall("[0-9]", password) and re.findall("[!@#$%^&*()_+]", password):
        def check(p_word, s_words):
            if p_word != password:
                return False
            temp_lst = []
            for item in s_words:
                if item in secret_word:
                    if secret_word.count(item) > 1 and item in temp_lst:
                        j = 0
                        x = temp_lst.count(item)
                        while j < x:
                            print("Item: %s" %item)
                            temp_lst.append(item)
                            j += 1
                    else:
                        if item not in temp_lst:
                            temp_lst.append(item)
            print(temp_lst)
            if len(temp_lst) == len(secret_word) or len(temp_lst) == len(secret_word) - 1 and len(s_words) == len(secret_word):
                return True
            else: 
                return False
    else:
        raise ValueError

    return check

initial_arr = ["1", "2", "1"]
tom = create_account("123", "qQ1!45", initial_arr)  
##check1 = tom("Qwerty1_",  ["1", "word"]) 
##check2 = tom("Qwerty1_",  ["word"]) 
##check3 = tom("Qwerty1_",  ["word", "2"])
##print(check3)
##check4 = tom("Qwerty1!",  ["word", "12"]) 


checked_arr_2_true = ["1", "1", "2"]
a = tom("qQ1!45", checked_arr_2_true) 
#print(a)


checked_arr_9_false = ["1", "2"]
a = tom("qQ1!45", checked_arr_9_false)

