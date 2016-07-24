import re
import urllib

def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  # uf = urllib.urlopen('http://google.com')
  #urllib.urlretrieve('http://google.com/intl/en_ALL/images/logo.gif', 'blah.gif')
  uf = urllib.urlopen(filename)
  textuf = uf.read()
  lst  =  re.findall('GET (\S+.jpg)',str(textuf))
  lst2 =  list(set(lst))
  lst2.sort()
  print len(lst2)
  print lst2[2]
  return lst2


print read_urls('animal_code.google.com')

