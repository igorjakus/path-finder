class Scheme:

    def __init__(self):
        # Read map.txt and store it in list
        self.map = []
        with open('map.txt') as f:
            for line in f:
                self.map.append(line[:-1])

    def update_map(self):
        # Updates map by reading map.txt again
        self.map = []
        with open('map.txt') as f:
            for line in f:
                self.map.append(line[:-1])
    
    def find(self, wanted):
        # Find the position of thing you are looking for
        for x in range(0, len(self.map) - 1):
            for y in range(0, len(self.map[x]) - 1):
                if self.map[x][y] == wanted:
                    print(wanted, x, y)

    def find_is_wall(self, x, y):
        try:
            # When there's wall (#) in selected position
            return True if self.map[x][y] == '#' else False
        except IndexError:
            # When there's no element in that position
            return None
