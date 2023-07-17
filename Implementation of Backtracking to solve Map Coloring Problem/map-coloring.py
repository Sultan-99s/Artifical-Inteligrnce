
def is_safe(graoh, colour, v):
    for i in range(v):
        for j in range(i+1, v):
            if graoh[i][j] and colour[j] == colour[i]:
                return False
    return True

def colour_graph(graph, c, colour, n, v):
    if n == v:
        if is_safe(graph, colour, v):
            return True
        return False

    for i in range(1, c+1):
        colour[n] = i

        if colour_graph(graph, c, colour, n+1, v):
            return True
        colour[n] = 0
    return False


def add_edge(graph, e1, e2):
    graph[e1][e2] = 1
    if e1 != e2:
        graph[e2][e1] = 1


# %%
v, e = input().split()

graph = [[0 for i in range(int(v))] for j in range(int(v))]
# 7 print(graph)

for i in range(int(e)):
    e1, e2 = input().split()
    add_edge(graph, int(e1) - 1, int(e2) - 1)

'''
c = int(input())
colour = []
for i in range(c):
    colour.append(i+1)

print(colour)'''

c = int(input())
colour = [0] * int(v)

if colour_graph(graph, c, colour, 0, int(v)):
    for i in range(len(colour)):
        print(colour[i])
    #print(colour)


else:
    print("NO")

# print(colour)
