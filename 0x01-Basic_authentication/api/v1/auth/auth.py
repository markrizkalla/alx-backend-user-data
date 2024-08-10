#!/usr/bin/env python3
""" Module of Auth
"""
from flask import request


class Auth():
    """ Auth class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require auth"""

        return False

    def authorization_header(self, request=None) -> str:
        """ auth header """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user """
        return None
