# printam in consola un mesaj
print ('Hello World!')

# comentariu shortcut ctrl+/
# ctrl D copiaza
# ctrl Z undo


numere = [-5, 7, 2, 9, 3, 1, -6]
for a in range(len(numere)):
    for b in range(a + 1, len(numere)):
        if(numere[a] > numere[b]):
            temporar_C = numere[a]
            numere[a] = numere[b]
            numere[b] = temporar_C
print(f" Ordinea este urmatoarea {numere}")

alte_numere = [7, -4, 3, 9, -6]
i = 1
for n in alte_numere:
    if n > alte_numere[i]:
        interim = alte_numere[i-1]
        alte_numere[i-1] = alte_numere[i]
        alte_numere[i] = interim
    i += 1
print(alte_numere)

