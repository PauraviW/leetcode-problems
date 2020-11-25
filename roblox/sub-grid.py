def largestSubgrid(grid, maxSum):

    n = len(grid)
    sum = [[0]*n for i in range(n)]
    mx=0
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                sum[0][0] = grid[0][0]
            elif i==0:
                sum[0][j]=sum[0][j-1]+grid[0][j]
            elif j==0:

                sum[i][0]=sum[i-1][0]+grid[i][0]
            else:
                sum[i][j]=sum[i-1][j]+sum[i][j-1]+grid[i][j]-sum[i-1][j-1]

            mx=max(mx, grid[i][j])


    ans=0
    l=0
    r=n
    while l<r:
        x = int(l+(r-l+1)/2)
        res=0;
        for i in range(x-1,n):
            for j in range(x-1, n):
                total=sum[i][j]
                if(i>=x):
                    total-=sum[i-x][j]
                if(j>=x):
                    total-=sum[i][j-x]
                if(i>=x and  j>=x):
                    total+=sum[i-x][j-x]

                res=max(res, total);

        if maxSum >= res:
            l=x
        else:
            r=x-1
    return r
grid = [[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]]
maxSum = 14
print(largestSubgrid(grid, maxSum))