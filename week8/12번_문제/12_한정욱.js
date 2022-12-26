/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    //if the number is 4 or 9 we subtract the number 
    //make numeral list and roman list 
    const numeral = [1000, 900 , 500, 400,  100, 90, 50, 40, 10, 9, 5, 4, 1];
    const roman = ["M" , "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    let result ="";
    let i =0;
    while(num > 0){
        //going through numeral numbers and minus the numeral number and add the roman into result
        if(num - numeral[i]>= 0){
            result+=roman[i];
            num -=numeral[i];
        }
        else i++;
    }
    return result;
};
