from space_network_lib import SpaceEntity, Packet, SpaceNetwork


class Satellite(SpaceEntity):
    def receive_signal(self, packet: Packet):
        print(f"[{self.name}] Received packet: {packet}")

space_network_1 = SpaceNetwork(level=1)
satellite_1 = Satellite(name="Satellite 1", distance_from_earth=100)
satellite_2 = Satellite(name="Satellite 2", distance_from_earth=200)
packet_1 = Packet(data="Hello, Satellite 2!", sender=satellite_1, receiver=satellite_2)
space_network_1.send(packet_1)
