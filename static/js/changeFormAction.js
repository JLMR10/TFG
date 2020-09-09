document.getElementById('ModalMapForm').mapList.onchange = function() {
    var value = this.value;
    if (value != ""){
        document.getElementById("createBtn").disabled = false;
    }else{
        document.getElementById("createBtn").disabled = true;
    }
};

function changeValueMap(mapId) {
    document.getElementById("editMap").mapId.value = mapId;
    document.forms['editMap'].submit();
}