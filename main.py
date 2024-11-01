import sys
from tkinter import *
from tkinter import ttk
import colorsys

# I literally cannot figure out a better way to do this.
solution_index = 0
solutions = list()

class Node:
    def __init__(self, letter, number):
        self.letter = letter
        self.number = number  # Necessary so swipe order can be shown clearly visually
        self.neighbours = set()

    def link(self, other):
        self.neighbours.add(other)
        other.neighbours.add(self)


class Word_Matrix:
    def __init__(self, input):

        # Pull word list
        file = open('wordlist.txt')

        print('\033[1;35m' + 'word-hunter-killer' + '\033[0m' + ': Loading word list')
        print('Words from: ' + file.readline().strip())

        file.readline()
        content = file.read()
        word_list = set(content.split('\n'))

        print('Loaded')
        print('\033[1;35m' + 'word-hunter-killer' + '\033[0m' + ': Searching for words')

        node_list = []

        for i in range(len(input)):
            node_list.append(Node(input[i], i))  # Can do this since strings are iterable!

        # Nodes now need to be connected properly.
        for i in range(16):  # Since letters are in 4x4 grid == 16 nodes

            # Is the node on these edges?
            left_edge = (i % 4 == 0)
            right_edge = (i % 4 == 3)
            top_edge = (i < 4)
            bottom_edge = (i > 11)

            if top_edge and left_edge:  # TOP LEFT
                neighbour_indices = [1, 4, 5]  # Hardcodeable because table is always the same
            elif top_edge and right_edge:  # TOP RIGHT
                neighbour_indices = [2, 6, 7]
            elif bottom_edge and left_edge:  # BOTTOM LEFT
                neighbour_indices = [8, 9, 13]
            elif bottom_edge and right_edge:  # BOTTOM RIGHT
                neighbour_indices = [10, 11, 14]
            elif top_edge:  # TOP MIDDLE
                neighbour_indices = [i - 1, i + 1, i + 3, i + 4, i + 5]
            elif bottom_edge:  # BOTTOM MIDDLE
                neighbour_indices = [i - 5, i - 4, i - 3, i - 1, i + 1]
            elif left_edge:  # LEFT MIDDLE
                neighbour_indices = [i - 4, i - 3, i + 1, i + 4, i + 5]
            elif right_edge:  # RIGHT MIDDLE
                neighbour_indices = [i - 5, i - 4, i - 1, i + 3, i + 4]
            else:  # CENTRAL FOUR
                neighbour_indices = [i - 5, i - 4, i - 3, i - 1, i + 1, i + 3, i + 4, i + 5]

            for j in neighbour_indices:
                node_list[i].link(node_list[j])

        # Nodes are now connected. Graph can be searched for words.
        # Solutions is a dict. Keys are words, items are list of node integers - the swipe order
        # Passing dicts passes shallow copy - so can just pass solution dict in and edit inside

        solves = dict()

        for node in node_list:
            word_bfs(node, list(), '', word_list, solves)

        for word in solves:
            solutions.append(solves[word])

        print('Found ' + str(len(solutions)) + ' Words')
        print('Words loaded')
        print('\033[1;35m' + 'word-hunter-killer' + '\033[0m' + ': Displaying results')
        print()
        print('Destroy them.') # print("Go get 'em tiger.")

        # for solution in solutions:
        #     print(solution)
        # for word in solves.keys():
        #     print(word)

        display(solutions)


def word_bfs(node, path, word_so_far, word_list, solutions):
    # Housekeeping
    new_path = path + [node.number]
    new_word_so_far = word_so_far + node.letter

    if new_word_so_far in word_list and len(new_word_so_far) >= 3:
        solutions[new_word_so_far] = new_path

    for neighbour in node.neighbours:
        if neighbour.number not in new_path:  # Prevent double-counting same node in word
            word_bfs(neighbour, new_path, new_word_so_far, word_list, solutions)


