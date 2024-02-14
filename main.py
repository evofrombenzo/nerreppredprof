class Songs:
    streams = 0
    fio = ""
    id_project = 0
    clas = ""
    score = 0

f = open("songs.csv")
songs = []
j = 0
skip = f.readline()

for i in f:
    s = i.split(',')
    if int(s[3][:-1]) == 10:
        songs.append(Songs())
        songs[j].fio = s[1]
        songs[j].score = int(s[4])
        j += 1

for i in range(len(songs)):
    j = 1
    t = songs[i]
    while j > 0 and songs[j-1].score > t.score:
        songs[j] = songs[j-1]
        j -= 1
    songs[j] = t

print("Топ 5 песен:")
print(f'1 место: {songs[0].fio[0]}.{songs[0].fio.split()[0]}')
print(f'2 место: {songs[1].fio[0]}.{songs[1].fio.split()[0]}')
print(f'3 место: {songs[2].fio[0]}.{songs[2].fio.split()[0]}')
print(f'4 место: {songs[3].fio[0]}.{songs[3].fio.split()[0]}')
print(f'5 место: {songs[4].fio[0]}.{songs[4].fio.split()[0]}')