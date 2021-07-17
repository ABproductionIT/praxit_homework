# 1.	Print a box
""""*******************
    * 	     	   *
    * 		       *
    ******************* """
# a.	Using one statement with one stream insertion operator
statment = (("*" * 19) + "\n") + ("*" + " "*13 + "*" "\n") * 2 + (("*" * 19) + "\n")
print(statment, end="")
# b.	Using one statement with four stream insertion operator.
# 1 statement is list
list_st = [("*" * 19), ("*" + " "*13 + "*")]
print(list_st[0])
print(list_st[1])
print(list_st[1])
print(list_st[0])
# c.	Using four statement
print((("*" * 19) + "\n"), ("*" + " "*13 + "*" + "\n"), ("*" + " "*13 + "*" + "\n"), (("*" * 19) + "\n"), sep="")
