import random

max=int(input("Donnez un nombre maximum :\n"))
nbr=random.randint(1, max)
test=0
i=0
while (test!=nbr):
	

	test=int(input("Donnez un nombre entre 1  et votre max :\n"))
	i=i+1
	if (test==nbr):
		print("bravo, vous avez gagne en",i , "coups")

	elif (test<nbr):
		print("plus")

	else:
		print("moins")

