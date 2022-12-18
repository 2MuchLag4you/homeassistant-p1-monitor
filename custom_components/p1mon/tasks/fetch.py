from __future__ import annotations

from datetime import datetime
from pprint import pprint
from telnetlib import Telnet
from typing import Any

from re import sub, search

from custom_components.p1mon.exceptions import (
    P1MonConnectionBrokenError, 
    P1MonConnectionError, 
    P1MonEmptyResponseError, 
    P1MonIndexError, 
    P1MonValueError
)

async def fetch(host: str, port: int) -> dict[str, Any]:
    message_eol = '!'.encode('ascii')
    output_values = {}

    try: 
        telnet_connection = Telnet(host, port)
    except:
        raise P1MonConnectionError("Connection could not be made, host is offline")
    
    try:
        telnet_output = telnet_connection.read_until(message_eol)
    except:
        raise P1MonConnectionBrokenError("Terminated request, output could not be read")

    telnet_strings = (telnet_output.decode('ascii')).split('\n')
    if len(telnet_strings) == 0:
        raise P1MonEmptyResponseError("Terminated module, output could not be read from host")
    
    telnet_strings.remove('/KFM5KAIFA-METER\r')
    telnet_strings.remove('\r')
    telnet_strings.remove('!')   

    output_list = []
    for output_line in telnet_strings:
        output_value =  str(sub(r"[0-9]-[0-9]:", "", output_line.replace('\r', '')))
        reg_string = search('([0-9]{1,2}\.[0-9]{1,2}\.[0-9]{1,2})\((.*)\)', output_value)
        if reg_string.group(2) != "":
            output_list.append(reg_string.group(2))

    try:
        # Define all infromation into dict
        output_values["VERSION"] = output_list[0]
        output_values["SESSION_TIME"] = datetime.strptime(output_list[1][:-1], '%y%m%d%H%M%S')
        output_values["DEVICE_ID"] = output_list[2]
        output_values["CONSUMPTION_KWH_LOW"] = float(output_list[3][:-4])
        output_values["CONSUMPTION_KWH_HIGH"] = float(output_list[4][:-4])
        output_values["PRODUCTION_KWH_LOW"] = float(output_list[5][:-4])
        output_values["PRODUCTION_KWH_HIGH"] = float(output_list[6][:-4])
        output_values["TARIFCODE"] = int(output_list[7])
        output_values["CONSUMPTION_W_TODAY"] = float(output_list[8][:-3])
        output_values["PRODUCTION_W_TODAY"] = float(output_list[9][:-3])
        output_values["CONSUMPTION_W"] = float(output_list[16][:-3])
        output_values["PRODUCTION_W"] = float(output_list[17][:-3])

        output_values["voltage_phase_l1"] = float(output_list[13])
        output_values["voltage_phase_l2"] = None
        output_values["voltage_phase_l3"] = None

        output_values["current_phase_l1"] = float(output_list[15][:-2])
        output_values["current_phase_l2"] = None
        output_values["current_phase_l3"] = None

        output_values["power_consumed_phase_l1"] = float(output_list[16][:-3])
        output_values["power_consumed_phase_l2"] = None
        output_values["power_consumed_phase_l3"] = None

        output_values["power_produced_phase_l1"] = float(output_list[17][:-3])
        output_values["power_produced_phase_l2"] = None
        output_values["power_produced_phase_l3"] = None
    except IndexError:
        raise P1MonIndexError("Not all the data was fetched from the module")
    except ValueError:
        raise P1MonValueError("There was an issue with processing a value from the module")
    
    return output_values