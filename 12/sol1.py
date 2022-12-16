import heapq
def main():
    dic = {}
    grid = []
    with open("input.txt","r") as fp:
        lines = fp.read().splitlines()
        grid = [ [] for i in range(len(lines))]
        char = 'a'
        for i in range(1,27):
            dic[chr(ord(char)+(i-1))] = i
        dic['S'] = dic['a']
        dic['E'] = dic['z']
        i = 0
        start = [0,0]
        end = [0,0]
        for x in lines:
            for j in range(len(x)):
                grid[i].append(dic[x[j]])
                if x[j] == 'S':
                    start = (i,j)
                elif x[j] == 'E':
                    end = (i,j)
            i+=1
        for i in grid:
            print(i)
        print('start',start,'end',end)
        distances, prev = dij(grid,start,end)
        #print(distances[end])
        #print(prev[end])
        path = []
        cur = end
        while True:
            if prev[cur] != start:
                path.append(prev[cur])
                cur = prev[cur]
            else:
                path.append(prev[cur])
                break
        print(len(path))
        #print(path)
        #print(grid[start[0]][start[1]],start)
        #print(grid[end[0]][end[1]],end)

def dij(matrix, start, end):
    print(start)
    print(end)
    print('----')
    queue = []
    distances = {}
    prev = {}
    distances[start] = 0
    heapq.heappush(queue, (0, start))
    while queue:
        dist, node = heapq.heappop(queue)
        if node == end:
            return distances, prev
        #print(dist,node)
        row,col = node
        for i, j in [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]:
            if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]):
                if matrix[i][j] - matrix[row][col] <= 1:
                    new_dist = dist + matrix[i][j]
                    if new_dist < distances.get((i,j), float("inf")):
                        distances[(i,j)] = new_dist
                        prev[(i,j)] = node
                        heapq.heappush(queue, (new_dist, (i,j)))
        #print('-',queue)
        
    return distances, prev
 
if __name__=="__main__":
    main()