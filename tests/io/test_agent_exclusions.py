'''
test agent exclusions
'''
import uuid
from datetime import datetime as dtime, timedelta
import pytest
from marshmallow import ValidationError
from tenable.errors import NotFoundError, PermissionError
from tests.pytenable_log_handler import log_exception
from ..checker import check


@pytest.fixture
@pytest.mark.vcr()
def agentexclusion(request, api):
    '''
    agent exclusion fixture
    '''
    excl = api.agent_exclusions.create(str(uuid.uuid4()),
                                       start_time=dtime.utcnow(),
                                       end_time=dtime.utcnow() + timedelta(hours=1))

    def teardown():
        try:
            api.agent_exclusions.delete(excl['id'])
        except NotFoundError as error:
            log_exception(error)

    request.addfinalizer(teardown)
    return excl


@pytest.mark.vcr()
def test_agentexclusions_create_scanner_id_typeerror(api):
    '''
    test to raise the exception while creating the exclusion when type of
    scanner_id is not passed as defined
    '''
    with pytest.raises(TypeError):
        api.agent_exclusions.create(str(uuid.uuid4()),
                                    scanner_id='nope',
                                    start_time=dtime.utcnow(),
                                    end_time=dtime.utcnow() + timedelta(hours=1))


@pytest.mark.vcr()
def test_agentexclusions_create_name_typeerror(api):
    '''
    test to raise the exception while creating the exclusion when type of
    name is not passed as defined
    '''
    with pytest.raises(TypeError):
        api.agent_exclusions.create(1.02,
                                    start_time=dtime.utcnow(),
                                    end_time=dtime.utcnow() + timedelta(hours=1))


@pytest.mark.vcr()
def test_agentexclusions_create_starttime_type_validationerror(api):
    '''
    test to raise the exception while creating the exclusion when type of
    starttime is not passed as defined
    '''
    with pytest.raises(ValidationError):
        api.agent_exclusions.create(str(uuid.uuid4()),
                                    start_time='fail',
                                    end_time=dtime.utcnow() + timedelta(hours=1))


@pytest.mark.vcr()
def test_agentexclusions_create_endtime_type_validationerror(api):
    '''
    test to raise the exception while creating the exclusion when type of
    endtime is not passed as defined
    '''
    with pytest.raises(ValidationError):
        api.agent_exclusions.create(str(uuid.uuid4()),
                                    start_time=dtime.utcnow(),
                                    end_time='nope')


@pytest.mark.vcr()
def test_agentexclusions_create_timezone_type_validationerror(api):
    '''
    test to raise the exception while creating the exclusion when type of
    timezone is not passed as defined
    '''
    with pytest.raises(ValidationError):
        api.agent_exclusions.create(str(uuid.uuid4()),
                                    timezone=1,
                                    start_time=dtime.utcnow(),
                                    end_time=dtime.utcnow() + timedelta(hours=1))


@pytest.mark.vcr()
def test_agentexclusions_create_description_type_validationerrorr(api):
    '''
    test to raise the exception while creating the exclusion when type of
    description is not passed as defined
    '''
    with pytest.raises(ValidationError):
        api.agent_exclusions.create(str(uuid.uuid4()),
                                    description=True,
                                    start_time=dtime.utcnow(),
                                    end_time=dtime.utcnow() + timedelta(hours=1))


@pytest.mark.vcr()
def test_agentexclusions_create_frequency_type_validationerror(api):
    '''
    test to raise the exception while creating the exclusion when type of
    frequency is not passed as defined
    '''
    with pytest.raises(ValidationError):
        api.agent_exclusions.create(str(uuid.uuid4()),
                                    frequency=True,
                                    start_time=dtime.utcnow(),
                                    end_time=dtime.utcnow() + timedelta(hours=1))


@pytest.mark.vcr()
def test_agentexclusions_create_frequency_value_validationerror(api):
    '''
    test to raise the exception while creating the exclusion when value of
    frequency is not passed as defined
    '''
    with pytest.raises(ValidationError):
        api.agent_exclusions.create(str(uuid.uuid4()),
                                    frequency='nope',
                                    start_time=dtime.utcnow(),
                                    end_time=dtime.utcnow() + timedelta(hours=1))


