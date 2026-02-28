class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count=0
        #using hash map  to look up fast
        hash_table={}
        for row in grid:
            #sice dictionary key is must be immutable  we needs to convertes to tuple

            row_tuple=tuple(row)
            #checking the  esxistance and counts this  frequicy as values and row as key.
            if row_tuple in hash_table:
                hash_table[row_tuple]+=1 #this increase the frequency by one
            else:
                hash_table[row_tuple]=1 #this is set frequency to 1 if it first appearance

        for i in range(len(grid)):
            column=[]
            #to contractues clumn as tuple
            for j in range(len(grid)):
                 column.append(grid[j][i])
            column_tuple=tuple(column)
            if column_tuple in hash_table:
                count+=hash_table[column_tuple]
        return count     