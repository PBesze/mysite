*** Settings ***
Library  SeleniumLibrary

*** Variables ***


*** Test Cases ***
Főoldal - Belépés Google.com
    [Documentation]  Open Google
    [Tags]  Smoke
    Open Browser  https://www.google.com  chrome

    Close Browser

*** Keywords ***