@pytest.mark.vcr()
def test_agentexclusions_create_interval_type_validationerror(api):
    '''
    test to raise the exception while creating the exclusion when type of
    interval is not passed as defined
    '''
    with pytest.raises(ValidationError):
        api.agent_exclusions.create(str(uuid.uuid4()),
                                    interval='nope',
                                    start_time=dtime.utcnow(),
                                    end_time=dtime.utcnow() + timedelta(hours=1))


@pytest.mark.vcr()
def test_agentexclusions_create_weekdays_type_validationerror(api):
    '''
    test to raise the exception while creating the exclusion when type of
    weekdays is not passed as defined
    '''
    with pytest.raises(ValidationError):
        api.agent_exclusions.create(str(uuid.uuid4()),
                                    weekdays='nope',
                                    frequency='weekly',
                                    start_time=dtime.utcnow(),
                                    end_time=dtime.utcnow() + timedelta(hours=1))


@pytest.mark.vcr()
def test_agentexclusions_create_weekdays_value_validationerror(api):
    '''
    test to raise the exception while creating the exclusion when value of
    weekdays is not passed as defined
    '''
    with pytest.raises(ValidationError):
        api.agent_exclusions.create(str(uuid.uuid4()),
                                    weekdays=['MO', 'TU', 'nope'],
                                    frequency='weekly',
                                    start_time=dtime.utcnow(),
                                    end_time=dtime.utcnow() + timedelta(hours=1))


@pytest.mark.vcr()
def test_agentexclusions_create_dayofmonth_type_validationerrorr(api):
    '''
    test to raise the exception while creating the exclusion when type of
    day of month is not passed as defined
    '''
    with pytest.raises(ValidationError):
        api.agent_exclusions.create(str(uuid.uuid4()),
                                    day_of_month='nope',
                                    frequency='monthly',
                                    start_time=dtime.utcnow(),
                                    end_time=dtime.utcnow() + timedelta(hours=1))


@pytest.mark.vcr()
def test_agentexclusions_create_dayofmonth_value_validationerror(api):
    '''
    test to raise the exception while creating the exclusion when value of
    day of month is not passed as defined
    '''
    with pytest.raises(ValidationError):
        api.agent_exclusions.create(str(uuid.uuid4()),
                                    day_of_month=0,
                                    frequency='monthly',
                                    start_time=dtime.utcnow(),
                                    end_time=dtime.utcnow() + timedelta(hours=1))


@pytest.mark.vcr()
def test_agentexclusions_create_onetime_exclusion(api):
    '''
        test to create one time exclusion
    '''
    resp = api.agent_exclusions.create(str(uuid.uuid4()),
                                       start_time=dtime.utcnow(),
                                       end_time=dtime.utcnow() + timedelta(hours=1))
    assert isinstance(resp, dict)
    check(resp, 'id', int)
    check(resp, 'name', str)
    check(resp, 'description', str, allow_none=True)
    check(resp, 'last_modification_date', int)
    check(resp, 'schedule', dict)
    check(resp['schedule'], 'enabled', bool)
    check(resp['schedule'], 'starttime', 'datetime')
    check(resp['schedule'], 'endtime', 'datetime')
    check(resp['schedule'], 'timezone', str)
    check(resp['schedule']['rrules'], 'freq', str)
    check(resp['schedule']['rrules'], 'interval', str)
    api.agent_exclusions.delete(resp['id'])


@pytest.mark.vcr()
def test_agentexclusions_create_daily_exclusion(api):
    '''
        test to create daily exclusion
    '''
    resp = api.agent_exclusions.create(str(uuid.uuid4()),
                                       start_time=dtime.utcnow(),
                                       end_time=dtime.utcnow() + timedelta(hours=1),
                                       frequency='daily')
    assert isinstance(resp, dict)
    check(resp, 'id', int)
    check(resp, 'name', str)
    check(resp, 'description', str, allow_none=True)
    check(resp, 'last_modification_date', int)
    check(resp, 'schedule', dict)
    check(resp['schedule'], 'enabled', bool)
    check(resp['schedule'], 'starttime', 'datetime')
    check(resp['schedule'], 'endtime', 'datetime')
    check(resp['schedule'], 'timezone', str)
    check(resp['schedule']['rrules'], 'freq', str)
    check(resp['schedule']['rrules'], 'interval', str)
    api.agent_exclusions.delete(resp['id'])


