# -*- coding: utf-8 -*-
#
# Copyright 2022 WeTest. All rights reserved.

import logging
import time
import traceback

from . import elemutil
from . import messages

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
_logger = logging.getLogger("vpnui")  # default level: INFO

PREFERENCES_BUNDLE_ID = "com.apple.Preferences"

_setting_ui_locale = "cn"


def _i18n(s):
    return messages.get_i18n_string(_setting_ui_locale, s)


def _wait_for_page_load():
    time.sleep(3)


def _dismiss_popups(session):
    default_accept_buttons = [
        "取消", "以后", "好", "关闭", "Not Now", "Cancel", "OK", "Later", "Close"
    ]
    while session.alert.exists:
        session.alert.click(default_accept_buttons)
        time.sleep(3)


def _fill_out_l2tp_info(session, description, server, account, password, secret):
    _logger.info("Filling out L2TP info")
    _wait_for_page_load()
    # Select VPN Type
    elemutil.find_and_tap_cell(session, _i18n("TYPE"))
    _wait_for_page_load()
    elemutil.find_and_tap_cell(session, "L2TP")
    # Back
    elemutil.find_and_tap_button(session, _i18n("ADD_CONFIGURATION"))

    _wait_for_page_load()
    # Set fields
    elemutil.set_text_field(session, _i18n("DESCRIPTION"), description)
    elemutil.set_text_field(session, _i18n("SERVER"), server)
    elemutil.set_text_field(session, _i18n("ACCOUNT"), account)

    elemutil.set_secure_text_field(session, _i18n("PASSWORD"), password)
    elemutil.set_secure_text_field(session, _i18n("SECRET"), secret)

    # Done
    elemutil.find_and_tap_button(session, _i18n("DONE"))
    time.sleep(6)  # wait for a while.
    return True


def _go_to_vpn_setting_page(s):
    _logger.info("Going to VPN setting page")
    _wait_for_page_load()
    _dismiss_popups(s)
    elemutil.find_and_tap_cell(s, _i18n("GENERAL"))
    _wait_for_page_load()
    if elemutil.cell_exists(s, _i18n("VPN_AND_DEVICE_MANAGEMENT")):
        elemutil.find_and_tap_cell(s, _i18n("VPN_AND_DEVICE_MANAGEMENT"))
    elif elemutil.cell_exists(s, _i18n("VPN")):
        elemutil.find_and_tap_cell(s, _i18n("VPN"))

    else:
        _logger.warning("VPN cell NOT found.")
        return False
    _wait_for_page_load()
    # iOS15:
    if elemutil.is_greater_than_or_equals_to_ios15(s):
        if elemutil.cell_exists(s, _i18n("VPN")):
            elemutil.find_and_tap_cell(s, _i18n("VPN"))

    _wait_for_page_load()


def _wait_connected(s):
    _logger.info("Waiting for connection")
    timeout = 60  # [seconds]
    timeout_start = time.time()
    while time.time() < timeout_start + timeout:
        if elemutil.alert_exists(s, _i18n("VPN_CONNECTION")):
            _logger.warning("Failed to connect to the specified VPN")
            return False
        if elemutil.cell_exists(s, _i18n("STATUS_CONNECTED")):
            _logger.info("Connected to the specified VPN")
            time.sleep(6)  # wait for a while.
            return True
        time.sleep(5)
    return False


def set_locale(locale):
    """ Set locale of the iOS.

        Args:
           locale(str): either "cn" or "en"

    """
    global _setting_ui_locale
    _setting_ui_locale = locale


def connect(wda_client, vpn_name):
    """ Connect to the VPN with description 'vpn_name'

    Args:
       wda_client: the WDA client object. It's created by wda.Client(wda_server_url).
       vpn_name (str): the description of the VPN configuration.

    Returns:
       bool: The return value. True for success, False otherwise.
    """

    wda_client.app_stop(PREFERENCES_BUNDLE_ID)
    with wda_client.session(bundle_id=PREFERENCES_BUNDLE_ID) as s:
        _go_to_vpn_setting_page(s)
        if elemutil.cell_exists(s, vpn_name):
            elemutil.find_and_tap_cell(s, vpn_name)
            if elemutil.switch_exists(s, _i18n("STATUS_CONNECTED")):
                _logger.warning("\"{}\" already connected. do not need to connect it again.".format(vpn_name))
                return True
            else:
                elemutil.find_and_tap_switch(s)
                return _wait_connected(s)
        else:
            _logger.warning("\"{}\" NOT found".format(vpn_name))
            return False
    return False


