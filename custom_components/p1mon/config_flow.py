from __future__ import annotations

import voluptuous as vol
from typing import Any

from homeassistant.const import CONF_HOST, CONF_PORT, CONF_NAME
from homeassistant import config_entries
from homeassistant.data_entry_flow import FlowResult
from homeassistant.config_entries import ConfigFlow
from custom_components.p1mon.exceptions import P1MonError
from custom_components.p1mon.classes import p1mon
from custom_components.p1mon.const import DOMAIN


@config_entries.HANDLERS.register(DOMAIN)
class P1monFlowHandler(ConfigFlow, domain=DOMAIN):

    VERSION = 1
    _errors = {}

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:

        self._errors = {}

        if user_input is not None:
            try:
                async with p1mon(
                    host=user_input[CONF_HOST], port=user_input[CONF_PORT]
                ) as client:
                    await client.smartmeter()
            except P1MonError:
                self._errors["base"] = "cannot_connect"
            else:
                return self.async_create_entry(
                    title=user_input[CONF_NAME],
                    data={
                        CONF_HOST: user_input[CONF_HOST],
                        CONF_PORT: user_input[CONF_PORT]
                    }
                )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Optional(
                        CONF_NAME,
                        default="P1 Monitor Module {}".format(
                            self.hass.config.location_name),
                        description="Module Name"
                    ): str,
                    vol.Required(
                        CONF_HOST,
                        default="192.168.178.23",
                        description="P1 Monitor IP"
                    ): str,
                    vol.Required(
                        CONF_PORT,
                        default=8088,
                        description="P1 Monitor Telnet port"
                    ): int
                }
            ),
            errors=self._errors
        )
