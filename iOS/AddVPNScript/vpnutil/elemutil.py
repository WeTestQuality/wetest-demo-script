# -*- coding: utf-8 -*-
#
# Copyright 2022 WeTest. All rights reserved.

import time

from packaging import version


def cell_exists(session, name):
    predicate = "name == \"{}\" AND type == \"XCUIElementTypeCell\"".format(name)
    return session(predicate=predicate).exists


def alert_exists(session, name):
    predicate = "name == \"{}\" AND type == \"XCUIElementTypeAlert\"".format(name)
    return session(predicate=predicate).exists


def switch_exists(session, name):
    predicate = "name == \"{}\" AND type == \"XCUIElementTypeSwitch\"".format(name)
    return session(predicate=predicate).exists


def contains_switch(session):
    predicate = "type == \"XCUIElementTypeSwitch\""
    return session(predicate=predicate).exists


def _scroll_find_and_tap_cell(session, name):
    found = False
    while not found:
        predicate = "name == \"{}\" AND type == \"XCUIElementTypeCell\"".format(name)
        cell = session(predicate=predicate).get()
        if cell.visible:
            found = True;
            if is_greater_than_or_equals_to_ios15(session):
                cell.click()
            else:
                cell.tap()
        else:
            _slightly_swipe_up(session)
            time.sleep(4)
    return


def find_and_tap_cell(session, name):
    _scroll_find_and_tap_cell(session, name)


def find_and_tap_switch(session):
    predicate = "type == \"XCUIElementTypeSwitch\""
    session(predicate=predicate).click()
    return


def find_and_tap_navigation_bar(session, name):
    predicate = "name == \"{}\" AND type == \"XCUIElementTypeNavigationBar\"".format(name)
    session(predicate=predicate).click()
    return


def find_and_tap_button(session, name):
    predicate = "name == \"{}\" AND type == \"XCUIElementTypeButton\"".format(name)
    session(predicate=predicate).click()
    return


def _slightly_swipe_up(session):
    w, h = session.window_size()
    return session.swipe(w // 2, h // 2 + 100, w // 2, h // 2 - 100)


def _scroll_find_and_tap_cell_button(session, cell_name, button_name):
    found = False
    while not found:
        xpath = "//XCUIElementTypeCell[@name=\"{}\"]/XCUIElementTypeButton[@name=\"{}\"]".format(cell_name, button_name)
        cell = session(xpath=xpath).get()
        if cell.visible:
            found = True;
            cell.click()
        else:
            _slightly_swipe_up(session)
            time.sleep(4)
    return


def find_and_tap_cell_button(session, cell_name, button_name):
    xpath = "//XCUIElementTypeCell[@name=\"{}\"]/XCUIElementTypeButton[@name=\"{}\"]".format(cell_name, button_name)
    session(xpath=xpath).tap()


def set_text_field(session, field_name, field_value):
    predicate = "name == \"{}\" AND type == \"XCUIElementTypeTextField\"".format(field_name)
    textfield = session(predicate=predicate).get()
    textfield.set_text(field_value)


def set_secure_text_field(session, field_name, field_value):
    predicate = "name == \"{}\" AND type == \"XCUIElementTypeSecureTextField\"".format(field_name)
    textfield = session(predicate=predicate).get()
    textfield.set_text(field_value)


def is_switch_on(session):
    predicate = "type == \"XCUIElementTypeSwitch\""
    switch = session(predicate=predicate).get()
    print("switch", switch.value)
    return switch.value == "1"


def is_greater_than_or_equals_to_ios14(session):
    os_version_string = session.status()["os"]["version"]
    if version.parse(os_version_string) >= version.parse("14.0"):
        return True
    return False


def is_greater_than_or_equals_to_ios15(session):
    os_version_string = session.status()["os"]["version"]
    if version.parse(os_version_string) >= version.parse("15.0"):
        return True
    return False


def is_less_than_ios12(session):
    os_version_string = session.status()["os"]["version"]
    if version.parse(os_version_string) < version.parse("12.0"):
        return True
    return False