def disconnect(wda_client):
    """ Disconnect from the connected VPN connection

    Args:
       wda_client: the WDA client object. It's created by wda.Client(wda_server_url).
    """

    wda_client.app_stop(PREFERENCES_BUNDLE_ID)
    with wda_client.session(bundle_id=PREFERENCES_BUNDLE_ID) as s:
        try:
            _go_to_vpn_setting_page(s)
            if elemutil.contains_switch(s):
                if elemutil.switch_exists(s, _i18n("STATUS_CONNECTED")):
                    elemutil.find_and_tap_switch(s)
                    time.sleep(6)
                else:
                    _logger.warning("VPN Not Connected")
            else:
                _logger.warning("Switches NOT found. It seems there is no VPN configuration")
        except Exception as ex:
            print(traceback.format_exc())
    return True


def add_l2tp_vpn(wda_client, vpn_name, server, account, password, secret):
    """ Add an L2TP VPN configuration in the iOS Settings.

    Args:
       wda_client: the WDA client object. It's created by wda.Client(wda_server_url).
       vpn_name (str): the description of the VPN configuration.
       server (str): LT2P server address
       account (str): LT2P VPN account name.
       password (str): LT2P VPN account password.
       secret (str): LT2P VPN account secret.

   Returns:
       bool: The return value. True for success, False otherwise.
 """
    wda_client.app_stop(PREFERENCES_BUNDLE_ID)
    with wda_client.session(bundle_id=PREFERENCES_BUNDLE_ID) as s:
        try:
            _go_to_vpn_setting_page(s)

            if elemutil.cell_exists(s, vpn_name):
                _logger.warning("\"{}\" exists. It will not be added again.".format(vpn_name))
                time.sleep(6)  # wait for a while
                return False
            else:
                if elemutil.cell_exists(s, _i18n("ADD_VPN_CONFIGURATION")):
                    elemutil.find_and_tap_cell(s, _i18n("ADD_VPN_CONFIGURATION"))
                elif elemutil.cell_exists(s, _i18n("ADD_VPN_CONFIGURATION_IOS13")):
                    elemutil.find_and_tap_cell(s, _i18n("ADD_VPN_CONFIGURATION_IOS13"))

                return _fill_out_l2tp_info(s, description=vpn_name,
                                           server=server,
                                           account=account,
                                           password=password,
                                           secret=secret
                                           )
        except Exception as ex:
            print(traceback.format_exc())
    return False


def remove_vpn(wda_client, vpn_name):
    """ Remove an L2TP VPN configuration

    Args:
       wda_client: the WDA client object. It's created by wda.Client(wda_server_url).
       vpn_name (str): the description of the VPN configuration.

    Returns:
           bool: The return value. True for success, False otherwise.
    """

    wda_client.app_stop(PREFERENCES_BUNDLE_ID)
    with wda_client.session(bundle_id=PREFERENCES_BUNDLE_ID) as s:
        try:
            _go_to_vpn_setting_page(s)
            if elemutil.cell_exists(s, vpn_name):
                elemutil.find_and_tap_cell(s, vpn_name)
                elemutil.find_and_tap_cell_button(s, vpn_name, _i18n("MORE_INFORMATION"))
                if elemutil.cell_exists(s, _i18n("DELETE_VPN")):
                    elemutil.find_and_tap_cell(s, _i18n("DELETE_VPN"))
                elif elemutil.cell_exists(s, _i18n("DELETE_VPN_IOS13")):
                    elemutil.find_and_tap_cell(s, _i18n("DELETE_VPN_IOS13"))

                _wait_for_page_load()
                if elemutil.alert_exists(s, _i18n("DELETE_VPN_QUESTION_MARK")) \
                        or elemutil.alert_exists(s, _i18n("DELETE_VPN_QUESTION_MARK_IOS13")):
                    elemutil.find_and_tap_button(s, _i18n("DELETE"))
                    time.sleep(6)  # wait for a while
                    return True
            else:
                _logger.warning("\"{}\" NOT found".format(vpn_name))
                time.sleep(6)  # wait for a while
                return False

        except Exception as ex:
            print(traceback.format_exc())
    return False
