*** Settings ***
Library     AppiumLibrary

*** Test Cases ***
Open Application
    Open Application    http://localhost:4723/wd/hub    deviceName=Bhavani      platformName=Android        appPackage=com.android.calculator2      appActivity=com.android.calculator2.Calculator

adding
    Click Element    	id=com.android.calculator2:id/digit_1
    Click Element    id=com.android.calculator2:id/op_add
    Click Element    id=com.android.calculator2:id/digit_9
    Press Keycode    161
    Sleep    10
    
subtract
    Click Element    com.android.calculator2:id/digit_9
    Click Element    com.android.calculator2:id/digit_8
    Click Element    com.android.calculator2:id/op_sub
    Click Element    com.android.calculator2:id/digit_6
    Press Keycode    161
    Sleep    10

#closing application
#    Close Application