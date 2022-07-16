string=input()
list_string=list(string)
list_string.sort(reverse=True)
result=''.join(s for s in list_string)
print(result)
    
