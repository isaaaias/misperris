

$(document).ready(function() {
    jQuery.validator.addMethod("rut", function(value, element) { 
        return this.optional(element) || validaRut(value); 
    }, "Revise el RUT");
    jQuery.validator.addMethod("txtTelefono", function(value, element) {
        return this.optional(element) || soloLetras(value);
    }, "Solo Numeros"); 
    jQuery.validator.addMethod("email", function(value, element) { 
        return this.optional(element) || isEmail(value); 
    }, "Revise el Email");
        
    $("#formularioFundacion").validate({
        rules:{
            rut: {
            required: true,
            rut:true,
            minlength:11,
            maxlength: 12
            },
            nombre: {
            required: true,
            minlength: 8,
            maxlength: 50
            },
            dtpFechaNacimiento: {
            required:true,
            date:true
            },
            email: {
            required:true,
            email: true
            },
            txtTelefono:{
            required:true,
            number:true,
            minlength: 9,
            maxlength: 12,
            txtTelefono:true
            },
            cboRegion:{
            required:true,
            
            },
            cboCiudad:{
            required:true,
            
            },
            cboComuna:{
            required:true,
            
            },
            cboVivienda:{
            required:true,
            
            },
        },
        messages:{
           
            rut: "Favor Ingrese su rut",
            rut: {
                required: "Favor Ingrese su rut",
            },
            nombre: "Ingrese solo caracteres",
            nombre:{
                required:"Ingrese solo caracteres",
                minlength:"El largo debe ser mayor a 8 caracteres",
                maxlength:"El largo debe ser menor a 50 caracteres"
            },
            dtpFechaNacimiento:{
                required:"Ingrese una fecha valida",
     
            },
            email:"Ingrese con formato de correo valido",
            email:{
                required:"Ingrese su correo electronico",
                email:"Ingrese un correo electronico valido"
            },
            txtTelefono: "Ingrese Numero telefonico",
            txtTelefono:{
            required:"Ingrese Numero telefonico",
            minlength:"El largo debe ser mayor a 9 caracteres",
            maxlength:"El largo debe ser menor a 12 caracteres"
       
            },
            cboRegion:{
                required:"Seleccione una Region"
            },
            cboCiudad:{
                required:"Seleccione una Ciudad"
            },
            cboComuna:{
                required:"Seleccione una Comuna"
            },
            cboVivienda:{
                required:"Seleccione tipo de Vivienda",
            },
        }
    });
});