@pytest.mark.vcr()
def test_agentexclusions_create_weekly_exclusion(api):
    '''
        test to create weekly exclusion

    '''
    resp = api.agent_exclusions.create(str(uuid.uuid4()),
                                       start_time=dtime.utcnow(),
                                       end_time=dtime.utcnow() + timedelta(hours=1),
                                       frequency='weekly',
                                       weekdays=['mo', 'we', 'fr'])
    assert isinstance(resp, dict)
    check(resp, 'id', int)
    check(resp, 'name', str)
    check(resp, 'description', str, allow_none=True)
    check(resp, 'last_modification_date', int)
    check(resp, 'schedule', dict)
    check(resp['schedule'], 'enabled', bool)
    check(resp['schedule'], 'starttime', 'datetime')
    check(resp['schedule'], 'endtime', 'datetime')
    check(resp['schedule'], 'timezone', str)
    check(resp['schedule']['rrules'], 'freq', str)
    check(resp['schedule']['rrules'], 'interval', str)
    check(resp['schedule']['rrules'], 'byweekday', str)
    api.agent_exclusions.delete(resp['id'])


@pytest.mark.vcr()
def test_agentexclusions_create_monthly_exclusion(api):
    '''
        test to create monthly exclusion
    '''
    resp = api.agent_exclusions.create(str(uuid.uuid4()),
                                       start_time=dtime.utcnow(),
                                       end_time=dtime.utcnow() + timedelta(hours=1),
                                       frequency='monthly',
                                       day_of_month=15)
    assert isinstance(resp, dict)
    check(resp, 'id', int)
    check(resp, 'name', str)
    check(resp, 'description', str, allow_none=True)
    check(resp, 'last_modification_date', int)
    check(resp, 'schedule', dict)
    check(resp['schedule'], 'enabled', bool)
    check(resp['schedule'], 'starttime', 'datetime')
    check(resp['schedule'], 'endtime', 'datetime')
    check(resp['schedule'], 'timezone', str)
    check(resp['schedule']['rrules'], 'freq', str)
    check(resp['schedule']['rrules'], 'interval', str)
    check(resp['schedule']['rrules'], 'bymonthday', str)
    api.agent_exclusions.delete(resp['id'])


@pytest.mark.vcr()
def test_agentexclusions_create_yearly_exclusion(api):
    '''
    test to create yearly exclusion
    '''
    resp = api.agent_exclusions.create(str(uuid.uuid4()),
                                       start_time=dtime.utcnow(),
                                       end_time=dtime.utcnow() + timedelta(hours=1),
                                       frequency='yearly')
    assert isinstance(resp, dict)
    check(resp, 'id', int)
    check(resp, 'name', str)
    check(resp, 'description', str, allow_none=True)
    check(resp, 'last_modification_date', int)
    check(resp, 'schedule', dict)
    check(resp['schedule'], 'enabled', bool)
    check(resp['schedule'], 'starttime', 'datetime')
    check(resp['schedule'], 'endtime', 'datetime')
    check(resp['schedule'], 'timezone', str)
    check(resp['schedule']['rrules'], 'freq', str)
    check(resp['schedule']['rrules'], 'interval', str)
    api.agent_exclusions.delete(resp['id'])


@pytest.mark.vcr()
def test_agentexclusions_create_enabled_false_exclusion(api):
    '''
    test to create exclusion when it is disabled
    '''
    resp = api.agent_exclusions.create(str(uuid.uuid4()),
                                       enabled=False)
    assert isinstance(resp, dict)
    check(resp, 'id', int)
    check(resp, 'name', str)
    check(resp, 'description', str, allow_none=True)
    check(resp, 'last_modification_date', int)
    check(resp, 'schedule', dict)
    check(resp['schedule'], 'enabled', bool)
    check(resp['schedule'], 'starttime', 'datetime')
    check(resp['schedule'], 'endtime', 'datetime')
    check(resp['schedule'], 'timezone', str)
    check(resp['schedule']['rrules'], 'freq', str)
    check(resp['schedule']['rrules'], 'interval', str)
    assert resp['schedule']['enabled'] is False
    api.agent_exclusions.delete(resp['id'])


