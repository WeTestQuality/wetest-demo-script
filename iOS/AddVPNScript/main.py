# -*- coding: utf-8 -*-
#
# Copyright 2022 WeTest. All rights reserved.

import os

import wda

from vpnutil import vpnui


def main():
    if "WDA_SERVER_IP" in os.environ:
        # When run on WeTest Cloud environment
        wda_server_url = "http://%s:%s/" % (os.getenv("WDA_SERVER_IP"), os.getenv("WDA_SERVER_PORT"))
    else:
        # When run locally
        wda_server_url = "http://127.0.0.1:8100/"

    c = wda.Client(wda_server_url)

    vpnui.set_locale("cn")
    vpnui.add_l2tp_vpn(c, vpn_name="my-vpn-server-name",
                       server="123.123.123.123",
                       account="myvpnaccount",
                       password="myvpnpassword",
                       secret="myvpnsecret")
    vpnui.connect(c, vpn_name="my-vpn-server-name")
    vpnui.disconnect(c)
    vpnui.remove_vpn(c, vpn_name="my-vpn-server-name")


if __name__ == "__main__":
    main()
