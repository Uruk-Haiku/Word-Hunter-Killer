from tkinter import *
from tkinter import ttk

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

        print('======================= Loading Word List =======================')
        print('Words from: ' + file.readline())
        file.readline()

        content = file.read()
        word_list = set(content.split('\n'))

        print('============================ Loaded =============================')
        print()
        print()
        print()
        print('========================= Finding Words =========================')

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

        solutions = dict()

        for node in node_list:
            word_bfs(node, list(), '', word_list, solutions)

        # Solutions is now complete. Display the swipes!
        print('Found ' + str(len(solutions)) + ' Words')
        print('========================== Words Loaded =========================')
        print()
        print()
        print()
        print('======================== Display Results ========================')
        print("Go get 'em tiger.")
        print()

        display(solutions)

        # for solution in solutions.items():
        #     print(solution)


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
    can = Canvas(root, width=400, height=400)
    can.grid()

    backing = can.create_rectangle(0, 0, 400, 400, fill='lightgrey', outline='black', width=1)

    # Grid
    # Verticals
    can.create_line(100, 0, 100, 400, fill='black')
    can.create_line(200, 0, 200, 400, fill='black')
    can.create_line(300, 0, 300, 400, fill='black')
    can.create_line(400, 0, 400, 400, fill='black')

    # Horizontals
    can.create_line(0, 100, 400, 100, fill='black')
    can.create_line(0, 200, 400, 200, fill='black')
    can.create_line(0, 300, 400, 300, fill='black')
    can.create_line(0, 400, 400, 400, fill='black')

    root.bind('<KeyRelease>', change)



    # ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    # ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

    root.mainloop()


def change(event):
    """
    Advance or regress to the next/previous word.

    :param event:
    :return: NIL
    """
    if event.keysym == 'Right':
        # Advance right
        pass
    elif event.keysym == 'Left':
        # Regress left
        pass



def main():
    ### Data Intake ###
    # TODO
    input = 'A B C D \n E F G H \n I J K L \n L M N O'

    ### Data Processing ###
    # input format: "A B C D \n E F G H \n I J K L \n L M N O"
    # processed format: "ABCDEFGHIJKLMNO"

    processed_input = 'HDHFRNOAETOTALER'
    Word_Matrix(processed_input)


    ### Result Presenting ###

    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
