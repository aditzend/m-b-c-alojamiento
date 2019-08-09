## st1
* ActualizacionDeDatos_NoSoy
  - action_hello_world
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

