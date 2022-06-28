### File structure
#### vpnutil
 The library to manipulate iOS L2TP VPN settings. vpnui.py is the major file.

Please read following APIs method doc for details:
 * vpnui.set_locale
 * vpnui.add_l2tp_vpn
 * vpnui.connect
 * vpnui.disconnect
 * vpnui.remove_vpn
#### main.py
The demo script.
#### runTest.sh
The entry point during the script package running on WeTest Cloud. It is invoked by WeTest.
#### endTest.sh
The cleanup stage shell script the script package running on WeTest Cloud. It is invoked by WeTest.
#### requirements.txt
The python requirements.txt used by pip. In WeTest Cloud environment, those libraries have been installed.
#### zip_package.sh
The shell script to compress all files into one zip file. The generated zip file could be submitted to and run on WeTest Cloud
