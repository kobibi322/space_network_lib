import time

from space_network_lib import *



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

