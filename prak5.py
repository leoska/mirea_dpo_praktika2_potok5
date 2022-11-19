g = [
    # 1, 2,  3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14
     [1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [-1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, -1, -1, 1, 0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, -1, -1, 1, 0, 1, 0, 0, 0, 0],
     [0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, -1, -1],
     [0, 0, 0, 0, 0, 0, 0, 0, -1, -1, 1, -1, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, -1, 1, 0, 0, 0, 0, 0]
]


def trans_matrix(graph):
     res = []
     for v in g:
          prev_res = []
          for k in v:
               prev_res.append(-k)
          res.append(prev_res)
     return res


def ver(cur, graph):
     res = []
     for i in range(len(graph)):
          if i != cur:
               for j in range(len(graph[i])):
                    if graph[cur][j] == 1 and graph[i][j] != 0 and graph[i][j] == - graph[cur][j]:
                         res.append(i)
     return res


def dfs_1(cur, order, used, graph):
     used[cur] = True
     for v in ver(cur, graph):
          if not used[v]:
               dfs_1(v, order, used, graph)
     order.append(cur)


def dfs_2(cur, component, used, t):
     used[cur] = True
     component.append(cur)
     for v in ver(cur, t):
          if not used[v]:
               dfs_2(v, component, used, t)


order = []
component = []
used = [False] * len(g)
for i in range(len(g)):
     if not used[i]:
          dfs_1(i, order, used, g)
used = [False] * len(g)
transpos = trans_matrix(g)
for i in range(len(g)):
     v = order[len(transpos) - i - 1]
     if not used[v]:
          m = ["a", 'b', 'c', 'd', 'e', 'f', 'g', 'h']
          dfs_2(v, component, used, transpos)
          a = ''
          for item in component:
               a += m[item] + " "
          print(a)
          component = []
