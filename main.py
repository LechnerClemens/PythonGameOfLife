import tkinter as tk
import time

rowsandcol = 30
rows, cols = (rowsandcol, rowsandcol)
arr = [[0 for i in range(cols)] for j in range(rows)]
rows1, cols1 = (rowsandcol, rowsandcol)
newarr = [[0 for i in range(cols1)] for j in range(rows1)]

root = tk.Tk()
root.title("GameOfLife")
def clear():
    list = root.grid_slaves()
    for l in list:
        l.destroy()

def click(event):
    #get grid information
    x = event.x_root - frame.winfo_rootx()
    y = event.y_root - frame.winfo_rooty()
    z = frame.grid_location(x, y)
    #write the alive status into 2d array
    for i in range(cols):
        for j in range(rows):
            if i == z[0] and j == z[1]:
                arr[j][i] = 1
    #if the clicked button is a button in the "normal" grid then the color changes to the alive state
    if z[1] != rowsandcol+1:
        new = tk.Button(frame,bg="black")
        new.grid(row=z[1], column=z[0], sticky=tk.N+tk.S+tk.E+tk.W)
        root.update()
    else:
        if True:
            while True:
                    rows1, cols1 = (rowsandcol, rowsandcol)
                    newarr = [[0 for i in range(cols1)] for j in range(rows1)]
                    #iterate through grid and calculate all the neighbors
                    for i in range(cols):
                        for j in range(rows):
                            #new = tk.Button(frame,bg="yellow")
                            #new.grid(row=i, column=j, sticky=tk.N+tk.S+tk.E+tk.W)
                            #root.update()
                            #time.sleep(0.1)
                            state = arr[i][j]
                            #chase for all the cells on the edges
                            #the state on the edges does not change
                            if i==0 or i == cols-1 or j == 0 or j == rows-1:
                                newarr[i][j] = state
                            else:
                                #calculate the sum of all alive neighbors
                                sum = 0
                                sum += arr[i-1][j-1]
                                sum += arr[i][j-1]
                                sum += arr[i-1][j]
                                sum += arr[i+1][j-1]
                                sum += arr[i+1][j]
                                sum += arr[i-1][j+1]
                                sum += arr[i][j+1]
                                sum += arr[i+1][j+1]
                                #if an alive cell has less than two alive neighbors the cell dies
                                if arr[i][j] == 1 and sum < 2:
                                    newarr[i][j] = 0
                                #if an alive cell has two or three alive neighbors the cell stays alive
                                elif arr[i][j] == 1 and (sum == 2 or sum == 3):
                                    newarr[i][j] = 1
                                #if an alive cell has more than three alive neighbors it dies
                                elif arr[i][j] == 1 and sum > 3:
                                    newarr[i][j] = 0
                                #if a dead cell has exactly three alive neighbors it becomes alive
                                elif arr[i][j] == 0 and sum == 3:
                                    newarr[i][j] = 1
                            #this is for viewing the iterations
                            #new = tk.Button(frame,bg="yellow")
                            #new.grid(row=i, column=j, sticky=tk.N+tk.S+tk.E+tk.W)
                            #root.update()
                            #time.sleep(0.5)
                    for i in range(cols1):
                        for j in range(rows1):
                            if newarr[i][j] == 0 and arr[i][j] == 1:
                                new = tk.Button(frame,bg="white")
                                new.grid(row=i, column=j, sticky=tk.N+tk.S+tk.E+tk.W)
                                #btn.config(bg="white").grid(row=i,column = j)
                                arr[i][j] = 0
                                root.update()
                                #time.sleep(0.1)
                            elif newarr[i][j] == 1 and arr[i][j] == 0:
                                new1 = tk.Button(frame,bg="black")
                                new1.grid(row=i, column=j, sticky=tk.N+tk.S+tk.E+tk.W)
                                arr[i][j] = 1
                                root.update()
                                #time.sleep(0.1)
                    time.sleep(0)

root.geometry("800x800")
tk.Grid.rowconfigure(root, 0, weight=1)
tk.Grid.columnconfigure(root, 0, weight=1)

#Create & Configure frame 
frame=tk.Frame(root, height=200, width=200)
frame.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

#Create a 5x10 (rows x columns) grid of buttons inside the frame
for row_index in range(rowsandcol):
    tk.Grid.rowconfigure(frame, row_index, weight=1)
    for col_index in range(rowsandcol):
        tk.Grid.columnconfigure(frame, col_index, weight=1)
        btn = tk.Button(frame, bg="white") #create a button inside frame 
        btn.grid(row=row_index, column=col_index, sticky=tk.N+tk.S+tk.E+tk.W)  

#button to start the mayhem
start = tk.Button(frame,text="", bg="green")
start.grid(row = rowsandcol+1, column=0) 



#bind all the buttons  
root.bind("<Button-1>", click)

root.mainloop()