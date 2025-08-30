import numpy as np

x=np.array([1,2,3])
y=np.array([4,5,6])

add = x+y
print ("addition:",add)

sub = x-y
print("subtraction:",sub)

mult = x*y
print("Multiplication:", mult)

div = x/y
print("division:",div)

x = np.array([-1,-2,-3,0,1,2,3])
print(np.absolute(x))



import numpy as np


dtypes = [('name', 'S10'), ('grad_year', int), ('cgpa', float)]


values = [('Hrithik', 2009, 8.5), ('Ajay', 2008, 8.7), 
           ('Pankaj', 2008, 7.9), ('Aakash', 2009, 9.0)]
           

arr = np.array(values, dtype = dtypes)
print ("\nArray sorted by names:\n",
            np.sort(arr, order = 'name'))
            
print ("Array sorted by graduation year and then cgpa:\n",
                np.sort(arr, order = ['grad_year', 'cgpa']))