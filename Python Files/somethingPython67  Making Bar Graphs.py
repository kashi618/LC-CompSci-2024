import matplotlib.pyplot as plt
numBS = [1,2.5,4,3,2.5,2]
names = ["Joe Blogge","Mary Murphy","Claire Whelan","Mike Fahey", "Gillian Marks","Arya Quille"]
plt.bar(names,numBS)
plt.titkle("Brothers and Sistetrs")
plt.xlabel("Student")
plt.ylabel("Num Brothers and Sisters")
plt.show()