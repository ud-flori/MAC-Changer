import subprocess
import re
# ifconfig eth0 down
# ifconfig eth0 hw ether 00:11:22:33:44:55
# ifconfig eth0 up


class MAC_Changer:

    """ This Class allow you to get your devices MAC address and change it.
    """

    def __init__ (self):
        self.MAC = ""


    def get_MAC(self, iface):

        """This function get the devices MAC address.

        Returns:
            [type]: [description]
        """
        output = subprocess.run(["ifconfig", iface], shell=False, capture_output=True)

        cmd_result = output.stdout.decode('utf-8')


        pattern = r'ether\s[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}'
        regex = re.compile(pattern)
        ans = regex.search(cmd_result)

        current_mac_address = ans.group().split(" ")[1]
        self.MAC = current_mac_address
        return current_mac_address

    def change_mac(self, iface, new_mac):
        """This function change your MAC address to the given parameter.

        Args:
            iface ([type]): [description]
            new_mac ([type]): [description]

        Returns:
            [type]: [description]
        """
        print("[+] Current MAC address is ", self.get_MAC(iface))

        output = subprocess.run(["ifconfig", iface, "down"], shell=False, capture_output = True)


        print(output.stderr.decode('utf-8'))

        # ifconfig eth0 hw ether 00:11:22:33:44:55
        output = subprocess.run(["ifconfig", iface, "hw", "ether", new_mac], shell=False, capture_output = True)

        # ifconfig eth0 up
        output = subprocess.run(["ifconfig", iface, "up"], shell=False, capture_output = True)

        print("[+] Updated MAC address is ", self.get_MAC(iface))

        return self.get_MAC(iface)