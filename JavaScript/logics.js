
// Round up Function
function roundup(val){
    let intval = parseInt(val)
    let valans = intval + 1

    if (val + 0.5 >= valans){
        return valans
    }else if(val + 0.5 < valans){
        return intval
    } 
}

// Min and Max Functions

function Max(r,g,b){
    if(r > g && r > b){
        return r
    }else if(g > r && g > b){
        return g
    }else{
        return b
    }
}

function Min(r,g,b){
    if(r < g && r < b){
        return r
    }else if(g < r && g < b){
        return g
    }else{
        return b
    }
}

function hextorgb(hex){

    if(typeof(hex) != 'string'){
        return false
    }

    let rgb = []

    for (let i=0;i<6;i+=2){
        let temp = hex.substring(i,i+2);
        let decimalVal = parseInt(temp,16)
        rgb.push(decimalVal)
    }

    return rgb

}

function rgbtohex(r,g,b){
    let HexR = r.toString(16).padStart(2,'0')
    let HexG = g.toString(16).padStart(2,'0')
    let HexB = b.toString(16).padStart(2,'0')

    return hexcode = "#" + HexR + HexG + HexB
}


function rgbtohsv(r, g, b) {
    // Converting RGB Values from 0-255 to 0-1
    let R = r / 255.0
    let G = g / 255.0
    let B = b / 255.0

    // Calculating Min Max and Diff Values

    let MinV = Min(R,G,B)
    let MaxV = Max(R,G,B)
    let Diff = (MaxV - MinV)

    // Hue Calculation
    let h = 0
    
    if(MinV == MaxV){
        h = 0
    }
    else if(MaxV == R){
        h = (60 * ((G - B)/Diff) + 360) % 360
    }
    else if(MaxV == G){
        h = (60 * ((B - R)/Diff) + 120) % 360
    }else if(MaxV == B){
        h = (60 * ((R - G)/Diff) + 240) % 360
    }

    // Saturation Calculation

    let s = 0

    if (MaxV == 0){
        s = 0
    }else{
        s = (Diff/MaxV) * 100
    }

    // Value Calculation

    let v = MaxV*100

    let HSV = [roundup(h),roundup(s),roundup(v)]

    return HSV

  }
  

export {hextorgb,rgbtohex,rgbtohsv}