@pytest.mark.vcr()
def test_agentexclusions_create_standard_users_cant_create(stdapi):
    '''
    test to raise the exception when user try to create the exclusion
    '''
    with pytest.raises(PermissionError):
        stdapi.agent_exclusions.create(str(uuid.uuid4()),
                                       start_time=dtime.utcnow(),
                                       end_time=dtime.utcnow() + timedelta(hours=1))


@pytest.mark.vcr()
def test_agentexclusions_delete_notfounderror(api):
    '''
    test to raise the exception when id not found to perform the deletion
    '''
    with pytest.raises(NotFoundError):
        api.agent_exclusions.delete(123)


@pytest.mark.vcr()
def test_agentexclusions_delete_exclusion(api, agentexclusion):
    '''
    test to delete the agent exclusion
    '''
    api.agent_exclusions.delete(agentexclusion['id'])


@pytest.mark.vcr()
def test_agentexclusions_delete_standard_user_fail(stdapi, agentexclusion):
    '''
    test to raise the exception when failed to delete the agent exclusion
    '''
    with pytest.raises(PermissionError):
        stdapi.agent_exclusions.delete(agentexclusion['id'])


@pytest.mark.vcr()
def test_agentexclusions_edit_no_exclusion_id_typeerror(api):
    '''
    test to raise the exception when nothing is passed
    '''
    with pytest.raises(TypeError):
        api.agent_exclusions.edit()


@pytest.mark.vcr()
def test_agentexclusions_edit_exclusion_id_typeerror(api):
    '''
    test to raise the exception when expected type of exclusion_id is not passed
    '''
    with pytest.raises(TypeError):
        api.agent_exclusions.edit('nope')


@pytest.mark.vcr()
def test_agentexclusions_edit_scanner_id_typeerror(api, agentexclusion):
    '''
    test to raise the exception when expected type of scanner_id is not passed
    '''
    with pytest.raises(TypeError):
        api.agent_exclusions.edit(agentexclusion['id'], scanner_id='nope')


@pytest.mark.vcr()
def test_agentexclusions_edit_name_type_validationerror(api, agentexclusion):
    '''
    test to raise the exception when expected type of name is not passed
    '''
    with pytest.raises(ValidationError):
        api.agent_exclusions.edit(agentexclusion['id'], name=1.02)


@pytest.mark.vcr()
def test_agentexclusions_edit_starttime_type_validationerror(api, agentexclusion):
    '''
    test to raise the exception when expected type of starttime is not passed
    '''
    with pytest.raises(ValidationError):
        api.agent_exclusions.edit(agentexclusion['id'], start_time='nope')


@pytest.mark.vcr()
def test_agentexclusions_edit_timezone_type_validationerror(api, agentexclusion):
    '''
    test to raise the exception when expected type of timezone is not passed
    '''
    with pytest.raises(ValidationError):
        api.agent_exclusions.edit(agentexclusion['id'], timezone=1)


@pytest.mark.vcr()
def test_agentexclusions_edit_description_type_validationerror(api, agentexclusion):
    '''
    test to raise the exception when expected type of description is not passed
    '''
    with pytest.raises(ValidationError):
        api.agent_exclusions.edit(agentexclusion['id'], description=1)


@pytest.mark.vcr()
def test_agentexclusions_edit_frequency_type_validationerror(api, agentexclusion):
    '''
    test to raise the exception when expected type of frequency is not passed
    '''
    with pytest.raises(ValidationError):
        api.agent_exclusions.edit(agentexclusion['id'], frequency=1)


@pytest.mark.vcr()
def test_agentexclusions_edit_frequency_value_validationerror(api, agentexclusion):
    '''
    test to raise the exception when expected value of frequency is not passed
    '''
    with pytest.raises(ValidationError):
        api.agent_exclusions.edit(agentexclusion['id'], frequency='nope')


@pytest.mark.vcr()
def test_agentexclusions_edit_interval_type_validationerror(api, agentexclusion):
    '''
    test to raise the exception when expected type of interval is not passed
    '''
    with pytest.raises(ValidationError):
        api.agent_exclusions.edit(agentexclusion['id'], interval='nope')


