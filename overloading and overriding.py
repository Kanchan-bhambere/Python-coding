# Overloading

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