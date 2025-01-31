import json

from storyhub.sdk.service.Contact import Contact
from tests.storyhub.sdk.JsonFixtureHelper import JsonFixtureHelper

contact_fixture = JsonFixtureHelper.load_fixture("contact_fixture")

contact_fixture_json = json.dumps(contact_fixture)


def test_deserialization(mocker):

    mocker.patch.object(json, 'loads', return_value=contact_fixture)

    assert Contact.from_json(jsonstr=contact_fixture_json) is not None

    json.loads.assert_called_with(contact_fixture_json)


def test_serialization(mocker):

    mocker.patch.object(json, 'dumps', return_value=contact_fixture_json)

    service_command = Contact.from_dict(data=contact_fixture)

    assert service_command.as_json(compact=True) is not None
    json.dumps.assert_called_with(contact_fixture, sort_keys=True)

    assert service_command.as_json() is not None
    json.dumps.assert_called_with(contact_fixture, indent=4, sort_keys=True)

