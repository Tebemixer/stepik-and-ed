system = {'global': {'var': []}}
n = int(input())
for n in range(n):
    s = input().split()
    if 'create' in s:
        system[s[1]] = {'parent': s[2], 'var': []}
    if 'add' in s:
        system[s[1]]['var'].append(s[2])
    if 'get' in s:
        while True:
            if s[2] in system[s[1]]['var']:
                print(s[1])
                break
            elif s[1] == 'global':
                print('None')
                break
            else:
                s[1] = system[s[1]]['parent']


