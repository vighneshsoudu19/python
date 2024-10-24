def vighnesh(t):
    if(t>0):
      result=t+vighnesh(t-1)
      print(result)
    else:
       result=0
    return result
print("/n /n recursion eaxmple result")
vighnesh(12)