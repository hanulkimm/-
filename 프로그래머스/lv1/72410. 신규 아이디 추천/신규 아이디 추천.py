def solution(new_id):
    #1
    new_id=new_id.lower()
    #2
    for ch in set(new_id):
        if not ch.isalpha() and not ch.isnumeric() and ch not in ['-','_','.']:
            new_id = new_id.replace(ch, '')
    #3
    for i in range(len(new_id),1,-1):
        new_id = new_id.replace("."*i,'.')
    #4
    if new_id and new_id[0]=='.':
        new_id = new_id[1:]
    if new_id and new_id[-1]=='.':
        new_id= new_id[:len(new_id)-1]
    #5
    if not new_id:
        new_id += 'a'
    #6
    if len(new_id)>=16:
        new_id = new_id[:15]
    if new_id[-1]=='.':
        new_id= new_id[:len(new_id)-1]
    #7
    if len(new_id)<=2:
        while len(new_id) < 3:
            new_id += new_id[-1]

    answer = new_id

    return answer