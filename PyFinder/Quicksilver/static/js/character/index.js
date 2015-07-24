/**
 * Created by adamthomson on 4/9/15.
 */

$(document).ready(function(){

    var chars_url = "/quicksilver/character/api_char_list/";

    $("#char_grid").jqGrid({
        colModel:[
            {name:'Character Name', index:'char_name', width:'150px', align:'left'},
            {name:'Creator', index:'char_user', width:'125px', align:'left'},
            {name:'Created', index:'char_date', width:'100px', align:'right'},
            {name:'Level', index:'char_level', width:'60px', align:'center'},
            {name:'Class', index:'char_class', width:'150px', align:'left'},
            {name:'Race', index:'char_race', width:'100px', align:'left'},
            {name:'Alignment', index:'char_align', width:'120px', align:'left'}
        ],
        rowNum: 50,
        caption:'Characters',
        height:'auto',
        datatype:'json',
        mtype: 'GET',
        url:chars_url
    });

});