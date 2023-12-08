const CryptoJS=require('./crypto-js')
const encode=(str)=>
{
    const s1=CryptoJS.enc.Base64.stringify(CryptoJS.enc.Utf8.parse(str))
    const x=s1.indexOf('=')
    const s2=CryptoJS.enc.Base64.stringify(CryptoJS.enc.Utf8.parse(Math.random().toString())).slice(0,16)
    if(x!==-1)
    {
        return s2+s1.slice(0,x).split('').reverse().join('')+s1.slice(x)
    }
    else
    {
       return s2+s1.split('').reverse().join('')
    }
}
const cal=(str)=>
{
    let x=0
    for(let i=0;i<str.length;i++)
    {
        x+=str.charCodeAt(i)%10
    }
    return x<<8
}
const getEncLink=(str)=>
{
    const e=Math.random().toString(10).substring(2)
    const i=cal(str+'@'+e)
    return encode(str)+'@'+e+'@'+i
}
const getDecData=(str)=>
{
    str=str.slice(16)
    const x=str.indexOf('=')
    if(x!==-1)
    {
        return CryptoJS.enc.Utf8.stringify(CryptoJS.enc.Base64.parse(str.slice(0,x).split('').reverse().join('')+'='))
    }
    else
    {
        return CryptoJS.enc.Utf8.stringify(CryptoJS.enc.Base64.parse(str.split('').reverse().join('')))
    }
}
const toolBase64=(str)=>
{
    return CryptoJS.AES.encrypt(
        CryptoJS.enc.Utf8.parse(str),
        CryptoJS.enc.Utf8.parse('H0GM7TGBw193GYf8'),
        {
            iv:CryptoJS.enc.Hex.parse('0000000000000000'),
            mode:CryptoJS.mode.CBC,
            padding:CryptoJS.pad.Pkcs7,
        }
    ).ciphertext.toString(CryptoJS.enc.Base64)
}
const getAcceptPatch=(hostPrefix,str)=>
{
    const a=hostPrefix.charAt(str.charCodeAt(0)%hostPrefix.length)
    const b=hostPrefix.charAt(str.charCodeAt(str.length-1)%hostPrefix.length)
    return toolBase64(a+str+b);
}