x = float(2.7)  # x should be 2.7 as a float
y = 2           # y should be 2 as an integer
c = float(x + y)  # x + y = 4.7, and it's converted to a float again (which is redundant but fine)
print(c)         # Should print 4.7
