*** Settings ***
Library    RPA.Browser.Playwright

*** Variables ***
${btnHome}    (//span[text()="หน้าแรก"])[2]
${COMMENTS}=    ['comment1','comment2','comment3','comment4']

*** Test Cases ***
test pantip
    Open and get comments from pantip 

*** Keywords ***
Open and get comments from pantip

    #Open Browser
    Open Browser    url=http://pantip.com/topic/41780470    browser=chromium
    

    #Wait for comments visible then log to console
    # FOR    ${comment}    IN    ${COMMENTS}
    #     Wait For Elements State    xpath=//span[@id=${comment}]    visible
    #     ${text}=    Get Text    xpath=//span[@id=${comment}]
    #     Log To Console   ${text}
    #     Sleep    2
    # END

    Wait For Elements State    xpath=//span[@id='comment1']    visible
    ${text1}=    Get Text    xpath=//span[@id='comment1']
    Log To Console   ${text1}
    Sleep    1
    Wait For Elements State    xpath=//span[@id='comment2']    visible
    ${text2}=    Get Text    xpath=//span[@id='comment2']
    Log To Console   ${text2}
    Sleep    1
    Wait For Elements State    xpath=//span[@id='comment3']    visible
    ${text3}=    Get Text    xpath=//span[@id='comment3']
    Log To Console   ${text3}
    Sleep    1
    Wait For Elements State    xpath=//span[@id='comment4']    visible
    ${text4}=    Get Text    xpath=//span[@id='comment4']
    Log To Console   ${text4}
    Sleep    1
    Close Browser