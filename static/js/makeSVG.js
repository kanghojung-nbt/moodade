
    var IDlist=new Array();  //color data모음집.
    var category ;

    var firstpercent ,lastpercent;

    var firstcolor;
    var lastcolor;

     var colorMap={"red":360, "orange":30, "yellow":60 , "green":180, "skyblue":210, "blue":240 ,"purple":300, "magenta":330};

    function makeColor(minval, maxval,color,category) {
        firstpercent=parseInt(10 * minval);
        lastpercent = parseInt(10* maxval);

        firstcolor="hsla("+(colorMap[color]-parseInt(minval))+",88%, "+firstpercent+"%"+", 0.9)";
        lastcolor= "hsla("+( parseInt(colorMap[color])+parseInt(last))+",98%, "+lastpercent+"%"+", 1)";
    }












