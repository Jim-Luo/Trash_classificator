
// File reading
function encodeImageFileAsURL(file) {
    var reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = function () {
        console.log(reader.result);
        document.querySelector("#Thumbnail").src = reader.result;

        var xhttp = new XMLHttpRequest();
        xhttp.open("POST", "/process", true);
        xhttp.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            var res = JSON.parse(this.responseText);
            document.querySelector("#result").textContent = res["result"];
        }
        };
        xhttp.send(
            JSON.stringify({
                content : reader.result
            })
        );
    };
    reader.onerror = function (error) {
        return error;
    };
}

//Upload Button
const upload = document.querySelector("#Upload");
upload.onclick = function (e) {
    var photo = document.querySelector("#photo").files[0];
    encodeImageFileAsURL(photo);
    document.querySelector("#UploadingBar").classList.replace('d-flex', 'd-none');
    document.querySelector("#ResultBar").classList.replace('d-none','d-flex');
};

//Try Again Button
const back = document.querySelector("#Back");
back.onclick = function () {
    document.querySelector("#UploadingBar").classList.replace('d-none', 'd-flex');
    document.querySelector("#ResultBar").classList.replace('d-flex','d-none');
};