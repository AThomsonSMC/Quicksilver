$(document).ready(function(){

    var char_id = $("#char_id").text();
    var skill_url = "/quicksilver/character/" + char_id;
    skill_url += "/api_skill_list/";

    $("#skill_grid").jqGrid({
        colModel:[
            {name:'Skill Name', index:'name', width:'115px', align:'left'},
            {name:'Bonus', index:'bonus', width:'50px', align:'center', classes:'total_bonus'},
            {name:'Ability', index:'ability', width:'50px', align:'center', classes:'grid_abil'},
            {name:'Abil Mod', index:'abil_mod', width:'50px', align:'center'},
            {name:'Ranks', index:'ranks', width:'40px', align:'center'},
            {name:'Misc. Mod', index:'misc', width:'60px', align:'center'}
        ],
        rowNum: 50,
        caption:'Skills',
        height:'auto',
        datatype:'json',
        mtype: 'GET',
        url:skill_url
    });

});


