X,Y=map(float, raw_input().split())
print '%0.2f' %( Y if X%5!=0 or X>Y-0.5 else (Y-X-0.5))