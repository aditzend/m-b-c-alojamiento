## start
* bfi_start
    - action_parse_context
    - utter_Inicio_Saluda

## st1
* ActualizacionDeDatos_NoSoy
  - utter_Informa_ActualizacionDeDatos_Gracias

## st2
* ActualizacionDeDatos_Actualizar
  - utter_Informa_ActualizacionDeDatos_Como

## st3
* Afiliaciones_Categoria
  - utter_Informa_Afiliaciones_Categoria

# hotel
* Pide_Reserva
    - utter_Pregunta_Reserva_Fecha
* Informa_Reserva_Fecha{"reserva_fecha":"27"}
    - utter_Pregunta_Reserva_Pax
* Informa_Reserva_Pax{"reserva_pax":"4"}
    - slot{"reserva_fecha":"4"}
    - action_echo
    - utter_Confirma_Reserva

# reinicia
* Pide_Reiniciar
    - action_restart

# da id
* Identificacion_Nro_Cedula{"nro_cedula":"12345678"}
    - utter_Confirma_Nro_Cedula

# da un codigo
* Decir_Codigo{"codigo":"123"}
    - utter_Confirma_Codigo

#da un celular
* Decir_Celular{"nro_celular":"3013209089"}
    - utter_Confirma_Nro_Celular
