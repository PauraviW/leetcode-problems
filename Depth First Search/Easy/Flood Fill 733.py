class Solution:
    def floodFill(self, image: [[]], sr: int, sc: int, newColor: int) -> [[]]:
        stack = [(sr,sc)]
        old_color = image[sr][sc]
        visited = []
        while stack:
            current_row, current_col = stack.pop()
            if image[current_row][current_col] == old_color and (current_row, current_col) not in visited:
                if current_row - 1 >= 0 :
                    stack.append((current_row - 1,current_col))
                if current_col - 1 >= 0:
                    stack.append((current_row,current_col - 1))
                if current_col + 1 < len(image[0]):
                    stack.append((current_row,current_col + 1))
                if current_row + 1 < len(image):
                    stack.append((current_row + 1,current_col))
                image[current_row][current_col] = newColor
                visited.append((current_row, current_col))
        print(image)


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
newColor = 2
print(Solution().floodFill(image, sr, sc, newColor))













