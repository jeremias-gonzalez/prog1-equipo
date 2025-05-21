data2018=["Liam,19837,M","Noah,18267,M","Michael,14516,M","James,13525,M",
          "Oliver,13389,M","Emma,18688,F","Olivia,17921,F","Ava,14924,F","Isabella,14464,F","Sophia,13928,F"]

nacidos2008="Eva,17039,M,Daniel,19005,M,Emily,17434,M,Emma,18813,M,Ethan,20216,M,Julia,18616,F,Jacob,22594,M,Joshua,19205,M,Michael,20626,M,Olivia,17081,F"
nacidos2008Lista=nacidos2008.split(",")
listaData2008=[]

for i in nacidos2008Lista:
   nacidos2008Lista = i.split(",")
   listaData2008.append(nacidos2008Lista)

print(listaData2008)