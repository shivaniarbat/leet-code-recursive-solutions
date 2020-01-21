# valid parenthesis 
# implemented using stack operations

def val_par(s,op):
    n = len(s) - 1
    s = list(s)
    if(n >= 0):
        if(s[n] in [']','}',')']):
            op.append(s[n])
            s.pop()
            val_par(s,op)
        elif(len(s) > 0):
            if(s[n] == '['):
                if(len(op)>0):
                    if(op[len(op) - 1] == ']'):
                        op.pop()
                        s.pop()
                        val_par(s,op)
                else:
                    op.append(s[n])
            elif(s[n] == '('):
                if(len(op)>0):
                    if(op[len(op) - 1] == ')'):
                        op.pop()
                        s.pop()
                        val_par(s,op)
                else:
                    op.append(s[n])
            elif(s[n] == '{'):
                if(len(op)>0):
                    if(op[len(op) - 1] == '}'):
                        op.pop()
                        s.pop()
                        val_par(s,op)
                else:
                    op.append(s[n])
           
    if(op == []): return True
    else: return False

val_par('[][{}{}{}{(())}]',[])
