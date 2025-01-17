async function postShortenURL(event) {
	const url = "/app/create";
	const body = {
		"original_url": document.getElementById("original_url").value
	};

	const response = await fetch(url, {
		method: "POST",
		headers: {
			"Content-Type": "application/json"
		},
		body: JSON.stringify(body)
	}).then(
		function(res) {
			if(res.status === 200) {
				res.json().then(function(data){
					onSuccessShorten(body.original_url, data.short_url_id)
				});
			} else if(res.status === 400) {
				res.json().then(function(data){
					alert(data.message)
				});
			}
		}
	).catch(function(error) {
		console.log(error);
	});
}

function setURL(url, target_element) {
	target_element.value = url;
}

function onSuccessShorten(originalurl, shorturl) {
	console.log(originalurl, shorturl);
	setURL(originalurl, document.getElementById("long_url"));
	setURL(window.location.href + shorturl, document.getElementById("short_url"));

	document.getElementById("output").style.display = "";
}

function copyURLToClipboard(input_id, event) {
	const inputelement = document.getElementById(input_id);
	inputelement.select();
	inputelement.setSelectionRange(0, 99999);

	navigator.clipboard.writeText(inputelement.value);
}

document.addEventListener("DOMContentLoaded", function(event) {
	document.getElementById("shorten_url_form").addEventListener('submit', event => event.preventDefault());
	document.getElementById("long_copy_btn").addEventListener("click", (event) => copyURLToClipboard("long_url", event));
	document.getElementById("short_copy_btn").addEventListener("click", (event) => copyURLToClipboard("short_url", event));
});