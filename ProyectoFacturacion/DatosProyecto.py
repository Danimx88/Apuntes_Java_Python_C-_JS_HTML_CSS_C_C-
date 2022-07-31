#El siguiente proyecto abarcara la realización de un sistema que simule una facturación

#Ingresa al apartado Mi nómina en Mis cuentas.
#Captura tu RFC y Contraseña o tu e.firma.
#Proporciona o actualiza la información requerida.
#Ingresa al apartado Mi nómina, Datos del patrón.
#Ingresa al apartado Mi nómina, Datos de los Trabajadores.
#Ingresa al apartado Mi nómina, Recibo de nómina.
#Proporciona la información requerida.
#Genera el comprobante fiscal.
#Imprime o descarga la factura electrónica de nómina.

#El orden para calcular los montos de una factura es:

#Importe = precio * unidad
#Impuestos (Traslados y Retenciones) = (base * tasa)/100
#Subtotal = (suma de importes)
#Se redondean el Subtotal y los Impuestos al número de decimales de la moneda
#Total = Subtotal - (suma de descuentos) + (suma de impuestos de traslado) - (suma de impuestos de retención)

#Concepto	Precio	Unidad	Tasa IVA
#CONSUMO DE ALIMENTOS POR DÍA FESTIVO	4,416.00	1.00	16%

#importes  impuestos  descuentos
#Importe = 4,416.00 * 1.00 = 4,416.00
#Impuestos (IVA de Traslados) = (4416 * 16)/100 = 706.56
#Subtotal = 4,416.00
#Se redondean el Subtotal y los Impuestos al número de decimales de la moneda (MXN)
#Total = 4,416.00 + 706.56 = 5,122.56

#Factura con descuentos
#Se desea facturar un servicio de mantenimiento de computo con un descuento:

#Concepto	Precio	Unidad	Tasa IVA	Descuento
#MANTENIMIENTO EQUIPO DE COMPUTO	25,862.0669	1.00	16%	1,062.00
#importes  impuestos  descuentos
#Importe = 25862.0669 * 1.00 = 25,862.0669
#Impuestos (IVA de Traslados) = (24800.0669 * 16)/100 = 39,68.010704. Base = importe - descuento
#Subtotal = 25,862.0669
#Se redondean el Subtotal y los Impuestos al número de decimales de la moneda (MXN)
#25,862.0669 -> 25,862.07; 3,968.010704 -> 3,968.01


#Factura con múltiples impuestos (traslados y retenciones)
#Se desea facturar una venta de productos con descuentos e impuestos de traslado:

#Concepto	Precio	Unidad	Tasa IVA	Descuento	Tasa IEPS
#CAJA CON 20 BOTTELLAS DE JUGO DE PIÑA	494.00	5.00	16%	0.0	30%
#CAJA CON 20 BOTTELLAS DE JUGO DE MANGO	598.00	10.00	16%	65.00	30%
# importes  impuestos  descuentos
#Importe 1° concepto: 494.00 * 5.00 = 2,470.00
#Impuestos 1° concepto:
 #  a) IEPS: (2470.00 * 30)/100 = 741.00
 #  b) IVA: (3211.00 * 16)/100 = 513.76. Base = importe - descuento + IEPS
#Importe 2° concepto: 598.00 * 10.00 = 5,980.00
#Impuestos 2° concepto:
 #  a) IEPS: (5915.00 * 30)/100 = 1,774.50. Base = importe - descuento
 #  b) IVA: (7689.50 * 16)/100 = 1,230.32. Base = importe - descuento + IEPS
#Subtotal = 2470.00 + 5980.00 = 8,450.00
#Se redondean el Subtotal y los Impuestos al número de decimales de la moneda (MXN)
#Total = 8,450.00 - 65.00 + 4,259.58 = 12,644.58
