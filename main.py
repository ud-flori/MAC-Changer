from MAC_Changer import MAC_Changer


if __name__ == "__main__":
    mc = MAC_Changer()
    mac = mc.get_MAC("eth0")
 

    current_mac = mc.change_mac("eth0", "00:11:22:33:44:55")

