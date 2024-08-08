from search import *
graph={'A':{'B','C'},'B':{'D','E'},'C':{'F','G'},'D':{},'E':{},'F':{},'G':{}}

class Node():
    def __init__(self,state,parent=None,cost=0,heuristic=0):
        self.state=state
        self.parent=parent
        self.cost=cost
        self.heuristic=heuristic
    def __repr__(self):
        return repr(self.state)

def goal_test(state):
    if state==goal:
        return True
    else:
        return False


def sucessors(state):
 return graph[state]

def node_to_path(node):
    path=[node.state]
    while node.parent != None:
        node=node.parent
        path.append(node.state)
    path.reverse()
    #print(path)
    return path


def bfs(initial):
    frontier=Queue()
    inode=Node(initial)
    frontier.push(inode)
    explored={initial}
    while frontier.empty:
        print(frontier)
        print('hello')
        current_node=frontier.pop()
        current_state=current_node.state
        if goal_test(current_state):
            print(node_to_path(current_node))
            return current_node
        for child in sucessors(current_state):
            if child not in explored:
                frontier.push(Node(child,current_node))
                explored.add(child)
    return None

start='A'
goal='D'
bfs(start)