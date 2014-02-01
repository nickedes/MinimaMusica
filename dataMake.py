
def listing(line):
    '''
    Takes the lines of a document and extract music data.
    Takes a list and returns a list.
    '''
    data = []
    count = 0
    for l in line:
        if 'Download' in l or 'Bitrate' in l or 'quality.' in l:
            count += 1
        if(str(count) not in '1346'):
            if('quality' in l):
                data.append('Songs')
                continue
            data.append(l.strip('\n').strip('\t').strip().strip(':'))
    data.append('')
    return data

def actualData(data):
    '''
    Takes music data and arrange in a format.
    takes a list and returns a dictionary.
    '''
    mov = {}
    mov[data[2]] = {}
    for l in range(3, len(data)):
        if 'Year' in data[l]:
            mov[data[2]][data[l]] = data[l+1]
            l += 1
        if 'Cast' in data[l]:
            c = mov[data[2]][data[l]] = []
            l += 1
            while 'Music' not in data[l]:
                c.append(data[l])
                l += 1
        if 'Music' in data[l]:
            mov[data[2]][data[l]] = data[l+1]
        if 'Lyricist' in data[l]:
            mov[data[2]][data[l]] = data[l+1]
        if 'Songs' in data[l]:
            d = mov[data[2]][data[l]] = {}
            l += 1
            while data[l] != '':
                d[data[l]] = data[l+1]
                l += 2
    return mov
