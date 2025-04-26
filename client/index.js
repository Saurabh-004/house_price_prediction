function getBHKvalue(){
    var bhk = document.getElementsByName("bath");
    for(var i in bhk){
        if( bhk[i].checked ){
            return parseInt(i) + 1;
        }
    }return -1;
}
function getBalconyValue(){
    var balcony = document.getElementsByName("Balcony");
    for(var i in balcony){
        if( balcony[i].checked ){
            return parseInt(i) + 1;
        }
    }return -1;
}
function getBathValue(){
    var bathroom = document.getElementsByName("bathrooms");
    for(var i in bathroom){
        if( bathroom[i].checked ){
            return parseInt(i) + 1;
        }
    }return -1;
}
function onclickEstimatedPrice(){
    console.log("estimate button clicked");
    let sqrft = document.querySelector("#sqft");
    let bath = getBathValue();
    let balcony = getBalconyValue();
    let bhk = getBHKvalue();
    let location = document.getElementById("uilocation");
    var estprice = document.getElementById("estprice");
    
    var url = "/makeprediction";
    // var url = "/api/makeprediction";
    $.post(url,{
        sqft: parseFloat(sqrft.value),
        bhk:bhk,
        bath:bath,
        balcony:balcony,
        location: location.value
    },function(data,status){
        console.log(data.estimated_price);
        estprice.innerHTML = "<h2> Estimated Price : " + data.estimated_price.toString() + " Lakhs </h2>";
        estprice.classList.add('estimated_price');
       
        console.log(status)}
)
   

}


function onPageload(){
    var url = "/get_location";
    // var url = "/api/get_location"
    $.get(url,function(data,status){
        console.log("got response get location names");
        console.log(data);
        if(data){
            var location = data.locations;
            var uilocation = document.getElementById("uilocation");
            $("#uilocation").empty();
            for (var i in location) {
                var opt = document.createElement("option");
                opt.value = location[i];
                opt.textContent = location[i];
                uilocation.appendChild(opt);
            }
            
            }
        
    });
}


window.onload = onPageload;