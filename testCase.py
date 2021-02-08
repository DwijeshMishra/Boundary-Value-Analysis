def roots_find(a,b,c):
    if a==0:
        print("Not a Quadratic Equation")
        return;
    D = b * b -4 * a *c;
    if D >0:
        print("Real Roots")
    elif D==0:
        print("Equa; Roots")
    else:
        print("Imaginary Roots")

def checkForTestCase(testcase):
    a=b=c=0
    while testcase<=13:
        if(testcase ==1):
            a=0
            b=50
            c=50
            print("Test Case",testcase)
            print(a,b,c)
            roots_find(a,b,c)
            break
        elif(testcase == 2):
            a=1
            b=50
            c=50 
            print("Test Case",testcase)
            print(a,b,c)
            roots_find(a,b,c)

            break

        elif(testcase == 3):
            a=50
            b=50
            c=50
            print("Test Case",testcase)
            print(a,b,c)
            roots_find(a,b,c)
           
            break

        elif(testcase == 4):
            a=99
            b=50
            c=50
            print("Test Case",testcase)
            print(a,b,c)
            roots_find(a,b,c)
            break

        elif(testcase == 5):
            a=100
            b=50
            c=50
            print("Test Case",testcase)
            print(a,b,c)
            roots_find(a,b,c)

            break

        elif(testcase == 6):
            a=50
            b=0
            c=50
            print("Test Case",testcase)
            print(a,b,c)
            roots_find(a,b,c)

            break

        elif(testcase == 7):
            a=50
            b=1
            c=50
            print("Test Case",testcase)
            print(a,b,c)
            roots_find(a,b,c)

            break

        elif(testcase == 8):
            a=50
            b=99
            c=50
            print("Test Case",testcase)
            print(a,b,c)
            roots_find(a,b,c)

            break

        elif(testcase == 9):
            a=50
            b=100
            c=50
            print("Test Case",testcase)
            print(a,b,c)
            roots_find(a,b,c)

            break

        elif(testcase == 10):
            a=50
            b=50
            c=0
            print("Test Case",testcase)
            print(a,b,c)
            roots_find(a,b,c)

            break

        elif(testcase == 11):
            a=50
            b=50
            c=1
            print("Test Case",testcase)
            print(a,b,c)
            roots_find(a,b,c)

            break

        elif(testcase == 12):
            a=50
            b=50
            c=99
            print("Test Case",testcase)
            print(a,b,c)
            roots_find(a,b,c)

            break
        elif(testcase == 13):
            a=50
            b=50
            c=100
            print("Test Case",testcase)
            print(a,b,c)
            roots_find(a,b,c)

            break


if __name__ == '__main__':
    testcase=int(input("Plese provide test number"))
    checkForTestCase(testcase)


     
