"""
This script shows how to implement a state machine -
or an object that operates in a number of different states
but you dont want a bunch of conditionals

This removes the need for a bunch of conditional checks (which suck).
Secondly the performance is poor. - because the state is always being
checked. A more elegant approach is to encode each operational state as
a separate class - and arrange for the Connection class to delegate to the
state Class - for example...
"""


class Connection:
    def __init__(self):
        self.new_state(ClosedConnectionState)

    def new_state(self, newstate):
        self._state = newstate

    # Delegate to the state class
    def read(self):
        return self._state.read(self)

    def write(self, data):
        return self._state.write(self, data)

    def open(self):
        return self._state.open(self)

    def close(self):
        return self._state.close(self)


# Connection state base class
class ConnectionState:
    @staticmethod
    def read(conn):
        raise NotImplementedError()

    @staticmethod
    def write(conn, data):
        raise NotImplementedError()

    @staticmethod
    def open(conn):
        raise NotImplementedError()

    @staticmethod
    def close(conn):
        raise NotImplementedError()


# Implementation of different states
class ClosedConnectionState(ConnectionState):
    @staticmethod
    def write(conn, data):
        raise RuntimeError("Not Open")

    @staticmethod
    def open(conn):
        conn.new_state(OpenConnectionState)

    @staticmethod
    def close(conn):
        raise RuntimeError("Already closed")

    @staticmethod
    def read(conn):
        raise RuntimeError("Not open")


class OpenConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        print("reading")

    @staticmethod
    def write(conn, data):
        print("writing")

    @staticmethod
    def open(conn):
        raise RuntimeError("Already open")

    @staticmethod
    def close(conn):
        conn.new_state(ClosedConnectionState)


# The follow implementation shows the direct manipulation of the __class__ attribute


class Connection:
    def __init__(self):
        self.new_state(ClosedConnection)

    def new_state(self, newstate):
        self.__class__ = newstate

    def read(self):
        raise NotImplementedError()

    def write(self, data):
        raise NotImplementedError()

    def open(self):
        raise NotImplementedError()

    def close(self):
        raise NotImplementedError()


class ClosedConnection(Connection):
    def read(self):
        raise RuntimeError("Not open")

    def write(self, data):
        raise RuntimeError("Not open")

    def open(self):
        self.new_state(OpenConnection)

    def close(self):
        raise RuntimeError("Already closed")


class OpenConnection(Connection):
    def read(self):
        print("reading")

    def write(self, data):
        print("writing")

    def open(self):
        raise RuntimeError("Already open")

    def close(self):
        self.new_state(ClosedConnection)


"""
This implementation benefits from the fact that it eliminates an extra level of misdirection.
Instead of having a Connection and ConnectionState class - they are merged into one. At state
change the instance will change its type.

This can result in slightly faster code as all of the methods on the connection no longer
involve an extra delegation step.

This pattern is great for implementing more complicated state machines (see below)
"""


class State:
    def __init__(self):
        self.new_state(State_A)

    def new_state(self, state):
        self.__class__ = state

    def action(self, x):
        raise NotImplementedError()


class State_A(State):
    def action(self, x):
        self.new_state(State_B)


class State_B(State):
    def action(self, x):
        self.new_state(State_C)


class State_C(State):
    def action(self, x):
        self.new_state(State_A)


# Loosley based on the 'state design pattern'
