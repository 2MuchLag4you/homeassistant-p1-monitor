# HomeAssistant - P1 Montor

The [letscontrolit](https://www.letscontrolit.com/) platform offers an telnet output of P1 data. This addon can be used to read the P1 data and can be used for the energy page of homeassistant.

[ESP EASY LETSCONTROL IT](https://www.letscontrolit.com/)

# Personal setup

D1 Mini connected to the p1 meter, with the firmware build `20111 - Mega`

# Configuration

Adding the `P1 monitor` to your Home Assistant can be done via the user interface, after the integration has been added to the `custom_components` .

- Add the p1mon folder inside the `config/custom_components`
- Restart Home Assistant
- In the side bar click on `Settings`
- From the configuration menu go to `Devices & Services`
- In the bottom right, click the `Add Integration` button.
- Select the "**SEMS Sensor**" from the list
- Follow the configuration instructions on screen to complete the setup
