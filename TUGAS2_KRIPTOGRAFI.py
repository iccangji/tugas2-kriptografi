print("MUH. NUR IKSAN")
print("E1E120036")
print("KRIPTOGRAFI ALGORITMA RC4")

s = []
for i in range(256):
    s.append(i)

k = 'saputra1'

j = 0
for i in range(len(s)):
     j = (j + s[i] + ord(k[i % len(k)])) % len(s)
     s[i], s[j] = s[j], s[i]

print(s)
P = '2036'
C = []
i=0
j=0
for idx in range(len(P)):
   i = (i + 1)  % len(s)
   j = (j + s[i]) % len(s)
   s[i], s[j] = s[j], s[i]
   t = (s[i] + s[j]) % len(s)
   u = s[t]
   c = u^ord(P[idx])
   C.append(chr(c))
for i in C:
    print(i,end='')