def display(solutions):
    # TODO graphics
    root = Tk()
    root.title('Word Hunter-Killer')
    global can # yes bad practice but I don't want to make the window until after command line text is entered. Sue me.
    can = Canvas(root, width=400, height=400)
    can.grid()

    # # Grid
    # # Verticals
    # can.create_line(100, 0, 100, 400, fill='black')
    # can.create_line(200, 0, 200, 400, fill='black')
    # can.create_line(300, 0, 300, 400, fill='black')
    # can.create_line(400, 0, 400, 400, fill='black')

    # # Horizontals
    # can.create_line(0, 100, 400, 100, fill='black')
    # can.create_line(0, 200, 400, 200, fill='black')
    # can.create_line(0, 300, 400, 300, fill='black')
    # can.create_line(0, 400, 400, 400, fill='black')

    global display
    display = [None]*16
    for i in range(16):
        x0 = (i % 4)*100
        y0 = (i // 4)*100
        x1 = x0 + 100
        y1 = y0 + 100

        display[i] = can.create_rectangle(x0, y0, x1, y1, fill='lightgrey', outline='black', width=1)

    display_solution(solutions, solution_index)
    print('LENGTH OF SOLUTIONS: ' + str(len(solutions)))

    root.bind('<KeyRelease>', change)
    root.mainloop()


def change(event):
    # TODO Add display of action sequences to UI.
    global solution_index
    global solutions

    if event.keysym == 'Right':
        # Advance right
        print('RIGHT SHIFT')
        can.itemconfig(display[0], fill='blue')
        if solution_index < len(solutions) - 1:
            solution_index += 1
        print(solution_index)
    elif event.keysym == 'Left':
        # Regress left
        print('LEFT SHIFT')
        can.itemconfig(display[0], fill='red')
        if solution_index > 0:
            solution_index -= 1
        print(solution_index)

    display_solution(solutions, solution_index)


def display_solution(solutions, solution_index):
    for i in range(len(display)):
        can.itemconfig(display[i], fill='lightgrey')
    solution = solutions[solution_index]
    colour_increment = 1 / len(solution)
    current_colour = 0
    for i in range(len(solution)):
        r, g, b = colorsys.hsv_to_rgb(current_colour, 1, 1)
        fill = '#{:02x}{:02x}{:02x}'.format(int(r * 255), int(g * 255), int(b * 255))
        can.itemconfig(display[solution[i]], fill=fill)
        current_colour += colour_increment
        
    print(solution)

    

def main():
    ### Data Intake ###
    # TODO

    input_accepted = False
    fails = 0
    
    while not input_accepted:
        try:
            raw_input = str(input('\033[1;35m' + 'word-hunter-killer' + '\033[0m' + ': Enter the content of the grid, left to right, top to bottom, no delimiters or newlines.\n'))

            # Command parsing
            # TODO use argparse and add more options
            if raw_input == 'quit' or raw_input == 'q':
                print('\033[1;35m' + 'word-hunter-killer' + '\033[0m' + ': Quitting.')
                sys.exit()
            

            ### Data Processing ###
            # target processed format: "ABCDEFGHIJKLMNO"
            processed_input = raw_input.translate( {ord(c): None for c in ' \n\t,.;'} ) # Common delimiters
            processed_input = processed_input.upper()

            if len(processed_input) < 16:
                raise ValueError('Input too short')
            if len(processed_input) > 16:
                raise ValueError('Input too long')
            if not processed_input.isalpha():
                raise ValueError('Non-alphabetic characters inserted')
            
            input_accepted = True
            
        except ValueError as value_err:
            print(value_err.args[0] + '. Please re-enter your grid.\n')
            fails += 1

            if fails >= 3:
                print('\033[1;35m' + 'word-hunter-killer' + '\033[0m' + ': Too many failures. Closing.')
                sys.exit()

    Word_Matrix(processed_input)

    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
