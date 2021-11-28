
### Complexity O(n^2)
def reverse_string(myStr):
    splt_str=myStr.split(' ')
    rev_ls = splt_str[:]
    for i in range(len(splt_str)-1,-1,-1):
        word = splt_str[i]
        word_ls =list(word)
        L = len(word_ls)
        rev_word = list(word_ls)
        for j in range(0,L):
            rev_word[j] = word_ls[L-1-j]
        rev_ls[len(splt_str)-1 - i] = ''.join(rev_word)
    return ' '.join(rev_ls)

#%%
    
### Complexity O(n)
def reverse_str (myStr):
    str_to_list = list(myStr)
    rev_str_ls = str_to_list[:]
    for i in range(0,len(str_to_list)):
        rev_str_ls[i] = str_to_list[len(str_to_list)-1-i]
        #print(i,rev_str_ls[i])
    return ''.join(rev_str_ls)
    