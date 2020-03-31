def big_frame(word_list):
    m = 0
    for i in word_list:
        if len(i) > m:
            m = len(i)
    print("+"*(m+2))
    for i in range(len(word_list)):
        print("+",word_list[i]," "*(m-len(word_list[i])),"+", sep = "")
    print("+"*(m+2))
    
big_frame(["Wellcome", "to", "Brno"])
