def fix_start(s):
  s1 = s.replace(s[0],"*")   
  s2 = s1[1:]
  return s[0]+s2
  
print fix_start("babble"
