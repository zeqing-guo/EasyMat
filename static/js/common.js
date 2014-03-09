/**
 * common.js
 * @authors	Syaning (syaning@hotmail.com)
 * @date  	2014-03-05 10:27:50
 * @contributor	zqguo (zqguo@zqguo.com)
 * @date	2014-03-06 22:20:30
 * @version	1.1
 */

$(function() {
	var cmd = $('#cmd');
	var monitor = $('#monitor');
	var commands = new Array();
	cmd.focus();

	cmd.focus().keydown(function(e) {
		if (e.keyCode == 13) {
			var value = cmd.val();
			if (value) {
				if (value == 'draw') {
					cmd.val('');
//					var filename = $('#filename').val();
                    var filename = 'default';
					var format = $('#format').val();
//					if (filename == '') {
//						filename = 'default';
//						$('#filename').val('default');
//					}
					//commands.push('savefig(' + 'imgData,' + ' format="' + format + '")');
					drawImage(commands, format, filename);
					commands.splice(0);
				} else if (value == 'clear') {
					cmd.val('');
					monitor.text('>>> Welcome to EasyMat!');
					monitor.append(document.createElement('br'));
					monitor.append(document.createTextNode('>>> '));
					commands.splice(0);
				} else {
					var span = document.createElement('span');
					span.className = 'green-font';
					span.appendChild(document.createTextNode(value));
					monitor.append(span);
					monitor.append(document.createElement('br'));
					monitor.append(document.createTextNode('>>> '));
					commands.push(value);
					cmd.val('');
				}
			}
		}
	});

	$('#prompt').click(changeMode);
	$('#upload').click(uploadFile);
});

function drawImage(commands, format, filename) {
	var params = {
		query: commands.join("&%&"), // &%& is delimiter
		mimeType: format,
		fileName: filename
	};

	$.post('/ajax_draw/', params, imageDraw);
}

/**
 * enter commands or upload file
 * @return
 */
function changeMode() {
	var prompt = $('#prompt');
	if (prompt.text() == '>>>') {
		prompt.text('File');
		$('#cmd').addClass('hidden');
		$('#file').removeClass('hidden');
		$('#upload').removeClass('hidden');
	} else if (prompt.text() == 'File') {
		prompt.text('>>>');
		$('#file').addClass('hidden');
		$('#upload').addClass('hidden');
		$('#cmd').removeClass('hidden');
	}
}

function uploadFile(event) {
	var file = $('#file').val();
    $("#mimeType").val($('#format').val());
	if (file) {
        $('#file-form').submit(function(){
        console.log("test-1");
			$('#file-form').ajaxSubmit({
				type: 'POST',
				url: '/ajax_file/',
				success: imageDraw,
				error: function() {
					alert('File upload failed.')
				}
			});
            return false;
            });
//        $('#file-form').ajaxForm(function(data) { 
//               console.log("test0")
//               console.log(data)
//       }); 
	}else{
		alert('Please choose a file');
	}
}

function imageDraw(data) {
    var format = $('#format').val();
	// For finding exception
	// If check = "True", then there is an exception
	var monitor = $('#monitor');
	check = data.slice(0, 4);
	if (check === "True") {
		// Show the exception
		exceptionData = data.slice(4)
		console.log(exceptionData);
		var span = document.createElement('span');
		span.className = 'green-font';
		span.appendChild(document.createTextNode(exceptionData));
		monitor.append(span);
		monitor.append(document.createElement('br'));
		monitor.append(document.createTextNode('>>> '));
		commands.push(value);
		cmd.val('');
		return;
	}
	if (format == "png" || format == "jpg") {
		$('.show-box').empty()
		$('.show-box').html('<img width="100%" height="100%" name="test" src="data:image/' + format + ';base64,' + data + '">');
	} else {
		$('.show-box').empty()
		$('.show-box').html('<embed width=' + document.body.offsetWidth / 2 + 'px height=' + document.body.offsetHeight + 'px src="data:application/' + format + ';base64,' + data + '">');
	}

}
