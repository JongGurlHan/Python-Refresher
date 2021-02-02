l = ["Bob", "Rolf", "Anne"] #순서있음, 수정가능
t = ("Bob", "Rolf", "Anne") #순서있음, 수정불가능
s = {"Bob", "Rolf", "Anne"} #순서없음, 수정가능

s.add("Smith")
print(s) 