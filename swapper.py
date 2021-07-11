def Swapper():


    filename1 = input("Enter File 1")
    filename2 = input("Enter File 2")

    with open(filename1,'r') as a:
        data_a = a.read()

    with open(filename2,'r') as b:
        data_b = b.read()

    with open(filename1,'w') as c:
        c.write(data_b)
        
    with open(filename2,'w') as d:
        d.write(data_a)



    

Swapper()