#list
formula1 = ["Suzuka", 10, True, 20.30, ["Lewis Hamilton", 2, 2.50]]
print(formula1)
formula1 = ["Suzuka", 10, True, 20.30, ["Lewis Hamilton", 2, 2.50]]
print(formula1[3])
sirkuit = ["Suzuka", "Monza", "Silverstone", "Marina Bay"]
print(sirkuit)
sirkuit.append("Spa-Francorchamps")
print(sirkuit)
sirkuit = ["Suzuka", "Monza", "Silverstone", "Marina Bay"]
print(sirkuit)
sirkuit[1] = "Monza Italia"
print(sirkuit)
sirkuit = ["Suzuka", "Monza", "Silverstone", "Marina Bay"]
print(sirkuit)

#tuple
chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
print(chara[2])
print(chara[-1])
print(chara[4][0])
chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
listchara = list(chara)
listchara.append("Yui ")
chara = tuple(listchara)
print(chara)