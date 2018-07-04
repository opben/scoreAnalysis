;$(function(){
    'use strict';

    let $slideBar = $(".slideBar"),   //侧边栏
        $toolbar = $(".toolbar"),
        $menu = $(".showSlideBar"); //icon

    function showBar() {
        $slideBar.css('left', 0); //修改CSS
        $toolbar.css('marginLeft', $slideBar.width());
    }

    function hideBar() {
        $slideBar.css('left', - $slideBar.width()); //修改CSS
        $toolbar.css('marginLeft', 0);
    }

    // 点击menu隐藏菜单，再次点击显示。这么简单的逻辑改了好久...
    $menu.on('click',function () {
        if ($slideBar.css('left')==='0px') {
            hideBar();
        }else {
            showBar();
        }
    })

});