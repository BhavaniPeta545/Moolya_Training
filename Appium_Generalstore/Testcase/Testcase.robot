*** Settings ***
Resource    ../Resources/Resources.robot

*** Test Cases ***
Launch the application
    Opening Application
Provide details
    Select the country
    Provide the name
    Select gender
    Lets shop
Purchase product
    Addtocart
Procced to checkout
    Proceed
Terminate application
    Closing the application




