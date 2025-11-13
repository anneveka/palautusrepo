*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  koiras  koira123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  kukka  kukka888
    Input Credentials  kukka  kuu3344r
    Output Should Contain  User with username kukka already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kukkkuuu2
    Output Should Contain  Virheellinen käyttäjänimi

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  Kalle  kallukka2
    Output Should Contain  Virheellinen käyttäjänimi

Register With Valid Username And Too Short Password
    Input Credentials  nalle  noksu
    Output Should Contain  Virheellinen salasana

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  nallukka  hunajaanam
    Output Should Contain  Virheellinen salasana

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123