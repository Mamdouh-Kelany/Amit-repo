
def duplicate_encode(word):

    word = word.lower()
    txt = ""
    dict = {}
    
    for i in word:
        dict[i] = dict.get(i,0) + 1
    for i in word:
        if dict[i] > 1 :
            txt += "("
        else:
            txt += ")"
            
    print(txt)
        
duplicate_encode("din")    
duplicate_encode("recede")
duplicate_encode("Success")
duplicate_encode("(( @")

'''     test.assert_equals(duplicate_encode("din"),"(((")
        test.assert_equals(duplicate_encode("recede"),"()()()")
        test.assert_equals(duplicate_encode("Success"),")())())","should ignore case")
        test.assert_equals(duplicate_encode("(( @"),"))((")'''