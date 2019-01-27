is_male = False
is_tall = False

if is_male and is_tall:
    print("you are a male or tall or both")

#if is_male and is_tall:
#   print("you are a male or tall or both")

elif is_male and  not(is_tall):
    print("you are a short male")

elif not(is_male) and  is_tall:
    print("you are not a male but tall")

#    print("you are a male or tall or both")

else:
    print("you are not a male or tall")
