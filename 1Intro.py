# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Write your code below: 
def degC(F):
  return (F-32)*5/9

def degF(C):
  return C*9/5+32

F100_C = degF(100)
C0_F = degC(0)

def F(M,A):
  return M*A

train_force = F(train_mass,train_acceleration)

print("The GE train supplies "+str(train_force)+" Newtons of force.")

def E(M,C=3*10**8):
  return M*C**2

bomb_energy = E(bomb_mass)

print("A 1kg bomb supplies "+str(bomb_energy)+" Joules.")

def W(M,A,D):
  return F(M,A)*D

train_work = W(train_mass, train_acceleration, train_distance)

print("The GE train does "+str(train_work)+" Joules of work over "+str(train_distance)+" meters.")