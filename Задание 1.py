side_a = int(input())
side_b = int(input())
side_c = int(input())

# Учитывается, что все значения введены правильно (проверку не делал специально) 

if (side_a + side_b) > side_c and (side_b + side_c) > side_a and (side_a + side_c) > side_b:
    if (side_a == side_b) and (side_b == side_c):
        print("Exists. Equilateral")
    elif ((side_a == side_b) and (side_b != side_c)) or ((side_a == side_c) and (side_c != side_b)) or ((side_b == side_c) and (side_c != side_a)):
        if ((side_a)**2 + (side_b)**2 == (side_c)**2) or ((side_a)**2 + (side_c)**2 == (side_b)**2) or ((side_b)**2 + (side_c)**2 == (side_a)**2):
            print ("Exists. Isosceles and Rectangular")
        else:
            print ("Exists. Isosceles")
    elif (side_a != side_b) and (side_b != side_a) and (side_a != side_c):
        if ((side_a)**2 + (side_b)**2 == (side_c)**2) or ((side_a)**2 + (side_c)**2 == (side_b)**2) or ((side_b)**2 + (side_c)**2 == (side_a)**2):
            print ("Exists. Rectangular")
        else:
            print ("Exists. Common case")
else:
    print ("Doesn't exist")
