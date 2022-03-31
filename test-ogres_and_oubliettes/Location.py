class Location:
    name = ""
    description = ""
    connections = []

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = []

    def connect(self, connection):
        self.connections.append(connection)
        connection.connections.append(self)

    def printOutLocation(self):
        print(self.description)
        for path in self.connections:
            print(path.name)
    def travel(self, input):
        for path in self.connections:
            if path.name == input:
                return path
        return None


