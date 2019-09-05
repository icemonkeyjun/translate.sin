function resize(obj) {
    obj.style.height = "1px";
    obj.style.height = (3+obj.scrollHeight)+"px";
}
resize(document.getElementById('translateResultInput'));
resize(document.getElementById('coinSentenceInput'));