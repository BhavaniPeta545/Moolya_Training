*** Settings ***
Resource        Resources.robot
Resource    ../robot_juno_project-main/Resources/Juno_Common_Keywords.robot

*** Keywords ***
Click the Element
    [Arguments]     ${element1}      
    Wait Until Element Is Visible    ${element1}
    Click Element    ${element1}

Is Element Visible
    [Arguments]     ${element}
    Element Should Be Visible    ${element}

Waiting_Time
    [Arguments]     ${element}
    Sleep    ${element}

Enter the data
    [Arguments]     ${element}  ${data}
    Input Text    ${element}    ${data}
