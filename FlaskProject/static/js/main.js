$(document).ready(function(){
	
	$('#newprojform').on('submit', function(event){
		$.ajax ({
			data : {
					name : $('#name').val(),
					description : $('#description').val(),
					pgrade : $('#pgrade').val(),
					tags : $('#tags').val()
			},
			type : 'POST',
			url : '/newProj'
		})
		.done(function(data){
			if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
			}
			else {
				alert("Project created successfully")
				var prjcount=data.mydata['Projects'].length;
				var Projs=data.mydata['Projects']
				var myhtml="<p> Your Projects </p><hr><br>";
				myhtml = myhtml+"<div style='table-responsive' id='Proj'><table class='table table-striped table-responsive table-bordered table-hover'><tr class='active'>Project</th><th>Created On</th><th>Tags</th></tr>";
				for (i=0;i <prjcount;i++) {
					var prj = Projs[i];
					var slno = i+1;
					myhtml = myhtml+"<tr id=prj value=prj>";
					myhtml+="<td>"+prj['projid']+"</td><td><a href='#'>"+prj['prjname']+"<td>"+prj['createdDate'] +"</td><td>"+prj['tags']+"</td></tr>";
				};
				myhtml = myhtml+"</table> </div>"
				$('#successAlert').show();
				$('#showproj').html(myhtml);
				$('#errorAlert').hide();
			}
		});
		event.preventDefault();
	});

	$('td').onclick(function(event){
		console.log(this.value)
		alert(this.value);


	});

	$('input:checkbox').onclick(function(event){
		alert("i was clicked")
		var topic = (document.getElementById(this)).value;

		alert("topic is  ",topic);
		$("#topic").show();


	});

});