@pytest.mark.vcr()
def test_agentexclusions_edit_weekdays_type_validationerror(api, agentexclusion):
    '''
    test to raise the exception when expected type of weekdays is not passed
    '''
    with pytest.raises(ValidationError):
        api.agent_exclusions.edit(agentexclusion['id'], frequency='weekly', weekdays='nope')


@pytest.mark.vcr()
def test_agentexclusions_edit_weekdays_value_validationerror(api, agentexclusion):
    '''
    test to raise the exception when expected value of weekdays is not passed
    '''
    with pytest.raises(ValidationError):
        api.agent_exclusions.edit(agentexclusion['id'],
                                  frequency='weekly',
                                  weekdays=['MO', 'WE', 'nope'])


@pytest.mark.vcr()
def test_agentexclusions_edit_dayofmonth_type_validationerror(api, agentexclusion):
    '''
    test to raise the exception when expected type of day of month is not passed
    '''
    with pytest.raises(ValidationError):
        api.agent_exclusions.edit(agentexclusion['id'], frequency='monthly', day_of_month='nope')


@pytest.mark.vcr()
def test_agentexclusions_edit_dayofmonth_value_validationerror(api, agentexclusion):
    '''
    test to raise the exception when expected value of day of month is not passed
    '''
    with pytest.raises(ValidationError):
        api.agent_exclusions.edit(agentexclusion['id'], frequency='monthly', day_of_month=0)


@pytest.mark.vcr()
def test_agentexclusions_edit_standard_user_permission_error(stdapi, agentexclusion):
    '''
    test to raise the exception when there is no permission to edit the agent exclusion
    '''
    with pytest.raises(PermissionError):
        stdapi.agent_exclusions.edit(agentexclusion['id'], name=str(uuid.uuid4()))


@pytest.mark.vcr()
def test_agentexclusions_edit_success(api, agentexclusion):
    '''
    test to edit the exclusion
    '''
    api.agent_exclusions.edit(agentexclusion['id'], name=str(uuid.uuid4()))


@pytest.mark.vcr()
def test_agentexclusions_edit_freq_onetime_to_daily(api, agentexclusion):
    '''
    test to edit the exclusion by enabling exclusion daily
    '''
    resp = api.agent_exclusions.edit(agentexclusion['id'], name=str(uuid.uuid4()),
                                     frequency='daily',
                                     interval=2)

    assert isinstance(resp, dict)
    check(resp, 'description', str, allow_none=True)
    check(resp, 'id', int)
    check(resp, 'last_modification_date', int)
    check(resp, 'name', str)
    check(resp, 'schedule', dict)
    check(resp['schedule'], 'enabled', bool)
    check(resp['schedule'], 'endtime', 'datetime')
    check(resp['schedule'], 'rrules', dict)
    check(resp['schedule']['rrules'], 'freq', str)
    check(resp['schedule']['rrules'], 'interval', str)
    check(resp['schedule'], 'starttime', 'datetime')
    check(resp['schedule'], 'timezone', str)
    assert resp['schedule']['rrules']['freq'] == 'DAILY'
    assert resp['schedule']['rrules']['interval'] == '2'


@pytest.mark.vcr()
def test_agentexclusions_edit_enable_exclusion(api):
    '''
        test to check the exclusion by enabling exclusion

    '''
    agentexclusion = api.agent_exclusions.create(str(uuid.uuid4()), enabled=False)
    resp = api.agent_exclusions.edit(agentexclusion['id'], enabled=True,
                                     start_time=dtime.utcnow(),
                                     end_time=dtime.utcnow() + timedelta(hours=1))
    check(resp, 'id', int)
    check(resp, 'name', str)
    check(resp, 'description', str, allow_none=True)
    check(resp, 'last_modification_date', int)
    check(resp, 'schedule', dict)
    check(resp['schedule'], 'enabled', bool)
    check(resp['schedule'], 'starttime', 'datetime')
    check(resp['schedule'], 'endtime', 'datetime')
    check(resp['schedule'], 'timezone', str)
    check(resp['schedule']['rrules'], 'freq', str)
    check(resp['schedule']['rrules'], 'interval', str)
    assert resp['schedule']['enabled'] is True
    api.agent_exclusions.delete(resp['id'])


