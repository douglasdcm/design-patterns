# State is the interface to be implemented by its subclasses
class TCPState:
    def change_state(self, tcp_connection, state):
        return tcp_connection.change_state(state)

    def active_open(self, tcp_connection):
        pass

    def close(self, tcp_connection):
        pass


# This ia a ConcretState which implemts the function "active_state"
class TCPClose(TCPState):
    def active_open(self, tcp_connection):
        # send SYN, receive SYN, ACK, etc. Executes a specific job
        self.change_state(tcp_connection, TCPActiveOpen())


# Same as TCPClose
class TCPActiveOpen(TCPState):
    def close(self, tcp_connection):
        # send FYN, receive ACk from FYN, etc. Executes a specific job
        return self.change_state(tcp_connection, TCPClose())


# Connection is the classes used by the client. It delegates the specific job to subclassed
# of State interface
class TCPConnection:
    def __init__(self) -> None:
        self._state: TCPState = TCPClose()

    def get_state(self):
        return self._state

    def change_state(self, state: TCPState):
        self._state = state

    def active_open(self):
        self._state.active_open(self)

    def close(self):
        self._state.close(self)


def client():
    # the default state is Close
    tcp_connection = TCPConnection()

    # as the Close class does not implement the function "close", it does nothing, because
    # the connetion is alreay closed
    tcp_connection.close()

    # as the connection is closed, it opens a new connection and changes the status to Open.
    # Inside of the funcion Close.activate_open could be an implementation to not stablish
    # a new connection if there is one already open (specific job)
    tcp_connection.active_open()

    # now, the status is Open, so the "close" function takes effect
    tcp_connection.close()

    # now, the current status is Close again
    status = tcp_connection.get_state()
    return status
