#CWN series
#ITM(module math)

#Program 1
#Πρόγραμμα Εύρεσης τιμής της συνάρτησης F(x)
import math #εισαγωγή  αρθρώματος math 
print('Hello')
name = input('Give me your name: ')
print('Nice',name,',Now')
x = int(input('Give me your number: '))
if x > 0 :
    fx = math.sqrt(x) - 1 / x
else:
    fx = 1- 2*pow(x,3)+math.exp(x)
print (fx)

#Program 2 
#Πρόγραμμα Εύρεσης Ριζών Τριωνύμου
import math
print("Hello")
name = input("Give Me Your Name: ")
print("Nice,",name)
a = int(input("Give me the a: "))
b = int(input("Give me the b: "))
c = int(input("Give me the c: "))
d = pow(b,2)-4*a*c #d =Διακρίνουσα
if d>0:
  r1 = (-b + sqrt(d))/2*a
  r2 = (-b - sqrt(d))/2*a
  print(r1)
  print(r2)
elif d<0:
  print("No roots of an equation")
elif d==0:
  r1 = -b / (2*a)
  print(r1)
  
#Program 1
#Εύρεση τιμής ΚΛΑΔΙΚΗΣ ΣΥΝΑΡΤΙΣΗΣ όπου εαν δωθεί τιμή (x) του μεγαλύτερη απο το 0 οδηγείται στον πρώτο κλάδο της
#ενώ εαν δωθεί τιμή (x)μικρότερη από το 0 θα μεταβεί στο άλλο κλάδο της

#Program 2 
#Γνωρίζουμε ότι για να βρούμε τις λύσεις μιας δευτεροβάθμιας εξίσωσης αρκεί να βρούμε την διακρίνουσα της(ο τύπος της δίνεται στο πρόγραμμα)
#Αν η Δ(Διακρίνουσα) είναι μεγαλύτερη απο το 0 τότε έχει 2 ρίζες(λύσεις)
#Αν η Δ(Διακρίνουσα) είναι μικρότερη απο το 0 τότε  δεν έχει ρίζες(λύσεις) - Είναι Αδύνατη
#Αν η Δ(Διακρίνουσα) είναι ίση απο το 0 τότε έχει 1 ρίζα (λύση)
