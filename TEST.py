import sys
A=sys.stdin.readlines()
print ''.join(A[:A.index('42\n')])