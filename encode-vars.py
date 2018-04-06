import base64
encoded = base64.b64encode(b'Critical error: You are looking cute and working hard - so proud of you.') 

print (encoded)

start = b'Q3JpdGljYWwgZXJyb3I6IFlvdSBhcmUgbG9va2luZyBjdXRlIGFuZCB3b3JraW5nIGhhcmQgLSBzbyBwcm91ZCBvZiB5b3Uu'

decoded = base64.b64decode(encoded).decode('utf-8')


print (decoded)
# raise ValueError(print (base64.decode(error)))

# break
types_of_people = 5 * "2" 
x = r"There are {types_of_people} types of people." 

binary = "binary" 
do_not = "don't" 
y = f"Those who know {binary} and those who {do_not}.".format(binary=do_not, do_not=binary)

print (x)
print (y) 

print (f"I said: {x}") 
print (f"I also said: '{y}'") 

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}" 

print (joke_evaluation.format(not hilarious))

w = f"This is the left side of..." 
e = f"a string with a right side." 

print (w + e) 
