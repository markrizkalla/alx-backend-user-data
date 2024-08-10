#!/usr/bin/env python3
""" Module of Auth
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """ Auth class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require auth
        Args
            path: str
            excluded_paths: excluded path

        Return:
            bool
        """
        if path is None or excluded_paths is None or len(exclused_paths) == 0:
            return True

        if path[-1] != '/':
            path = path + '/'

        for excluded in excluded_paths:
            if excluded == path:
                return False

        return False

    def authorization_header(self, request=None) -> str:
        """ auth header

        Args:
            request: the request

        Return:
            str
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user
        Args:
            request: the req

        Return:
            user
        """
        return None
