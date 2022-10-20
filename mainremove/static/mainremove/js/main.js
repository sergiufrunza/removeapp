

const uploadfile = document.getElementById("fimage");
const labeluploadfile = document.getElementById("text_label");
const uploadimage = document.getElementById("upload_img");
const loader = document.getElementById("loader");
const submitbtn = document.getElementById("lsubmit"); 

uploadfile.addEventListener('change', (event) => {
	if (uploadfile.value != ""){
		var reader = new FileReader();
		reader.onload = function() {
			uploadimage.src = reader.result;
			labeluploadfile.style.display = "none";
			uploadimage.style.display = "block";

      
    }
    reader.readAsDataURL(uploadfile.files[0]);

		}
	});

submitbtn.onclick = function () {
	loader.style.display = "flex";
}