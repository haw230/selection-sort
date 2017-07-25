def solved_selection_sort(ls):
    for i in range(len(ls)): #iterates through list of 0 to length of ls - 1
        lowest = i #for now, assume number at index i is the lowest
        for j in range(i, len(ls)): #iterates through list of i to length of ls - 1
            if ls[lowest] > ls[j]: #if the number at index of the lowest is greater than number at index of i
                lowest = j #actually the number at index of i is the lowest
        temp = ls[lowest] #current lowest found, put that in a temporary variable
        del ls[lowest] #delete the lowest
        ls.insert(i, temp) #put it to index i (where we keep track of where to put it)
    return ls #list is sorted by the time loop is done