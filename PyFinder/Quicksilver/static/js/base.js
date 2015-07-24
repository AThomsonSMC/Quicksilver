$(document).ready(function(){

    $(".nav_button").button();

    $("#new_char_button").click(function(){
        window.location = "/quicksilver/character/new";
    });
    $("#view_chars_button").click(function(){
        window.location = "/quicksilver/character";
    });
    $("#view_class_button").click(function(){
        window.location = "/quicksilver/class";
    });
    $("#view_races_button").click(function(){
        window.location = "/quicksilver/races";
    });
    $("#view_feats_button").click(function(){
        window.location = "/quicksilver/feats";
    });
    $("#view_spells_button").click(function(){
        window.location = "/quicksilver/spells";
    });

});