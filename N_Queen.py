#!/usr/bin/env python
# coding: utf-8

# In[1]:


def is_safe(board, row, col):

    # Check if there is a queen in the same row
    
    # 1 0 1
    # 0 0 0
    # 0 0 0

    for c in range(col):
        if(board[row][c]==1):
            
            return False
    
    # Check if there is a queen in the upper left diagonal
    # reduce both rows and column as u go up
    # 1 0 0
    # 0 0 0
    # 0 0 1
       
    r , c = row , col
    while r>=0 and c>=0:
        if board[r][c]==1:
            
            return False
        r -= 1 
        c -= 1
        
    # Check if there is a queen in the lower left diagonal
    # reduce columns and increment rows as u go down
    # 0 0 1
    # 0 0 0
    # 1 0 0
    
    while r<4 and c>=0:
        if board[r][c]==1:
           
            return False
        r +=1 
        c -=1
    
    return True


def solve_n_queens():
    # create a 4*4 board
    board=[[0 for _ in range(4)]for _ in range(4)]
    
    # check if solution exists or not
    if not solve_util(board,0):
        print('problem cannot be solved')
    else:
        print_board(board)



def solve_util(board, col):
    #check if we have reached last column
    
    # 0 1 0 0
    # 0 0 0 1
    # 1 0 0 0 
    # 0 0 1 0 <- when it reaches here it will terminate

    if col>=4:
        return True
    
    # else find ideal positon of next queen for next column
    # intially
    
    # 0 0 0 0
    # 0 0 0 0
    # 0 0 0 0
    # 0 0 0 0
    
    # in first iteration
    
    for row in range(4):
        if is_safe(board,row,col):
           
            board[row][col]=1
            
            if solve_util(board,col+1):
                return True
            
            board[row][col]=0
    
    return False



def print_board(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))
        




# In[2]:


solve_n_queens()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