@pytest.mark.vcr()
def test_agentexclusions_edit_onetime_to_weekly_valdefault(api, agentexclusion):
    '''
        test to check the exclusion weekly
    '''
    resp = api.agent_exclusions.edit(agentexclusion['id'],
                                     frequency='Weekly')
    check(resp, 'id', int)
    check(resp, 'name', str)
    check(resp, 'description', str, allow_none=True)
    check(resp, 'last_modification_date', int)
    check(resp, 'schedule', dict)
    check(resp['schedule'], 'enabled', bool)
    check(resp['schedule'], 'starttime', 'datetime')
    check(resp['schedule'], 'endtime', 'datetime')
    check(resp['schedule'], 'timezone', str)
    check(resp['schedule']['rrules'], 'freq', str)
    check(resp['schedule']['rrules'], 'interval', str)
    assert resp['schedule']['rrules']['byweekday'] == 'SU,MO,TU,WE,TH,FR,SA'


@pytest.mark.vcr()
def test_agentexclusions_edit_onetime_to_weekly_valassigned(api, agentexclusion):
    '''
        test to check the exclusion weekly

    '''
    resp = api.agent_exclusions.edit(agentexclusion['id'],
                                     frequency='Weekly',
                                     weekdays=['MO', 'TU'])
    check(resp, 'id', int)
    check(resp, 'name', str)
    check(resp, 'description', str, allow_none=True)
    check(resp, 'last_modification_date', int)
    check(resp, 'schedule', dict)
    check(resp['schedule'], 'enabled', bool)
    check(resp['schedule'], 'starttime', 'datetime')
    check(resp['schedule'], 'endtime', 'datetime')
    check(resp['schedule'], 'timezone', str)
    check(resp['schedule']['rrules'], 'freq', str)
    check(resp['schedule']['rrules'], 'interval', str)
    assert resp['schedule']['rrules']['byweekday'] == 'MO,TU'


@pytest.mark.vcr()
def test_agentexclusions_edit_onetime_to_weekly_valavailable(api):
    '''
        test to check the exclusion weekly

    '''
    agentexclusion = api.agent_exclusions.create(str(uuid.uuid4()),
                                                 frequency='Weekly',
                                                 weekdays=['TU', 'WE'],
                                                 start_time=dtime.utcnow(),
                                                 end_time=dtime.utcnow() + timedelta(hours=1))
    resp = api.agent_exclusions.edit(agentexclusion['id'], name=str(uuid.uuid4()))
    check(resp, 'id', int)
    check(resp, 'name', str)
    check(resp, 'description', str, allow_none=True)
    check(resp, 'last_modification_date', int)
    check(resp, 'schedule', dict)
    check(resp['schedule'], 'enabled', bool)
    check(resp['schedule'], 'starttime', 'datetime')
    check(resp['schedule'], 'endtime', 'datetime')
    check(resp['schedule'], 'timezone', str)
    check(resp['schedule']['rrules'], 'freq', str)
    check(resp['schedule']['rrules'], 'interval', str)
    assert resp['schedule']['rrules']['byweekday'] == 'TU,WE'


@pytest.mark.vcr()
def test_agentexclusions_edit_freq_onetime_to_monthly_valddefault(api, agentexclusion):
    '''
        test to check the exclusion monthly

    '''
    resp = api.agent_exclusions.edit(agentexclusion['id'], name=str(uuid.uuid4()),
                                     frequency='monthly',
                                     interval=2)
    assert isinstance(resp, dict)
    check(resp, 'description', str, allow_none=True)
    check(resp, 'id', int)
    check(resp, 'last_modification_date', int)
    check(resp, 'name', str)
    check(resp, 'schedule', dict)
    check(resp['schedule'], 'enabled', bool)
    check(resp['schedule'], 'endtime', 'datetime')
    check(resp['schedule'], 'rrules', dict)
    check(resp['schedule']['rrules'], 'freq', str)
    check(resp['schedule']['rrules'], 'interval', str)
    check(resp['schedule'], 'starttime', 'datetime')
    check(resp['schedule'], 'timezone', str)
    assert resp['schedule']['rrules']['freq'] == 'MONTHLY'
    assert resp['schedule']['rrules']['interval'] == '2'


