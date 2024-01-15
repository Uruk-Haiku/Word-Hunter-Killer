import string

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
        nodes = []
        input = input.split()

        for i in range(len(input)):
            nodes.append(Node(input[i], i))

        # Nodes now need to be connected properly.
        for i in range(16):  # Since letters are in 4x4 grid == 16 nodes
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
                nodes[i].link(nodes[j])

        # Nodes are now connected. Graph can be searched for words.
        solutions = search(nodes)

    def search(self, nodes):
        """Searches through the word matrix, returns a dict.
            Keys == words (String)
            Items == swipe order (list of indices)

        :return: dict
        """



def main():
    ### Data Intake ###
    # TODO
    input = "A B C D \n E F G H \n I J K L \n L M N O"

    ### Data Processing ###
    # input format: "A B C D \n E F G H \n I J K L \n L M N O"




    ### Result Presenting ###

    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
