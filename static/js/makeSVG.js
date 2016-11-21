

     var colorMap={
        "redmin":360, "orangemin":18, "yellowmin":49 , "greenmin":120, "skybluemin":210, "bluemin":227 ,"purplemin":281, "magentamin":333,
        "redmax":360, "orangemax":33, "yellowmax":50 , "greenmax":120, "skybluemax":215, "bluemax":236 ,"purplemax":285, "magentamax":336
};

     var colorpower=
     {
         "redmax":85, "orangemax":96, "yellowmax":96 , "greenmax":67, "skybluemax":77, "bluemax":30 ,"purplemax":97, "magentamin":42,
         "redmin":81, "orangemin":79, "yellowmin":93 , "greenmin":41, "skybluemin":70, "bluemin":26 ,"purplemin":43, "magentamax":42
     };

      var colorbrightness  ={
          "redmax":92, "orangemax":91, "yellowmax":91 , "greenmax":90, "skybluemax":92, "bluemax":90 ,"purplemax":90, "magentamax":90,
         "redmin":60, "orangemin":61, "yellowmin":66 , "greenmin":58, "skybluemin":70, "bluemin":56 ,"purplemin":57, "magentamin":60

      }

    function makeColor(val ,color, minmax ) {   //minmax에는 최대최소를 구분하라. "minmax를 스트링을 줘서 맵에서 바로 뽑아쓰자."
        var colorpercent=parseInt(10 * val);
       console.log(val);
        console.log(color);
        var str;
        var colortype ; //색깔타입
        var power;      //채도 , hsla의 걍 두번째 인자값
        var brightness  // 명도,  hsla의 세번째 인자값


         power= (colorpower[color+"max"]  -colorpower[color+"min"] ) *  val *10/100+ colorpower[color+"min"];
         brightness = (colorbrightness[color+"max"]  -colorbrightness[color+"min"] ) *  val *10/100+ colorbrightness[color+"min"];
          console.log(brightness);
        str= color+minmax;
        console.log(str);
        return "hsla("+(colorMap[str])+","+power+ "%, "+brightness+"%"+", 1)";
    }

    function checkMinMax(val  , minmax ) {  // start점에서 val을 더하라.  max 는 양수 min은 음수
        if(minmax=="max"){
            return val;
        }else
            return -1*val;
    }














