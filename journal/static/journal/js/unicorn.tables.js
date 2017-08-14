/**
 * Unicorn Admin Template
 * Diablo9983 -> diablo9983@gmail.com
**/
$(document).ready(function(){
	
	$('.data-table').dataTable({
		"bJQueryUI": true,
		"sPaginationType": "full_numbers",
		"sDom": '<""l>t<"F"fp>',
		"aaSorting": [[6, "desc"]],
		"oLanguage":{
			"sLengthMenu": "每页 _MENU_ 条",
			"sProcessing": "数据加载中......",
			"sEmptyTable": "数据为空......",
			"sZeroRecords": "对不起，查询不到相关数据！",
			"sSearch": "搜索",
			"oPaginate":{
				"sFirst": "首页",
				"sPrevious": "上一页",
				 "sNext": "下一页",
				 "sLast": "末页"
			}
		}
	});
	
	$('input[type=checkbox],input[type=radio],input[type=file]').uniform();
	
	$('select').select2();
	
	$("span.icon input:checkbox, th input:checkbox").click(function() {
		var checkedStatus = this.checked;
		var checkbox = $(this).parents('.widget-box').find('tr td:first-child input:checkbox');		
		checkbox.each(function() {
			this.checked = checkedStatus;
			if (checkedStatus == this.checked) {
				$(this).closest('.checker > span').removeClass('checked');
			}
			if (this.checked) {
				$(this).closest('.checker > span').addClass('checked');
			}
		});
	});	
});
