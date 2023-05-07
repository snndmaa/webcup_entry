var adSwitch = 1

function cursorStart(num){
    document.getElementsByClassName("question_detail")[num].focus()
    document.getElementsByClassName("question_detail")[num].setSelectionRange(0,0)
}

function backgroundChange(num, format){
    const htmlElement = document.documentElement
    htmlElement.style.backgroundImage = `url(/static/images/button_images/${num}.${format})`
    htmlElement.style.display = 'block'
    htmlElement.style.marginLeft = 'auto'
    htmlElement.style.marginRight = 'auto'
    // htmlElement.style.width = '50%'
}

function closeAd() {
    var ad = document.getElementById("ad");
    ad.style.display = "none";
}