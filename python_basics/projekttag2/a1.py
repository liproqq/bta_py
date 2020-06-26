import pickle as pkl

math = []
physics = []
philosophie = []

f = open('mathematiker.txt', 'r')

for line in f:
    math.append(line.rstrip())

f = open('physiker.txt', 'r')
for line in f:
    physics.append(line.rstrip())

f = open('philosophen.txt', 'r')
for line in f:
    philosophie.append(line.rstrip())

people = open("people.txt","w")
people.write(str(math)+"\n")
people.write(str(physics)+"\n")
people.write(str(philosophie)+"\n")

people_dict = {"math":math,"physics":physics,"philosophie":philosophie}

people_pkl = open("people.pkl","wb")
pkl.dump(people_dict, people_pkl)
people_pkl.close()

people_pkl = open("people.pkl","rb")
data = pkl.load(people_pkl)
people_pkl.close()

print(data["philosophie"])

