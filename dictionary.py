mark = {
    "het":32,
    "man":64,
    "famale":4   
}
print(mark, type(mark))  
print(mark["het"])# if name is not in the dict it will give error
print(mark.get("het"))# if name is not in the dict it will give None
mark.update({"het":63,"harry":73})
print(mark)