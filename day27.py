fileku = open("jurusan.txt","w")
fileku.write('Biologi\n')
fileku.write('PGSD\n')
fileku.write('PTI\n')
fileku.close()

with open("jurusan.txt",'r') as baca :
    print(baca.read()) 
