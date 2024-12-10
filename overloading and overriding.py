# Overloading

"""
obj=ABC()
obj.Disp()
obj.Disp("kanchan")
obj.Disp('kanchan', 'bhambere')

"OVERLOADING1 same result"
class ABCD:
    def Show(self, firstname='', lastname=''):
        print("Welcome", firstname, lastname ,"!")

obj=ABCD()
obj.Show( )
obj.Show('kanchan')
obj.Show('kanchan', 'bhambere')


def checkTriplet(array):
    n = len(array)
    for i in range(n):
        array[i] = array[i]**2

    array.sort()

    for i in range(n - 1, 1, -1):
        s = set()
        for j in range(i - 1, -1, -1):
            if (array[i] - array[j]) in s:
                return True
            s.add(array[j])
    return False


arr = [3, 2, 4, 6, 5]
a=checkTriplet(arr)
print(a)"""
# True


