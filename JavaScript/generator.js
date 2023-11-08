import {hextorgb,rgbtohsv} from "./logics.js";

class Generator{
    constructor(hex){
        this.hex = hex;
        this.rgb = hextorgb(this.hex);
        this.hsv = rgbtohsv(this.rgb[0],this.rgb[1],this.rgb[2]);

        // Variable for Calculating Shades, s for saturation and v for value

        this.s19 = 22;
        this.s37 = 12;
        this.s26 = 17;
        this.s48 = 7;

        this.v19 = 22;
        this.v37 = 12;
        this.v26 = 17;
        this.v48 = 7;

        // creating color defualt Hue Amount

        this.red = 1;
        this.orange = 37;
        this.blue = 210;
        this.green = 125;

        this.supportingColorObj = {"red":{},"blue":{},"green":{},"orange":{}};

    }

    mainColor(){
        const maincolorobj = {"hex":this.hex,"rgb":this.rgb,"hsv":this.hsv};
        return maincolorobj;
    }

    neutralColor(){
        const neutralcolorobj = {"100": "[0,0,94]",
        "200": "[0,0,84]",
        "300": "[0,0,74]",
        "400": "[0,0,64]",
        "500": "[0,0,54]",
        "600": "[0,0,44]",
        "700": "[0,0,34]",
        "800": "[0,0,24]",
        "900": "[0,0,10]"};

        return neutralcolorobj;
    }

    supportingColor(){
        // creating objects to handle output sobj for saturation and vobj for value
        let sobj = {};
        let vobj = {};

        // Saturation 
        sobj["100"] = this.hsv[1] - this.s19;
        sobj["200"] = this.hsv[1] - this.s26;
        sobj["300"] = this.hsv[1] - this.s37;
        sobj["400"] = this.hsv[1] - this.s48;
        sobj["500"] = this.hsv[1];
        sobj["600"] = this.hsv[1] + this.s26;
        sobj["700"] = this.hsv[1] + this.s37;
        sobj["800"] = this.hsv[1] + this.s48;
        sobj["900"] = this.hsv[1] + this.s19;

        // Value
        vobj["100"] = this.hsv[2] + this.s19;
        vobj["200"] = this.hsv[2] + this.s26;
        vobj["300"] = this.hsv[2] + this.s37;
        vobj["400"] = this.hsv[2] + this.s48;
        vobj["500"] = this.hsv[2];
        vobj["600"] = this.hsv[2] - this.s26;
        vobj["700"] = this.hsv[2] - this.s37;
        vobj["800"] = this.hsv[2] - this.s48;
        vobj["900"] = this.hsv[2] - this.s19;

        // Generating key Variable

        let objKey = Object.keys(sobj);
        

        // Looping through keys to CHeck conditions

        objKey.forEach(ele => {
            if(sobj[ele] < 10){
                sobj[ele] = 10;
            }else if(sobj[ele] > 100){
                sobj[ele] = 100;
            }
            if(vobj[ele] < 15){
                vobj[ele] = 15;
            }else if(vobj[ele] > 100){
                vobj[ele] = 100;
            }
        });

        // creating Color Name Variable
        // self.__SupportingColorDict[cname][k] = f"{self.__red,SaturationDict[k],ValueDict[k]}"

        let cname = ["red","green","blue","orange"];

        cname.forEach(color => {
            objKey.forEach(ind => {
                if (color === "red"){
                    this.supportingColorObj[color][ind] = [this.red,sobj[ind],vobj[ind]];
                }else if(color === "blue"){
                    this.supportingColorObj[color][ind] = [this.blue,sobj[ind],vobj[ind]];
                }else if(color === "green"){
                    this.supportingColorObj[color][ind] = [this.green,sobj[ind],vobj[ind]];
                }else{
                    this.supportingColorObj[color][ind] = [this.orange,sobj[ind],vobj[ind]];
                }
            });
        });

        return this.supportingColorObj

    }

}




