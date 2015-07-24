/**
 * Created by adamthomson on 5/30/15.
 */

$(document).ready(function(){

    var classes_url = "/quicksilver/class/api_class_list/";

    $("#char_grid").jqGrid({
        colModel:[
            {name:'Class Name', index:'class_name', width:'150px', align:'left'},
            {name:'Alignments', index:'class_align', width:'100px', align:'left'},
            {name:'Hit Die', index:'class_hd', width:'60px', align:'center'},
            {name:'Skill Ranks', index:'class_ranks', width:'80px', align:'center'},
            {name:'Weapon Prof', index:'class_weapon', width:'130px', align:'left'},
            {name:'Armor Prof', index:'class_armor', width:'180px', align:'left'},
            {name:'Caster', index:'class_caster', width:'120px', align:'left'}
        ],
        rowNum: 50,
        caption:'Classes',
        height:'auto',
        datatype:'json',
        mtype: 'GET',
        url:classes_url
    });

});