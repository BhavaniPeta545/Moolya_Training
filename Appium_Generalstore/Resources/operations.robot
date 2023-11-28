*** Settings ***
Resource       Resources.robot

*** Keywords ***
Opening Application
    Open Application    ${url}    deviceName=${devicename}      platformName=${platformname}        appPackage=${apppackage}       appActivity=${appactivity}
    Waiting_Time    5s
Select the country
    Click the Element       ${country}
    Tap With Positions
    Waiting_Time    5s
    Is Element Visible    ${countryframe}
    Swipe until Element found    ${element_visible}
Select gender
    Is Element Visible    ${radiofemale}
    Click the Element    ${radiofemale}
Provide the name
    Click the Element       ${input_text}
    Enter the data    ${input_text}    Harish
    Waiting_Time    5
    Hide Keyboard
Lets shop
    Click the Element    ${letsshop_button}
    Waiting_Time    5
    Is Element Visible    ${products_list}

Addtocart
#    Swipe    499    1948    475    318
#    Text Should Be Visible    Converse All Star
##    ${index}=    Get Element Attribute    ${shoe}    index
##    Log    ${index}
#    Click the Element    ${add_to_cart}
    Swipe until shoe found    ${product}
    Click the Element     ${cart_btn}
    Waiting_Time    5
Proceed
   Click Text    ${checkbox_text}
   Long Press    com.androidsample.generalstore:id/termsButton
   Waiting_Time    5s
   Click Element    id=android:id/button1
   Click the Element    ${proceed_btn}
   Waiting_Time    5
Swipe until Element found
    [Arguments]     ${element_visible}
    ${index}    Evaluate    1
    ${i}    Evaluate    1
    WHILE    ${i}>0
        ${LIST_ELEMENTS}    get webelements    xpath=//android.widget.TextView
        log to console    ${LIST_ELEMENTS}
        ${LIST_LENGTH}    get length        ${LIST_ELEMENTS}
        log to console    ${LIST_LENGTH}
#        ${country}      get element attribute    ${LIST_ELEMENTS}[${index}]    text
#        ${index}   evaluate    ${index}+1
      FOR    ${elem}      IN      @{LIST_ELEMENTS}
        ${country}      get element attribute    ${elem}    text
        log to console    ${country}
        IF      "${country}" == "${element_visible}"
            log to console    ${country}
            click element    ${elem}
            ${i}   evaluate    ${i}-1
            BREAK
        END
      END
      Swipe    789    2088    178    595
      SLEEP    5s
    END

Swipe until shoe found
    [Arguments]     ${product}
    ${index}    Evaluate    1
    ${i}    Evaluate    1
    WHILE    ${i}>0
        ${LIST_ELEMENTS}    get webelements    id=com.androidsample.generalstore:id/productName
        log to console    ${LIST_ELEMENTS}
        ${LIST_LENGTH}    get length        ${LIST_ELEMENTS}
        log to console    ${LIST_LENGTH}
#        ${country}      get element attribute    ${LIST_ELEMENTS}[${index}]    text
#        ${index}   evaluate    ${index}+1
      FOR    ${elem}      IN      @{LIST_ELEMENTS}
        ${shoe_prod}      get element attribute    ${elem}    text
        log to console    ${shoe_prod}
        IF      "${shoe_prod}" == "${product}"
            log to console    ${shoe_prod}
            click element    ${add_to_cart}
            ${i}   evaluate    ${i}-1
            BREAK
        END
      END
      Swipe    1052    1063    28    256   500
      SLEEP    5s
    END

#

Closing the application
    Close Application