a=input("Enter Your Name")
print(f"Good Aftyernoon {a}")

a='''
    Dear<|Name|>,
    You Are Selected!
    <|Date|>
    '''
print(a.replace("<|Name|>","Aarav").replace("<|Date|>","24 September 2050") )


b=("Aarav  Good Very Good!")

print(b.find("  "))

print(b.replace("  "," ")) #Strings Are Imutable That Means We CAnnot Change Them By Using Commands

c="Dear Aarav,\n This \"Python\" Course IS Best By,\n \"Code With Harry\" Programming Youtube Channel \nEveryone Can Visit And Follow It For Free."

print(c)