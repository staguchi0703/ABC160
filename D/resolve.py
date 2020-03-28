def resolve():
    '''
    code here
    '''
    N, X, Y = [int(item) for item in input().split()]
    G = [[[],[]] for _ in range(N+1)]

    for i in range(1, N+1):
        if i == 1:
            G[i] = [[2], True]
        elif i == N:
            G[i] = [[N-1], True]
        else:
            G[i] = [[i-1, i+1], True]

    G[X][0].append(Y)
    G[Y][0].append(X)

    # def dfs(node, depth, depth_limit, cnt):
    #     if depth == depth_limit:
    #         cnt = 1
    #         return 1
    #     # print(node)
    #     G[node][1] = False
    #     next_nodes = G[node][0]
    #     for next_node in next_nodes:
    #         if G[next_node][1]:
    #             dfs(next_node, depth+1, depth_limit, cnt)

    for k in range(1, N):
        cnt = 0
        for j in range(1, N+1):
            depth = 0
            stack = [j]
            is_flag = True
            while is_flag:
                if depth == k:
                    is_flag = False
                    cnt += 1
                node = stack.pop()
                G[node][1] = False
                next_nodes = G[j][0]
                for next_node in next_nodes:
                    if G[next_node][1]:
                        stack += next_nodes
                        depth += 1

                if len(stack) <= 0:
                    is_flag = False

            print(cnt)
            



if __name__ == "__main__":
    resolve()
