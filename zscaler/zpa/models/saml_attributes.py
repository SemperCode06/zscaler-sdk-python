"""
Copyright (c) 2023, Zscaler Inc.

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
"""

from zscaler.oneapi_object import ZscalerObject


class SAMLAttribute(ZscalerObject):
    def __init__(self, config=None):
        """
        Initialize the SAMLAttribute model based on API response.

        Args:
            config (dict): A dictionary representing the SAML attribute configuration.
        """
        super().__init__(config)
        if config:
            self.id = config["id"] if "id" in config else None
            self.creation_time = config["creationTime"] if "creationTime" in config else None
            self.modified_by = config["modifiedBy"] if "modifiedBy" in config else None
            self.name = config["name"] if "name" in config else None
            self.user_attribute = config["userAttribute"] if "userAttribute" in config else None
            self.idp_id = config["idpId"] if "idpId" in config else None
            self.saml_name = config["samlName"] if "samlName" in config else None
            self.idp_name = config["idpName"] if "idpName" in config else None
            self.delta = config["delta"] if "delta" in config else None
        else:
            self.id = None
            self.creation_time = None
            self.modified_by = None
            self.name = None
            self.user_attribute = None
            self.idp_id = None
            self.saml_name = None
            self.idp_name = None
            self.delta = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "id": self.id,
            "creationTime": self.creation_time,
            "modifiedBy": self.modified_by,
            "name": self.name,
            "userAttribute": self.user_attribute,
            "idpId": self.idp_id,
            "samlName": self.saml_name,
            "idpName": self.idp_name,
            "delta": self.delta,
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
