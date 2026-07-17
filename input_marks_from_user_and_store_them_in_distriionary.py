marks={}
phy=int(input("physics:"))
chem=int(input("chemistary:"))
maths=int(input("maths:"))

marks.update({"physics":phy})
marks.update({"chemistary":chem})
marks.update({"maths":maths})
print(marks)
