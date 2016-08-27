#!/usr/bin/env python
# Author:rogue
import difflib
text1 = """text1:
XXXXX
1234
1234
123
"""

test1_lines = text1.splitlines()
text2 = """text2:
XXX
123
123
"""

text2_lines = text2.splitlines()

d = difflib.Differ()

diff = d.compare(test1_lines, text2_lines)

print("\n".join(list(diff)))