@pytest.mark.vcr()
def test_agentexclusions_edit_freq_onetime_to_monthly_valassigned(api, agentexclusion):
    '''
        test to check the exclusion monthly

    '''
    resp = api.agent_exclusions.edit(agentexclusion['id'], name=str(uuid.uuid4()),
                                     frequency='monthly',
                                     interval=2,
                                     day_of_month=8)
    assert isinstance(resp, dict)
    check(resp, 'description', str, allow_none=True)
    check(resp, 'id', int)
    check(resp, 'last_modification_date', int)
    check(resp, 'name', str)
    check(resp, 'schedule', dict)
    check(resp['schedule'], 'enabled', bool)
    check(resp['schedule'], 'endtime', 'datetime')
    check(resp['schedule'], 'rrules', dict)
    check(resp['schedule']['rrules'], 'freq', str)
    check(resp['schedule']['rrules'], 'interval', str)
    check(resp['schedule'], 'starttime', 'datetime')
    check(resp['schedule'], 'timezone', str)
    assert resp['schedule']['rrules']['freq'] == 'MONTHLY'
    assert resp['schedule']['rrules']['interval'] == '2'
    assert resp['schedule']['rrules']['bymonthday'] == '8'


@pytest.mark.vcr()
def test_agentexclusions_edit_freq_onetime_to_monthly_valavailable(api):
    '''
        test to check the exclusion monthly

    '''
    agentexclusion = api.agent_exclusions.create(str(uuid.uuid4()),
                                                 start_time=dtime.utcnow(),
                                                 end_time=dtime.utcnow() + timedelta(hours=1),
                                                 frequency='monthly', day_of_month=8)
    resp = api.agent_exclusions.edit(agentexclusion['id'],
                                     frequency='monthly',
                                     interval=2)
    assert isinstance(resp, dict)
    check(resp, 'description', str, allow_none=True)
    check(resp, 'id', int)
    check(resp, 'last_modification_date', int)
    check(resp, 'name', str)
    check(resp, 'schedule', dict)
    check(resp['schedule'], 'enabled', bool)
    check(resp['schedule'], 'endtime', 'datetime')
    check(resp['schedule'], 'rrules', dict)
    check(resp['schedule']['rrules'], 'freq', str)
    check(resp['schedule']['rrules'], 'interval', str)
    check(resp['schedule'], 'starttime', 'datetime')
    check(resp['schedule'], 'timezone', str)
    assert resp['schedule']['rrules']['freq'] == 'MONTHLY'
    assert resp['schedule']['rrules']['interval'] == '2'
    assert resp['schedule']['rrules']['bymonthday'] == '8'
    api.agent_exclusions.delete(resp['id'])


@pytest.mark.vcr()
def test_agentexclusions_edit_freq_onetime_to_yearly(api, agentexclusion):
    '''
    test to check the exclusion yearly
    '''
    resp = api.agent_exclusions.edit(agentexclusion['id'], name=str(uuid.uuid4()),
                                     frequency='yearly',
                                     interval=2)
    assert isinstance(resp, dict)
    check(resp, 'description', str, allow_none=True)
    check(resp, 'id', int)
    check(resp, 'last_modification_date', int)
    check(resp, 'name', str)
    check(resp, 'schedule', dict)
    check(resp['schedule'], 'enabled', bool)
    check(resp['schedule'], 'endtime', 'datetime')
    check(resp['schedule'], 'rrules', dict)
    check(resp['schedule']['rrules'], 'freq', str)
    check(resp['schedule']['rrules'], 'interval', str)
    check(resp['schedule'], 'starttime', 'datetime')
    check(resp['schedule'], 'timezone', str)
    assert resp['schedule']['rrules']['freq'] == 'YEARLY'
    assert resp['schedule']['rrules']['interval'] == '2'


@pytest.mark.vcr()
def test_agentexclusions_list_blackouts(api):
    '''
    test to list the blackouts
    '''
    items = api.agent_exclusions.list()
    assert isinstance(items, list)
