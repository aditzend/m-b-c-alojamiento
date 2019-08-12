## intent:bfi_start
- *online {InteractionId: 20398498498, UserName: Alex, UserMail: alex@alex.com, ...}
- *online {"InteractionId":"190805124058612_CHT_29000","UserName":"jtorrelles","Parameters":["user.name=jtorrelles","user.mail=jtorrelles@myserver.com","user.channel=11"],"Message":"cmd=&msg=Hola!&","Channel":"web_sock","Lang":"es","Encoding":"utf-8","EventName":"*text","MimeType":"text/plain","Source":"127.0.0.1","UserChannel":"11","UserId":"jtorrelles","UserMail":"jtorrelles@myserver.com","BotName":"PI_Bot"}

# intent:Consulta_ActualizacionDeDatos_Actualizar
- como puedo actualizar datos?
- a través de que medio se pueden actualizar datos

## intent:Consulta_ActualizacionDeDatos_NoSoy
- Mi nombre no es ese
- Yo no soy ese
- como actualizo mis datos?
- no soy yo
- me estas confundiendo con una persona
- yo no me llamo asi

## intent:Consulta_Afiliaciones_Categoria
- como consulto mi categoria
- como valido mi categoria de validacion
- que categoria soy
- quiero saber cual es mi categoria de afiliacion
- en que categoria estoy
- quisiera saber cual es la categoria la cual fui asignado
- mi categoria porfa
- cual es mi categoria
- en que cate estaba yo?
- que categoria
- que categoria soy?

## intent:Dice_Gracias
- gracias
- Gracias
- grcs
- gr
- =)
- grasias

## intent:Pide_Reserva
- quiero reservar un hotel
- quiero hacer una reserva
- reservame por favor una habitacion
- hotel

## intent:Informa_Reserva_Fecha
- para el [27](reserva_fecha) 
- para el [viernes](reserva_fecha) 
- el [sabado](reserva_fecha) 
- [este fin de semana](reserva_fecha) 

## intent:Informa_Reserva_Pax
- vamos a ser [cuatro](reserva_pax:4)
- vamos a ser [TRES](reserva_pax:4)
- vamos a ser [mi esposo, mi hija y yo](reserva_pax:3)
- podrias reservarme para los [cinco](reserva_pax:5)?
- [1](reserva_pax)
- [2](reserva_pax)
- [3](reserva_pax)
- [4](reserva_pax)
- [5](reserva_pax)

## intent:Pide_Reiniciar
- empecemos de cero
- no entendiste nada, vamos de nuevo
- de cero
- volver al inicio
- volver a empezar

## intent:Identificacion_Nro_Cedula
- mi cedula es [29984695](nro_cedula)
- como no, es [12.234.439](nro_cedula)
- [13 234 432](nro_cedula)
- te paso [34149040](nro_cedula)
- te paso [89 094 309](nro_cedula)
- te paso [34.567.324](nro_cedula)
- te paso [47.234.456](nro_cedula)
- te paso [89.345.123](nro_cedula)


## intent:Decir_Codigo
- mi codigo es [123](codigo)
- el cod es [12](codigo)
- cod: [345](codigo)

## regex:nro_cedula
- \d{2}.\d{3}.\d{3}
- \d{8}




