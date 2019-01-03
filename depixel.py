import sys
import os
a = sys.argv
for i in a[1:]:
     os.system("potrace -b svg -b pdf "+i)
