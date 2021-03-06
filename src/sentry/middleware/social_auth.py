"""
sentry.middleware.social_auth
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2010-2014 by the Sentry Team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

from __future__ import absolute_import

from django.core.urlresolvers import reverse
from social_auth.middleware import SocialAuthExceptionMiddleware

from sentry.utils.http import absolute_uri


class SentrySocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    def get_redirect_uri(self, request, exception):
        return absolute_uri(reverse('sentry-login'))
