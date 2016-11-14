

     var colorMap={"red":360, "orange":30, "yellow":60 , "green":180, "skyblue":210, "blue":240 ,"purple":300, "magenta":330};

    function makeColor(val ,color) {
        var colorpercent=parseInt(10 * val);
        return "hsla("+(colorMap[color]-parseInt(val))+",88%, "+colorpercent+"%"+", 0.9)";
    }












