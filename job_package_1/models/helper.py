# -*- coding: utf-8 -*-

def find_dynamic_tags(s, a, b): 
  
    # initially our result list is empty . 
    res = list()

    # find the length of given strings 
    ls = len(s) 
    la = len(a) 
    lb = len(b)
  
    # currently make array and initially 
    # put zero. 
    x = [0] * ls
    y = [0] * ls 
  
    # find occurrence of "a" and "b" in string "s" 
    for i in range(ls): 
          
        if (s[i: la + i] == a): 
            x[i] = 1
        if (s[i: lb + i] == b): 
            y[i] = 1
  
    # We use a hash to make sure that same  
    # substring is not counted twice. 
    hash = []  
  
    # go through all the positions to find  
    # occurrence of "a" first. 
    curr_substr = "" 
    for i in range(ls): 
      
        # if we found occurrence of "a". 
        if (x[i]): 
          
            # then go through all the positions 
            # to find occurrence of "b". 
            for j in range( i, ls): 
              
                # if we do found "b" at index 
                # j then add it to already 
                # existed substring. 
                if (not y[j]): 
                    curr_substr += s[j] 
  
                # if we found occurrence of "b". 
                if (y[j]): 
                  
                    # now add string "b" to  
                    # already existed substing. 
                  
                    curr_substr += s[j: lb + j] 
                      
                    # If current substring is not 
                    # included already. 
                    if curr_substr not in hash: 
                        if curr_substr.count(a) == 1:
                            res.append(curr_substr)
  
                    # put any non negative integer  
                    # to make this string as already  
                    # existed. 
                    hash.append(curr_substr) 
  
            # make substring null. 
            curr_substr = "" 
  
    # return result. 
    return res 
