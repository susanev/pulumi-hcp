# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

import types

__config__ = pulumi.Config('hcp')


class _ExportableConfig(types.ModuleType):
    @property
    def client_id(self) -> Optional[str]:
        """
        The OAuth2 Client ID for API operations.
        """
        return __config__.get('clientId') or _utilities.get_env('HCP_CLIENT_ID')

    @property
    def client_secret(self) -> Optional[str]:
        """
        The OAuth2 Client Secret for API operations.
        """
        return __config__.get('clientSecret') or _utilities.get_env('HCP_CLIENT_SECRET')

