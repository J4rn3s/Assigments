scores = [ ]
result_f = open("results.txt")
for line in result_f:
	(name, score) = line.split()
	scores.append(float(score))
result_f.close()
print("The top scores were:")
print(score[0])
print(score[1])
print(score[2])