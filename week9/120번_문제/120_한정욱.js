/**
 * @param {number[][]} triangle
 * @return {number}
 */
var minimumTotal = function(triangle) {
    let sum =0;
    let j =0;//for 2D
    for(let i in triangle){
       let min = 0; //finding minimum
        if(triangle[i][j] > triangle[i][j+1]){
            min = triangle[i][j+1]
            j= j+1;
        }
        else{
            min = triangle[i][j]
        }
        sum += min; 
    }
    return sum 
};
