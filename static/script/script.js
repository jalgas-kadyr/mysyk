$(document).ready(function(){
    var flag = false;
    $('.mbutton').click(function (event){
        if(flag == false){
            $('.vector').css('transform', 'rotate(180deg)');
            $('.menu').css('zoom', '3');
            $('.menu').css('opacity', '1');
            $('.menu').css('visibility', 'visible');
            flag = true;
        }else {
            $('.vector').css('transform', 'rotate(0deg)');
            $('.menu').css('zoom', '0.1');
            $('.menu').css('opacity', '0');
            $('.menu').css('visibility', 'hidden');
            flag = false;
        }
    })

})
