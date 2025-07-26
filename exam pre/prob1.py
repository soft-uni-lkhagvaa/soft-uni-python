guzeelzgene1kg = float(input())
bananakg = float(input())
jurjkg = float(input())
boorolzgonokg = float(input())
guzeelzgenekg = float(input())

boorolzgono_une = guzeelzgene1kg / 2
jurj_une = 0.6 * boorolzgono_une
banana_une = 0.2 * boorolzgono_une
niitune = bananakg * banana_une + jurj_une * jurjkg + boorolzgonokg * boorolzgono_une + guzeelzgenekg * guzeelzgene1kg
print(f'{niitune:.2f}')