# Class that makes it easier to copy over Protocol name logic,
# instead of having to retype it each time.

from enum import Enum

class Protocol(Enum):
    LOGIN = 1   # For logging into account.
    CREATE = 2  # For account creation.
    CLOSE = 3 # For closing the program.

# Returns string representation of a given protocol.
# TODO: Change name.
def initiate_protocol (num: int) -> str:
    return str(Protocol(num)).split(".")[1]

#print(initiate_protocol(2))