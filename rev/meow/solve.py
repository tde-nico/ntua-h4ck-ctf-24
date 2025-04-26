def xor(a, b):
	return [x ^ b for x in a]

def xorl(a, b):
	return [x ^ y for x, y in zip(a, b)]

vals = [46096, 29310, 35786, 34250, 1682, 11703, 61757, 3732, 9259, 35900, 51157, 33143, 711, 15574, 10828, 33537, 40680, 50187, 18386, 31483]
finals = [13660, 20137, 19784, 1306, 978, 10684, 36366, 1167, 6038, 4071, 28503, 2856, 363, 1268, 7100, 9711, 21216, 17029, 17033, 25654]

k1 = 0x1337
k2 = 0xdead

flag = ''

for j in range(25):
	for i in range(256):
		print(flag + chr(i))
		tmp = (((i ^ k1) * k2) >> 4) % vals[j]
		if tmp == finals[j]:
			flag += chr(i)
			break
		#print(i, tmp, finals[j])
	

print(flag)

# NH4CK{r3v3r51n_m1p5}
