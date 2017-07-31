def solved_selection_sort(ls):
    for i in range(len(ls)): #iterates through list of 0 to length of ls - 1
        lowest = i #for now, assume number at index i is the lowest
        for j in range(i + 1, len(ls)): #iterates through list of i to length of ls - 1
            if ls[lowest] > ls[j]: #if the number at index of the lowest is greater than number at index of i
                lowest = j #actually the number at index of i is the lowest
        ls.insert(i, ls.pop(lowest)) #insert the item at index i, pop() returns the item and also deletes it
    return ls #list is sorted by the time loop is done
