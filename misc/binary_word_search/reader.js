const canvas = document.querySelector('canvas');
const ctx = canvas.getContext('2d');
const input = document.querySelector('input[type=file]');
let s;
input.addEventListener('change', () => {
    console.log(input.files);
    let f = input.files[0];
    drawImage(f);
});
function drawImage(file) {
    createImageBitmap(file)
        .then(img => {
        canvas.width = img.width;
        canvas.height = img.height;
        ctx.drawImage(img, 0, 0);
        readData();
    })
        .then(() => makeDownload());
}
function readData() {
    let id = ctx.getImageData(0, 0, canvas.width, canvas.height);
    let buf = id.data.buffer;
    let arr32 = new Uint32Array(buf);
    s = arr32.map(x => x == 4294967295 ? 1 : x == 4278190080 ? 0 : undefined).join('');
    s = s.match(/.{1000}/g).join('\n');
}
function makeDownload() {
    var textFile = null, makeTextFile = function (text) {
        var data = new Blob([text], { type: 'text/plain' });
        // If we are replacing a previously generated file we need to
        // manually revoke the object URL to avoid memory leaks.
        if (textFile !== null) {
            window.URL.revokeObjectURL(textFile);
        }
        textFile = window.URL.createObjectURL(data);
        return textFile;
    };
    var link = document.querySelector('a#downloadlink');
    link.href = makeTextFile(s);
    link.style.display = 'block';
}
