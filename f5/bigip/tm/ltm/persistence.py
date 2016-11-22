# coding=utf-8
#
#  Copyright 2016 F5 Networks Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""Directory: ltm module: persistence.

REST URI
    ``https://localhost/mgmt/tm/ltm/persistence/source-addr?ver=11.6.0``

GUI Path
    ``XXX``

REST Kind
    ``tm:ltm:persistence:*``
"""


from f5.bigip.resource import Collection
from f5.bigip.resource import OrganizingCollection
from f5.bigip.resource import Resource


class Persistence(OrganizingCollection):
    '''A Collection concrete subclass docstring.'''
    def __init__(self, ltm):
        '''Auto generated constructor.'''
        super(Persistence, self).__init__(ltm)
        self._meta_data['allowed_lazy_attributes'] = [
            Source_Addrs,
            Hashs,
            Sips,
            Ssls,
            Dest_Addrs,
            Msrdps,
            Cookies,
            Universals
        ]
        self._meta_data['template_generated'] = True


class Source_Addrs(Collection):
    '''A Collection concrete subclass docstring.'''
    def __init__(self, persistence):
        '''Auto generated constructor.'''
        super(Source_Addrs, self).__init__(persistence)
        # self._meta_data['allowed_lazy_attributes'] = [Source_Addr]
        # self._meta_data['attribute_registry'] =\
        #     {u'tm:ltm:persistence:source-addr:source-addrstate':
        #      Source_Addr}
        self._meta_data['template_generated'] = True


class Hashs(Collection):
    '''A Collection concrete subclass docstring.'''
    def __init__(self, persistence):
        '''Auto generated constructor.'''
        super(Hashs, self).__init__(persistence)
        # self._meta_data['allowed_lazy_attributes'] = [Hash]
        # self._meta_data['attribute_registry'] =\
        #     {u'tm:ltm:persistence:hash:hashstate': Hash}
        self._meta_data['template_generated'] = True


class Sips(Collection):
    '''A Collection concrete subclass docstring.'''
    def __init__(self, persistence):
        '''Auto generated constructor.'''
        super(Sips, self).__init__(persistence)
        # self._meta_data['allowed_lazy_attributes'] = [Sip]
        # self._meta_data['attribute_registry'] =\
        #     {u'tm:ltm:persistence:sip:sipstate': Sip}
        self._meta_data['template_generated'] = True


class Ssls(Collection):
    '''A Collection concrete subclass docstring.'''
    def __init__(self, persistence):
        '''Auto generated constructor.'''
        super(Ssls, self).__init__(persistence)
        # self._meta_data['allowed_lazy_attributes'] = [Ssl]
        # self._meta_data['attribute_registry'] =\
        #     {u'tm:ltm:persistence:ssl:sslstate': Ssl}
        self._meta_data['template_generated'] = True


class Global_Settings(Resource):
    '''A Resource concrete subclass.'''
    def __init__(self, Global_Settings_s):
        '''Autogenerated constructor.'''
        super(Global_Settings, self).__init__(Global_Settings_s)
        self._meta_data['template_generated'] = True
        self._meta_data['required_json_kind'] =\
            "tm:ltm:persistence:global-settings:global-settingsstate"
        self._meta_data['attribute_registry'] =\
            {}


class Dest_Addrs(Collection):
    '''A Collection concrete subclass docstring.'''
    def __init__(self, persistence):
        '''Auto generated constructor.'''
        super(Dest_Addrs, self).__init__(persistence)
        # self._meta_data['allowed_lazy_attributes'] = [Dest_Addr]
        # self._meta_data['attribute_registry'] =\
        #     {u'tm:ltm:persistence:dest-addr:dest-addrstate': Dest_Addr}
        self._meta_data['template_generated'] = True


class Msrdps(Collection):
    '''A Collection concrete subclass docstring.'''
    def __init__(self, persistence):
        '''Auto generated constructor.'''
        super(Msrdps, self).__init__(persistence)
        # self._meta_data['allowed_lazy_attributes'] = [Msrdp]
        # self._meta_data['attribute_registry'] =\
        #     {u'tm:ltm:persistence:msrdp:msrdpstate': Msrdp}
        self._meta_data['template_generated'] = True


class Cookies(Collection):
    '''A Collection concrete subclass docstring.'''
    def __init__(self, persistence):
        '''Auto generated constructor.'''
        super(Cookies, self).__init__(persistence)
        self._meta_data['allowed_lazy_attributes'] = [Cookie]
        self._meta_data['attribute_registry'] =\
            {'tm:ltm:persistence:cookie:cookiestate': Cookie}
        self._meta_data['template_generated'] = True


class Cookie(Resource):
    '''A Resource concrete subclass.'''
    def __init__(self, cookies):
        '''Autogenerated constructor.'''
        super(Cookie, self).__init__(cookies)
        self._meta_data['template_generated'] = True
        self._meta_data['required_json_kind'] =\
            "tm:ltm:persistence:cookie:cookiestate"
        self._meta_data['attribute_registry'] =\
            {}


class Universals(Collection):
    '''A Collection concrete subclass docstring.'''
    def __init__(self, persistence):
        '''Auto generated constructor.'''
        super(Universals, self).__init__(persistence)
        self._meta_data['allowed_lazy_attributes'] = [Universal]
        # self._meta_data['attribute_registry'] =\
        #     {u'tm:ltm:persistence:universal:universalstate': Universal}
        self._meta_data['template_generated'] = True


class Universal(Resource):
    '''A Resource concrete subclass.'''
    def __init__(self, Universals):
        '''Autogenerated constructor.'''
        super(Universal, self).__init__(Universals)
        self._meta_data['template_generated'] = True
        self._meta_data['required_json_kind'] =\
            "tm:ltm:persistence:universal:universalstate"
        self._meta_data['attribute_registry'] =\
            {}
