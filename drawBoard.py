def draw_line(row):
    rowout = "|"
    for entry in row:
        rowout = rowout + entry + "|"
    print(rowout)

def start_game():
    print(" _ _ _ ")
    for row_num in range(3):
        row = ["_","_","_"]
        draw_line(row)

if __name__ == '__main__':
    start_game()
