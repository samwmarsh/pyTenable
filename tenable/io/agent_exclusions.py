'''
agent_exclusions
================

The following methods allow for interaction into the Tenable.io
:devportal:`agent exclusions <agent-exclusions>` API endpoints.

Methods available on ``tio.agent_exclusions``:

.. rst-class:: hide-signature
.. autoclass:: AgentExclusionsAPI

    .. automethod:: create
    .. automethod:: delete
    .. automethod:: details
    .. automethod:: edit
    .. automethod:: list
'''
from typing import *
from restfly.utils import dict_merge, dict_clean
from .base import TIOEndpoint
from datetime import date, datetime, timedelta
from .schemas.agent_exclusion_schema import AgentExclusionSchema


class AgentExclusionsAPI(TIOEndpoint):
    '''
    This class contain all methods related to agent exclusions
    '''
    _path: ClassVar[str] = 'scanners'

    def _validate(
            self,
            data: Dict[Any, Any],
            validator=AgentExclusionSchema
    ) -> Dict:
        return validator().load(data)

    def create(
            self,
            name: str,
            scanner_id: Optional[int] = 1,
            **kwargs
    ) -> Dict:
        '''
        Creates a new agent exclusion.

        :devportal:`agent-exclusions: create <agent-exclusions-create>`

        Args:
            name (str): The name of the exclusion to create.
            scanner_id (int, optional): The scanner id.
            description (str, optional):
                Some further detail about the exclusion.
            start_time (datetime): When the exclusion should start.
            end_time (datetime): When the exclusion should end.
            timezone (str, optional):
                The timezone to use for the exclusion.  The default if none is
                specified is to use UTC.  For the list of usable timezones,
                please refer to:
                https://cloud.tenable.com/api#/resources/scans/timezones
            frequency (str, optional):
                The frequency of the rule. The string inputted will be up-cased.
                Valid values are: ``ONETIME``, ``DAILY``, ``WEEKLY``,
                ``MONTHLY``, ``YEARLY``.
                Default value is ``ONETIME``.
            interval (int, optional):
                The interval of the rule.  The default interval is 1
            weekdays (list, optional):
                List of 2-character representations of the days of the week to
                repeat the frequency rule on.  Valid values are:
                *SU, MO, TU, WE, TH, FR, SA*
                Default values: ``['SU', 'MO', 'TU', 'WE', 'TH', 'FR', 'SA']``
            day_of_month (int, optional):
                The day of the month to repeat a **MONTHLY** frequency rule on.
                The default is today.
            enabled (bool, optional):
                enable/disable exclusion. The default is ``True``

        Returns:
            dict: Dictionary of the newly minted exclusion.

        Examples:
            Creating a one-time exclusion:

            >>> from datetime import datetime, timedelta
            >>> exclusion = tio.agent_exclusions.create(
            ...     'Example One-Time Agent Exclusion',
            ...     ['127.0.0.1'],
            ...     start_time=datetime.utcnow(),
            ...     end_time=datetime.utcnow() + timedelta(hours=1))

            Creating a daily exclusion:

            >>> exclusion = tio.agent_exclusions.create(
            ...     'Example Daily Agent Exclusion',
            ...     ['127.0.0.1'],
            ...     frequency='daily',
            ...     start_time=datetime.utcnow(),
            ...     end_time=datetime.utcnow() + timedelta(hours=1))

            Creating a weekly exclusion:

            >>> exclusion = tio.agent_exclusions.create(
            ...     'Example Weekly Exclusion',
            ...     ['127.0.0.1'],
            ...     frequency='weekly',
            ...     weekdays=['mo', 'we', 'fr'],
            ...     start_time=datetime.utcnow(),
            ...     end_time=datetime.utcnow() + timedelta(hours=1))

            Creating a monthly esxclusion:

            >>> exclusion = tio.agent_exclusions.create(
            ...     'Example Monthly Agent Exclusion',
            ...     ['127.0.0.1'],
            ...     frequency='monthly',
            ...     day_of_month=1,
            ...     start_time=datetime.utcnow(),
            ...     end_time=datetime.utcnow() + timedelta(hours=1))

            Creating a yearly exclusion:

            >>> exclusion = tio.agent_exclusions.create(
            ...     'Example Yearly Agent Exclusion',
            ...     ['127.0.0.1'],
            ...     frequency='yearly',
            ...     start_time=datetime.utcnow(),
            ...     end_time=datetime.utcnow() + timedelta(hours=1))
        '''
        # validate user inputs
        kwargs = self._validate(kwargs)

        # Starting with the innermost part of the payload, lets construct the
        # rrules dictionary.
        frequency = kwargs.get('frequency', 'ONETIME')

        rrules = {
            'freq': frequency,
            'interval': kwargs.get('interval', 1)
        }

        # if the frequency is a weekly one, then we will need to specify the
        # days of the week that the exclusion is run on.
        if frequency == 'WEEKLY':
            rrules['byweekday'] = kwargs.get('weekdays', ['SU', 'MO', 'TU', 'WE', 'TH', 'FR', 'SA'])
            # In the same vein as the frequency check, we're accepting
            # case-insensitive input, comparing it to our known list of
            # acceptable responses, then joining them all together into a
            # comma-separated string.

        # if the frequency is monthly, then we will need to specify the day of
        # the month that the rule will run on.
        if frequency == 'MONTHLY':
            rrules['bymonthday'] = kwargs.get('day_of_month', datetime.today().day)

        # kwargs['enabled'] = kwargs.get('enabled', True)
        # Next we need to construct the rest of the payload
        payload = {
            'name': self._check('name', name, str),
            'description': kwargs.get('description', ''),
            'schedule': {
                'enabled': kwargs.get('enabled', True),
                'starttime': kwargs.get('start_time', datetime.utcnow()).strftime('%Y-%m-%d %H:%M:%S'),
                'endtime': kwargs.get('start_time', (datetime.utcnow() + timedelta(hours=1))).strftime('%Y-%m-%d %H:%M:%S'),
                'timezone': kwargs.get('timezone', 'Etc/UTC'),
                'rrules': rrules
            }
        }

        # Lets check to make sure that the scanner_id is an integer as the API
        # documentation requests and if we don't raise an error, then lets make
        # the call.
        self._check('scanner_id', scanner_id, int)
        return self._api.post(f'{self._path}/{scanner_id}/agents/exclusions', json=payload).json()

    def delete(
            self,
            exclusion_id: int,
            scanner_id: Optional[int] = 1
    ) -> None:
        '''
        Delete an agent exclusion.

        :devportal:`agent-exclusions: delete <agent-exclusions-delete>`

        Args:
            exclusion_id (int): The id of the exclusion object in Tenable.io
            scanner_id (int, optional): The id of the scanner

        Returns:
            None: The Exclusion was successfully deleted

        Examples:
            >>> tio.agent_exclusions.delete(1)
        '''
        self._check('scanner_id', scanner_id, int),
        self._check('exclusion_id', exclusion_id, int)
        self._api.delete(f'{self._path}/{scanner_id}/agents/exclusions/{exclusion_id}')

    def details(
            self,
            exclusion_id: int,
            scanner_id: Optional[int] = 1
    ) -> Dict:
        '''
        Retrieve the details for a specific agent exclusion.

        :devportal:`agent-exclusion: details <agent-exclusions-details>`

        Args:
            exclusion_id (int): The id of the exclusion object in Tenable.io
            scanner_id (int, optional): The id of the scanner

        Returns:
            dict: The exclusion resource dictionary.

        Examples:
            >>> exclusion = tio.agent_exclusions.details(1)
        '''
        self._check('scanner_id', scanner_id, int),
        self._check('exclusion_id', exclusion_id, int)
        return self._api.get(f'{self._path}/{scanner_id}/agents/exclusions/{exclusion_id}').json()

    def edit(
            self,
            exclusion_id: int,
            scanner_id: Optional[int] = 1,
            **kwargs
    ) -> Dict:
        '''
        Edit an existing agent exclusion.

        :devportal:`agent-exclusions: edit <agent-exclusions-edit>`

        The edit function will first gather the details of the exclusion that
        will be edited and will overlay the changes on top.  The result will
        then be pushed back to the API to modify the exclusion.

        Args:
            exclusion_id (int): The id of the exclusion object in Tenable.io
            scanner_id (int, optional): The scanner id.
            name (str, optional): The name of the exclusion to create.
            description (str, optional):
                Some further detail about the exclusion.
            start_time (datetime, optional): When the exclusion should start.
            end_time (datetime, optional): When the exclusion should end.
            timezone (str, optional):
                The timezone to use for the exclusion.  The default if none is
                specified is to use UTC.
            frequency (str, optional):
                The frequency of the rule. The string inputted will be up-cased.
                Valid values are: *ONETIME, DAILY, WEEKLY, MONTHLY, YEARLY*.
            interval (int, optional): The interval of the rule.
            weekdays (list, optional):
                List of 2-character representations of the days of the week to
                repeat the frequency rule on.  Valid values are:
                *SU, MO, TU, WE, TH, FR, SA*
                Default values: ``['SU', 'MO', 'TU', 'WE', 'TH', 'FR', 'SA']``
            day_of_month (int, optional):
                The day of the month to repeat a **MONTHLY** frequency rule on.
            enabled (bool, optional):
                enable/disable exclusion.

        Returns:
            dict: Dictionary of the newly minted exclusion.

        Examples:
            >>> exclusion = tio.agent_exclusions.edit(1, name='New Name')
        '''
        # validate user inputs
        kwargs = self._validate(kwargs)

        # Lets start constructing the payload to be sent to the API...
        payload = self.details(exclusion_id, scanner_id=scanner_id)
        payload['schedule'] = dict_clean(payload['schedule'])

        if kwargs.get('name'):
            payload['name'] = kwargs.get('name')

        if kwargs.get('description'):
            payload['description'] = kwargs.get('description')

        if kwargs.get('enabled'):
            payload['schedule']['enabled'] = kwargs.get('enabled')

        if payload['schedule']['enabled']:
            # we will create a dict of default values from existing payload or
            # set individually if not existing schedule exist
            if payload['schedule'].get('rrules') is not None:
                default_rrule_values = {
                    'frequency': payload['schedule']['rrules'].get('freq'),
                    'interval': payload['schedule']['rrules'].get('interval', 1),
                    'weekdays': payload['schedule']['rrules'].get(
                        'byweekday', ','.join(['SU', 'MO', 'TU', 'WE', 'TH', 'FR', 'SA'])),
                    'day_of_month': payload['schedule']['rrules'].get(
                        'bymonthday', datetime.today().day),
                }
            else:
                default_rrule_values = {
                    'frequency': 'ONETIME',
                    'interval': 1,
                    'weekdays': ','.join(['SU', 'MO', 'TU', 'WE', 'TH', 'FR', 'SA']),
                    'day_of_month': datetime.today().day,
                }

            frequency = kwargs.get('frequency', default_rrule_values.get('frequency'))

            rrules = {
                'freq': frequency,
                'interval': default_rrule_values.get('interval'),
                'byweekday': None,
                'bymonthday': None,
            }

            if frequency == 'WEEKLY':
                rrules['byweekday'] = kwargs.get('weekdays', default_rrule_values.get('weekdays'))
                # In the same vein as the frequency check, we're accepting
                # case-insensitive input, comparing it to our known list of
                # acceptable responses, then joining them all together into a
                # comma-separated string.

            if frequency == 'MONTHLY':
                rrules['bymonthday'] = kwargs.get(
                    'day_of_month', default_rrule_values.get('day_of_month'))

            # update new rrules in existing payload
            dict_merge(payload['schedule']['rrules'], rrules)
            # remove null values from payload
            payload = dict_clean(payload)

            if kwargs.get('start_time'):
                payload['schedule']['starttime'] = kwargs.get('start_time').strftime('%Y-%m-%d %H:%M:%S')

            if kwargs.get('end_time'):
                payload['schedule']['endtime'] = kwargs.get('end_time').strftime('%Y-%m-%d %H:%M:%S')

            if kwargs.get('interval'):
                payload['schedule']['rrules']['interval'] = kwargs.get('interval')

            if kwargs.get('timezone'):
                payload['schedule']['timezone'] = kwargs.get(
                    'timezone', payload['schedule'].get('timezone'))

        # Lets check to make sure that the scanner_id  and exclusion_id are
        # integers as the API documentation requests and if we don't raise an
        # error, then lets make the call.
        self._check('scanner_id', scanner_id, int),
        self._check('exclusion_id', exclusion_id, int)
        return self._api.put(f'{self._path}/{scanner_id}/agents/exclusions/{exclusion_id}', json=payload).json()

    def list(
            self,
            scanner_id: Optional[int] = 1
    ) -> List[Dict]:
        '''
        Lists all of the currently configured agent exclusions.

        :devportal:`agent-exclusions: list <agent-exclusions-list>`

        Args:
            scanner_id (int, optional): The scanner identifier to be used.

        Returns:
            list: List of agent exclusions.

        Examples:
            >>> for exclusion in tio.agent_exclusions.list():
            ...     pprint(exclusion)
        '''
        self._check('scanner_id', scanner_id, int)
        return self._api.get(f'{self._path}/{scanner_id}/agents/exclusions').json()['exclusions']
