# valid parenthesis 
# implemented using stack operations

def val_par(s,op):
    # n will hold the length of the string
    n = len(s) - 1
    
    # convert string to list to perform stack operations 
    s = list(s) 
    
    # in order to list indexing work we check n must be greater than or equal to zero
    if(n >= 0):
        
        # if the element on top of the stack is ']' or '}' or ')' then PUSH it to `op` stack and POP from the string `s` stack
        # and make a recursive call for the remaining string 
        if(s[n] in [']','}',')']):
            op.append(s[n])
            s.pop()
            val_par(s,op)   # recursive call
        
        # if the element in top of the string `s` stack is not then check length of the string; it should be greater than zero
        elif(len(s) > 0):
            # if string `s` stack is opening parenthesis; it checks if output `op` stack is not empty and top element in `op` 
            # stack is respective closing parenthesis 
            # if yes then : remove top element from `op` and `s` string stack and make a recusive call the val_par for the 
            # remaining string
            
            # for opening parenthesis '{' or '(' or '['
            if(s[n] == '['):
                if(len(op)>0):
                    if(op[len(op) - 1] == ']'):
                        op.pop()   
                        s.pop()
                        val_par(s,op)   # recursive call
                else:
                    op.append(s[n])
            elif(s[n] == '('):
                if(len(op)>0):
                    if(op[len(op) - 1] == ')'):
                        op.pop()
                        s.pop()
                        val_par(s,op)   # recursive call
                else:
                    op.append(s[n])
            elif(s[n] == '{'):
                if(len(op)>0):
                    if(op[len(op) - 1] == '}'):
                        op.pop()
                        s.pop()
                        val_par(s,op) # recursive call
                else:
                    op.append(s[n])
             # opening parenthesis logic ends here 
           
     # To finally return, if the stack is empty, then we have a valid expression and the function returns TRUE.
     # The output stack won't be empty for instances like ((([]}}}})
    if(op == []): return True
    else: return False

val_par('[][{}{}{}{(())}]',[])
