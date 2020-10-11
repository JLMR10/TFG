document.getElementById('ModalMapForm').mapList.onchange = function() {
    var value = this.value;
    if (value != ""){
        document.getElementById("createBtn").disabled = false;
        $('.select2-container--default .select2-selection--single').css('border-color','#4e73df');
        $('.select2-selection__rendered').css('color','#000')
    }else{
        document.getElementById("createBtn").disabled = true;
        $('.select2-container--default .select2-selection--single').css('border-color','#ccc');
        $('.select2-selection__rendered').css('color','#7d7d7d')
    }
};

$(document).ready(function () {
    $('[data-toggle="tooltip"]').tooltip()
    $('.select2-selection__rendered').css('color','#7d7d7d')
})


function changeValueMap(mapId) {
    document.getElementById("editMap").mapId.value = mapId;
    document.forms['editMap'].submit();
}