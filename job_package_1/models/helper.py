# -*- coding: utf-8 -*-

def find_dynamic_tags(string, start, end): 
  
    # initially our result list is empty . 
    result = list()

    # find the length of given strings 
    string_length = len(string) 
    start_length = len(start) 
    end_length = len(end)
  
    # currently make array and initially 
    # put zero. 
    list_x = [0] * string_length
    list_y = [0] * string_length 
  
    # find occurrence of "a" and "b" in string "s" 
    for i in range(string_length): 
          
        if (string[i: start_length + i] == start): 
            list_x[i] = 1
        if (string[i: end_length + i] == end): 
            list_y[i] = 1
  
    # We use a non_duplicate_strings to make sure that same  
    # substring is not counted twice. 
    non_duplicate_strings = list()
  
    # go through all the positions to find  
    # occurrence of "a" first. 
    curr_substr = "" 
    for i in range(string_length): 
      
        # if we found occurrence of "a". 
        if (list_x[i]): 
          
            # then go through all the positions 
            # to find occurrence of "b". 
            for j in range( i, string_length): 
              
                # if we do found "b" at index 
                # j then add it to already 
                # existed substring. 
                if (not list_y[j]): 
                    curr_substr += string[j] 
  
                # if we found occurrence of "b". 
                if (list_y[j]): 
                  
                    # now add string "b" to  
                    # already existed substing. 
                  
                    curr_substr += string[j: end_length + j] 
                      
                    # If current substring is not 
                    # included already. 
                    if curr_substr not in non_duplicate_strings: 
                        if curr_substr.count(start) == 1:
                            result.append(curr_substr)
  
                    # put any non negative integer  
                    # to make this string as already  
                    # existed. 
                    non_duplicate_strings.append(curr_substr) 
  
            # make substring null.
            curr_substr = "" 
  
    # return result. 
    return result
