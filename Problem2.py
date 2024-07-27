#In this code, I solved the problem of finding the distance of each cell from the nearest zero in a binary matrix by using a breadth-first search (BFS) approach. First, I initialized a distance matrix dist with infinity values and a queue to store the coordinates of all zero cells. I set the distance of zero cells to zero and added them to the queue. Then, I processed each cell in the queue, exploring its neighboring cells in four directions (up, down, left, right). If a neighboring cell's distance was still infinity, it meant it hadn't been processed yet, so I updated its distance to be one more than the current cell's distance and added it to the queue. This ensured that distances were calculated layer by layer from the nearest zeros outwards. The BFS guarantees that each cell is processed in the shortest path order. The time complexity of this approach is O(m×n), where m is the number of rows and n is the number of columns, since each cell is processed once. The space complexity is also O(m×n) due to the storage requirements of the distance matrix and the queue.

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        dist = [[float('inf')] * cols for _ in range(rows)]
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    queue.append((r, c))
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] == float('inf'):
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
        
        return dist