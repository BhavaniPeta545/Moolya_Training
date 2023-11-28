*** Settings ***

*** Variables ***
${url}=     http://localhost:4723/wd/hub
${devicename}=   Bhavani
${platformname}=   Android
${apppackage}=   com.androidsample.generalstore
${appactivity}=   com.androidsample.generalstore.SplashActivity


${element_visible}=     Brazil
${product}=     Converse All Star
${country}=     id=com.androidsample.generalstore:id/spinnerCountry
${countryframe}=    xpath=/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout
${countryname}=     xpath=/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[4]
${input_text}=       id=com.androidsample.generalstore:id/nameField
${radiofemale}=     id=com.androidsample.generalstore:id/radioFemale
${radiomale}=       id=com.androidsample.generalstore:id/radioMale
${letsshop_button}=     id=com.androidsample.generalstore:id/btnLetsShop

${products_list}=       id=com.androidsample.generalstore:id/rvProductList

${add_to_cart}=     xpath=//android.widget.TextView[@text='Converse All Star']/..//android.widget.TextView[@text='ADD TO CART']
${cart_btn}=        id=com.androidsample.generalstore:id/appbar_btn_cart

${checkbox_text}=       Send me e-mails on discounts related to selected products in future
${proceed_btn}=     id=com.androidsample.generalstore:id/btnProceed
#${shoe}=        xpath=/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]


