#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
    
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    print filename[0]
    f = open(filename[0],"r+")
    fstring = str(f)
    yearstr = re.search("file 'baby(\w+).html",fstring)
    year = yearstr.group(1)
    raw_list = re.findall("<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>",f.read())
    result = []
    for a in raw_list:
        b = a[1]+' '+a[0]
        c = a[2]+' '+a[0]
        result.append(b)
        result.append(c)
    result.sort()
    result.insert(0,year)
    return result    
  
  
def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  
  

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
'''<<<<<<< Local Changes
<<<<<<< Local Changes
<<<<<<< Local Changes
<<<<<<< Local Changes
<<<<<<< Local Changes
<<<<<<< Local Changes
<<<<<<< Local Changes
<<<<<<< Local Changes
<<<<<<< Local Changes
<<<<<<< Local Changes
<<<<<<< Local Changes
<<<<<<< Local Changes
<<<<<<< Local Changes
  argout = str(arg)+"_summary"
  w = open(argout,"w+")
  w.open(extract_names(args))
 #print extract_names(args)
=======
  arg_out = str(agr)+"_out"
=======
  arg_out = str(args)+"_out"
>>>>>>> External Changes
  print extract_names(args)
<<<<<<< Local Changes
  w = open(arg_out,'w')
  w.write(extract_names(args))
>>>>>>> External Changes
=======
  w = open(arg_out,'w')
  w.write(extract_names(args))
>>>>>>> External Changes
  # For each filename, get the names, then either print the text output
=======
  arg_out = str(args)+"_out"
  #print extract_names(args)
  
  w = open(arg_out,'w')
  out = extract_names(args)
  print out
  w.write(extract_names(args))
  
# For each filename, get the names, then either print the text output
>>>>>>> External Changes
=======
  arg_out = str(args)+"_out"
  #print extract_names(args)
  
  w = open(arg_out,'w')
  out = extract_names(args)
  out2 =  out.splice(",")
  w.write(extract_names(args))
  
# For each filename, get the names, then either print the text output
>>>>>>> External Changes
=======
  arg_out = str(args)+"_out"
  #print extract_names(args)
  
  w = open(arg_out,'w')
  out = extract_names(args)
  out2 =  out.splice(",")
  w.write(extract_names(args))
  
# For each filename, get the names, then either print the text output
>>>>>>> External Changes
=======
  arg_out = str(args)+"_out"
  #print extract_names(args)
  
  w = open(arg_out,'w')
  out = extract_names(args)
  print type(out)
  out2 =  out.splice(",")
  w.write(extract_names(args))
  
# For each filename, get the names, then either print the text output
>>>>>>> External Changes
=======
  arg_out = str(args)+"_out"
  #print extract_names(args)
  
  w = open(arg_out,'w')
  out = extract_names(args)
  print type(out)
  out2 =  out.splice(",")
  w.write(extract_names(args))
  
# For each filename, get the names, then either print the text output
>>>>>>> External Changes
=======
  arg_out = str(args)+"_out"
  #print extract_names(args)
  
  w = open(arg_out,'w')
  out = extract_names(args)
  print type(out)
  out2 =  ','.join(out)
  print out2
  #w.write(extract_names(args))
  
# For each filename, get the names, then either print the text output
>>>>>>> External Changes
=======
  arg_out = str(args)+"_out"
  #print extract_names(args)
  
  w = open(arg_out,'w')
  out = extract_names(args)
  print type(out)
  out2 =  '\n'.join(out)
  print out2
  #w.write(extract_names(args))
  
# For each filename, get the names, then either print the text output
>>>>>>> External Changes
=======
  arg_out = str(args)+"_out"
  #print extract_names(args)
  
  w = open(arg_out,'w')
  out = extract_names(args)
  print type(out)
  out2 =  '\n'.join(out)
  print out2
  w.write(out2)
  
# For each filename, get the names, then either print the text output
>>>>>>> External Changes
=======
  arg_out = str(args)+"_out"
  #print extract_names(args)
  
  w = open(arg_out,'w')
  out = extract_names(args)
  print type(out)
  out2 =  '\n'.join(out)
  print out2
  w.write(out2)
  w.close() 
# For each filename, get the names, then either print the text output
>>>>>>> External Changes
=======
  arg_out = str(args)+"_out"
  #print extract_names(args)
  
  w = open(arg_out,'w')
  out = extract_names(args)
  print type(out)
  out2 =  '\n'.join(out)
  print out2
  w.write(out2)
  w.close() 
# For each filename, get the names, then either print the text output
>>>>>>> External Changes
=======
  arg_out = str(args[0])+"_out"
  #print extract_names(args)
  
  w = open(arg_out,'w')
  out = extract_names(args)
  print type(out)
  out2 =  '\n'.join(out)
  print out2
  w.write(out2)
  w.close() 
# For each filename, get the names, then either print the text output
>>>>>>> External Changes
  # or write it to a summary file
'''  
if __name__ == '__main__':
  main()
