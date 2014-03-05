/**
 * common.js
 * @authors Syaning (syaning@hotmail.com)
 * @date    2014-03-05 10:27:50
 * @version 1.0
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
					var filename = $('#filename').val();
					var format = $('#format').val();
					if (filename == '') {
						filename = 'default';
						$('#filename').val('default');
					}
					commands.push('savefig(' + 'imgData,' + ' format="' + format + '")');
					drawImage(commands, format);
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
});

function drawImage(commands, format) {
	var params = {
		query: commands.join("&%&"),// &%& is delimiter
		mimeType: format
	};

	$.post('/ajax/', params, function(data){
		if(format == "png" || format == "jpg"){
			$('.show-box').html('<img width="100%" height="100%" name="test" src="data:image/' + format + ';base64,' + data + '">');
		} else {
			$('.show-box').html('<embed width=' + document.body.offsetWidth / 2 + 'px height=' + document.body.offsetHeight + 'px src="data:application/' + format + ';base64,' + data + '">');
		}
		console.log(data);
	});
}