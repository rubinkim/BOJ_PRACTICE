#-*- coding: utf-8 -*-

"""
5
0 1 1 3 2

4 2 5 3 1
"""
import sys
input = sys.stdin.readline

N = int(input())
dataArray = [x for x in range(1, N+1)]
memory = []
head, current, pre = None, None, None

# 클래스와 함수 선언 부분
class Node():
    def __init__(self):
        self.data = None
        self.link = None
        
    def printNodes(start):
        current = start
        if current == None:
            return
        print(current.data, end=' ')
        while current.link != None:
            current = current.link
            print(current.data, end=' ')
        print()
        
    # 노드삽입(findData앞에 insertData를 삽입한다.)
    def insertData(findData, insertData):
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
            
