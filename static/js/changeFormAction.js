document.getElementById('ModalMapForm').mapList.onchange = function() {
    var newAction = this.value;
    console.log(this.value)
    if (newAction != ""){
        document.getElementById("createBtn").disabled = false;
    }else{
        document.getElementById("createBtn").disabled = true;
    }
    document.getElementById('ModalMapForm').action = "/"+newAction+"/";
};

