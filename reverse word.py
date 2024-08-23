def rev(s):
    l = s.split(".")
    l.reverse()
    l = ".".join(l)
    return l
    
    
s = "i.like.this.program.very.much"
print(rev(s))