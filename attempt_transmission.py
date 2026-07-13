import time

from space_network_lib import *


class BrokenConnectionError(CommsError):
    pass



def attempt_transmission(packet : Packet, space_netwotk : SpaceNetwork):
    while True:

        try:
            space_netwotk.send(packet)
            break

        except TemporalInterferenceError:
            print('Interference ,waiting...')
            time.sleep(2)

        except DataCorruptedError:
            print('Data corrupted retrying...')
        
        except LinkTerminatedError:
            raise BrokenConnectionError('lost Link')  

        except OutOfRangeError:
            raise BrokenConnectionError('Target out of range')


