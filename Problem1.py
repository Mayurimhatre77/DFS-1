#In this code, I implemented the floodFill function to perform a flood fill on a 2D image, starting from a given pixel (sr, sc) and replacing all connected pixels of the same original color with a new color. I used a depth-first search (DFS) approach to explore and fill all connected pixels. First, I determined the dimensions of the image and stored the original color of the starting pixel. I created a set to keep track of visited pixels to avoid reprocessing. The recursive dfs function changes the pixel color and explores the four possible directions (up, down, left, right). The base case for the recursion checks if the pixel is out of bounds, if it’s not of the original color, or if it’s already visited. The recursion continues until all connected pixels are filled. The time complexity of this algorithm is O(n×m), where n is the number of rows and m is the number of columns, as it potentially visits every pixel in the image. The space complexity is also O(n×m) due to the recursive stack and the visited set that could store every pixel in the worst case.

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        origin_cell_color = image[sr][sc]
        visited = set()

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols
                or image[r][c] != origin_cell_color
                or (r, c) in visited):
                return

            image[r][c] = color
            visited.add((r, c))

            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r - 1, c)

        dfs(sr, sc)
        return image