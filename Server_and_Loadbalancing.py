import random

class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random()*10+1
        # Add the connection to the dictionary with the calculated load
        self.connections[connection_id] = connection_load

    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        # Remove the connection from the dictionary
        del self.connections[connection_id]

    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        # Add up the load for each of the connections
        for load in self.connections.values():
            total+=load
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())
    


class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {}
        self.servers = [Server()]

    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        server = random.choice(self.servers)
        # Add the connection to the dictionary with the selected server
#         self.connections[server] =connection_id 
        # Add the connection to the server
        server.add_connection(connection_id)
        self.ensure_availability()

    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        # Find out the right server
        # Close the connection on the server
        # Remove the connection from the load balancer
        for server in self.servers:
            if connection_id in server.connections:
                server.close_connection(connection_id)
                break

    def avg_load(self):
        """Calculates the average load of all servers"""
        # Sum the load of each server and divide by the amount of servers
        total_load=0
        total_Server=0
        for server in self.servers:
            total_load+=server.load()
            total_Server+=1
        
        return total_load/total_Server

    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        if self.avg_load() >50:
            self.servers.append(Server())

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))





server=Server()
l=LoadBalancing()
server.add_connection('192.168.1.1')
print(f'server load is {server.load()} \n')

server.close_connection('192.168.1.1')
print(f'server load is {server.load()} \n')

print(f'connections available right now {server.connections}')

l.add_connection('192.168.1.1')
print(f'average load is : {l.avg_load()} \n')

l.servers.append(Server())
print(f'server load should be half of above  {l.avg_load()} \n')

l.close_connection('192.168.1.1')

print(f'average load is: {l.avg_load()} \n')

for connection in range(20):
    l.add_connection(connection)

print(f'average load is: {l.avg_load()} \n')