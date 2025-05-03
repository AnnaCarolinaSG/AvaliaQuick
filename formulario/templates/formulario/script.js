$(document).read(function(){
    $("#gestor_contratos_2").prop("disable", true);
    const gestor_contratos = document.querySelector('input[field_name="gestor_contratos"]:checked')
    if (gestor_contratos == "2"){
        $("#gestor_contratos_2").prop("disable", false);
    } else if (gestor_contratos == "1"){
        $("#gestor_contratos_1").prop("disable", false);
        $("#gestor_contratos_2").prop("disable", true);
    } else if (gestor_contratos == "0"){
        $("#gestor_contratos_0").prop("disable", false);
        $("#gestor_contratos_2").prop("disable", true);
    }
})