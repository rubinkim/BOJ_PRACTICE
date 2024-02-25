#-*- coding: utf-8 -*-

"""
5
0 1 1 3 2

4 2 5 3 1
"""
# 클래스와 함수 선언 부분
class Node():
    def __init__(self):
        self.data = None
        self.link = None
        
def printNodes(start):
    global dataArray
    dataArray = []
    current = start
    if current == None:
        return
    #print(current.data, end=' ')
    dataArray.append(current.data)
    while current.link != None:
        current = current.link
        #print(current.data, end=' ')
        dataArray.append(current.data)
    return dataArray
        
# 노드삽입(findData앞에 insertData를 삽입한다.)
def insertNode(findData, insertData):
    global memory, head, current, pre
    if head.data == findData:   # 첫번째 위치에 데이터삽입
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return
    
    current = head
    while current.link != None: # 중간 위치에 데이터삽입
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return
    node = Node()            # 마지막 위치에 데이터삽입
    node.data = insertData
    current.link = node
        
# 노드삭제
def deleteNode(deleteData):
    global memory, head, current, pre
    if head.data == deleteData:  # 첫번째 위치에 데이터삭제
        current = head
        head = head.link
        del(current)
        return
    
    current = head               # 첫번째외의 위치에 데이터삭제
    while current.link != None:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return 
        
if __name__ == "__main()":       
    N = int(input())
    picked = list(map(int, input().split()))
    dataArray = [x for x in range(1, N+1)]


    memory = []
    head, current, pre = None, None, None 

    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    for i, p in enumerate(picked):  
        
        move = i - p
        finding_data = dataArray[move]
        insert_data = dataArray[i]
        
        if i != move:
            deleteNode(insert_data)
            insertNode(finding_data, insert_data)
        #print(f"head_data : {head.data},  i : {i},  p : {p},  move : {move},  finding_data : {finding_data},  insert_data : {insert_data}",  end=',    ')    
        printNodes(head)
        
    print(*printNodes(head))