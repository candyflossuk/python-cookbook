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
