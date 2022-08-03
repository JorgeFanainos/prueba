from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import click

lista_area = []
lista_fechaIni = []
lista_horaIni = []
lista_fechaFin = []
lista_horaFin = []
lista_servicio = []

print(""" 
  000000    0    0    000000
  0    0    0    0    0
  00000     0    0    0
  0    0     0  0     0
  000000      00      000000
""")

print("Bienvenido al sistema de genración de reportes\n\n\n")

nombre = input("\nIngrese el nombre del documento:")
canvas = canvas.Canvas(nombre+".pdf", pagesize=letter)
canvas.setStrokeColorRGB(0, 0, 0)
canvas.setLineWidth(.3)
canvas.setFont('Helvetica', 9)
canvas.drawImage("logo.png", 30,700, width=150, height=100)
canvas.drawString(82,700,"RIF: J-000029709")
canvas.setFont('Helvetica', 15)
canvas.drawString(125,660,"Informe de Eventos, Fallas o Incidencias [ Inicio/Cierre ]")





"""Area deteccion incidente"""


nombre_area = input("\nIngrese el nombre del área donde se detectó el incidente: ")



"""Area indicacion de servcio"""




nombre_servicio = input("\nIngrese el nombre del servicio donde se presento el incidente: ")


"""Area Canales"""



aux = True
print("""
  Porfavor seleccione uno de los canales:\n
  1)oficinas     2)IVR \n
  3)ATM           4)POS \n
  5)Banca Por Internet \n

  (Si el servicio es Suiche7b o Tranred, solo presionar ENTER)\n
  """)
while aux == True:
  seleccion_canales = input("-->")
  if seleccion_canales == "1":
    canvas.drawString(240,574, "X")
    aux = False
  elif seleccion_canales == "2":
    canvas.drawString(375,574, "X")
    aux = False
  elif seleccion_canales == "3":
    canvas.drawString(525,574, "X")
    aux = False
  elif seleccion_canales == "4":
    canvas.drawString(227,554, "X")
    aux = False
  elif seleccion_canales == "5":
    canvas.drawString(440,554, "X")
    aux = False
  elif nombre_servicio == "Suiche7b":
    canvas.drawString(525,574, "X")
    canvas.drawString(227,554, "X")
    canvas.drawString(440,554, "X")
    aux = False
  elif nombre_servicio == "Tranred":
    canvas.drawString(525,574, "X")
    canvas.drawString(227,554, "X")
    canvas.drawString(440,554, "X")
    aux = False
  else :
    print("Realizo una selección invalida! porfavor intente nuevamente")
    aux = True


"""Area Fechas y Horas """

fecha_inicio = input("\nIngrese la fecha de inicio del incidente(DD/MM/YYYY): ")

hora_inicio = input("\nIngrese la hora de inicio del incidente(00:00 am/pm): ")

fecha_fin = input("\nIngrese la fecha de fin del incidente(DD/MM/YYYY): ")

hora_fin = input("\nIngrese la hora de fin del incidente(00:00 am/pm): ")


"""Area Seleccion de los campos"""


aux1 = True

while aux1 == True:
  print("""
  Porfavor seleccione uno de los siguientes campos:\n
  1)Incidente Tecnológico\n
  2)Proveedor Externo \n
  3)Mantenimiento \n
  """)
  seleccion_canales1 = input("-->")
  if seleccion_canales1 == "1":
    canvas.drawString(150,472, "X")
    aux1 = False
  elif seleccion_canales1 == "2":
    canvas.drawString(335,472, "X")
    aux1 = False
  elif seleccion_canales1 == "3":
    canvas.drawString(517,472, "X")
    aux1 = False
  else :
    print("Realizo una selección invalida! porfavor intente nuevamente")
    aux1 = True




"""Area Descripciones"""

print("DESCRIPCIONES")

maxlength = 80
descripcion=""
click.echo('\nIngrese la descripcion del incidente: ', nl=False)
while len(descripcion) < maxlength:
    temp = click.getchar()
    click.echo(temp, nl=False)
    descripcion += temp
descripcion1=""
click.echo(':', nl=False)
while len(descripcion1) < maxlength:
    temp = click.getchar()
    click.echo(temp, nl=False)
    descripcion1 += temp
descripcion2=""
click.echo(':', nl=False)
while len(descripcion2) < maxlength:
    temp = click.getchar()
    click.echo(temp, nl=False)
    descripcion2 += temp

a = input("\n\n\nPresione enter para rellenar el siguente punto!")


"""Area del motivo u origen"""


maxlength = 80
motivo=""
click.echo('\nIngrese el motivo u origen del incidente o evento: ', nl=False)
while len(motivo) < maxlength:
    temp = click.getchar()
    click.echo(temp, nl=False)
    motivo += temp
motivo1=""
click.echo('', nl=False)
while len(motivo1) < maxlength:
    temp = click.getchar()
    click.echo(temp, nl=False)
    motivo1 += temp

motivo2=""
click.echo('', nl=False)
while len(motivo2) < maxlength:
    temp = click.getchar()
    click.echo(temp, nl=False)
    motivo2 += temp
a = input("\n\n\nPresione enter para rellenar el siguente punto!")


"""Area servicios afectados"""
maxlength = 80
servicios_afectados=""
click.echo('\nIngrese los servicios afectados por el incidente: ', nl=False)
while len(servicios_afectados) < maxlength:
    temp = click.getchar()
    click.echo(temp, nl=False)
    servicios_afectados += temp
a = input("\n\n\nPresione enter para rellenar el siguente punto!")


"""Area Correctivos"""

maxlength = 75
correctivos=""
click.echo('\nIngrese los correctivos aplicados para solventar el incidente o evento : ', nl=False)
while len(correctivos) < maxlength:
    temp = click.getchar()
    click.echo(temp, nl=False)
    correctivos += temp
correctivos1=""
click.echo('', nl=False)
while len(correctivos1) < maxlength:
    temp = click.getchar()
    click.echo(temp, nl=False)
    correctivos1 += temp
correctivos2=""
click.echo('', nl=False)
while len(correctivos2) < maxlength:
    temp = click.getchar()
    click.echo(temp, nl=False)
    correctivos2 += temp
correctivos3=""
click.echo('', nl=False)
while len(correctivos3) < maxlength:
    temp = click.getchar()
    click.echo(temp, nl=False)
    correctivos3 += temp
correctivos4=""
click.echo('', nl=False)
while len(correctivos4) < maxlength:
    temp = click.getchar()
    click.echo(temp, nl=False)
    correctivos4 += temp

def generar():
  """Identificacion"""
  canvas.setFont('Helvetica', 12)
  canvas.rect(30,630,550, 15)
  canvas.drawString(250,632,'IDENTIFICACIÓN')
  canvas.setFont('Helvetica', 10)

  """Nombre Area"""
  canvas.rect(30,610,175, 20)
  canvas.drawString(40,617,'Área donde se detectó el incidente:')
  canvas.rect(205,610,375, 20)
  canvas.drawString(230,617,nombre_area)

  """Nombre Servico"""

  canvas.rect(30,590,100, 20)
  canvas.drawString(40,595,'Servicio:')
  canvas.rect(130,590,450, 20)
  canvas.drawString(150,595,nombre_servicio)


  """Canales"""
  canvas.rect(30,550,150, 40)
  canvas.drawString(40,565,'Canales:')
  canvas.rect(180,550,400, 40)
  canvas.drawString(200,575,'Oficinas')
  canvas.rect(240,574,8, 8)
  canvas.drawString(350,575,'IVR')
  canvas.rect(375,574,8, 8)
  canvas.drawString(500,575,'ATM')
  canvas.rect(525,574,8, 8)
  canvas.drawString(200,555,'POS')
  canvas.rect(227,554,8, 8)
  canvas.drawString(350,555,'Banca Por Internet')
  canvas.rect(440,554,8, 8)

  """Area Fechas y Horas"""
  canvas.rect(30,490,150, 60)
  canvas.drawString(40,520,'Fecha de inicio del incidente')
  canvas.drawString(40,510,'o evento tecnológico:')
  canvas.rect(180,490,125, 60)
  canvas.drawString(190,510,fecha_inicio+" "+hora_inicio)
  canvas.rect(305,490,150, 60)
  canvas.drawString(315,520,'Fecha de fin del incidente')
  canvas.drawString(315,510,'o evento tecnológico:')
  canvas.rect(455,490,125, 60)
  canvas.drawString(465,510,fecha_fin+" "+hora_fin)

  """Incidentes"""
  canvas.rect(30,465,550, 25)
  canvas.drawString(50,473,'Incidente Tecnológico')
  canvas.rect(150,472,10, 10)
  canvas.drawString(250,473,'Proveedor Externo')
  canvas.rect(335,472,10, 10)
  canvas.drawString(450,473,'Mantenimiento')
  canvas.rect(517,472,10, 10)

  """Area Descripciones"""


  canvas.setFont('Helvetica', 12)
  canvas.rect(30,450,550, 15)
  canvas.drawString(250,452,'DESCRIPCIONES')
  canvas.setFont('Helvetica', 10)
  canvas.rect(30,350,110, 100)
  canvas.drawString(40,418,'Descripción del')
  canvas.drawString(40,408,'incidente o evento')
  canvas.drawString(40,398,'tecnológico')
  canvas.rect(140,350,440, 100)

  canvas.drawString(150,430,descripcion)

  canvas.drawString(150,419,descripcion1)                     

  canvas.drawString(150,408,descripcion2)
  
  """Area del ingreso u origen"""
  canvas.setFont('Helvetica', 10)
  canvas.rect(30,250,110, 100)
  canvas.drawString(40,318,'Motivo u origen')
  canvas.drawString(40,308,'del incidente o')
  canvas.drawString(40,298,'evento tecnológico')
  canvas.rect(140,250,440, 100)
  canvas.setFont('Helvetica', 10)
  canvas.drawString(150,330,motivo)
  canvas.setFont('Helvetica', 10)
  canvas.drawString(150,319,motivo1)
  canvas.setFont('Helvetica', 10)
  canvas.drawString(150,308,motivo2)

  """Area servicios afectados"""
  canvas.setFont('Helvetica', 10)
  canvas.rect(30,150,110, 100)
  canvas.drawString(40,218,'Servicios afectados')
  canvas.drawString(40,208,'por el incidente o ')
  canvas.drawString(40,198,'evento tecnológico')
  canvas.rect(140,150,440, 100)

  canvas.drawString(150,208,servicios_afectados)

  """Correctivos"""
  canvas.setFont('Helvetica', 10)
  canvas.rect(30,50,110, 100)
  canvas.drawString(40,118,'Correctivos aplicados')
  canvas.drawString(40,108,'para solventar')
  canvas.drawString(40,98,'el incidente o ')
  canvas.drawString(40,88,'evento tecnológico')
  canvas.rect(140,50,440, 100)

  canvas.drawString(150,130,correctivos)

  canvas.drawString(150,119,correctivos1)

  canvas.drawString(150,108,correctivos2)

  canvas.drawString(150,97,correctivos3)
  
  canvas.drawString(150,97,correctivos4)
 
def editar():
  aux5= True
  while aux5 == True:
    ingreso_edicion = input("Ingrese el numero del campo que desea editar: ")
    if ingreso_edicion =="1":
      nombre = input("\nIngrese el NUEVO nombre del documento:")
      aux5 = False
    elif ingreso_edicion =="2":
      nombre_area = input("\nIngrese el NUEVO nombre del área donde se detectó el incidente: ")
      aux5 = False
    elif ingreso_edicion =="3":
      nombre_servicio = input("\nIngrese el NUEVO nombre del servicio donde se presento el incidente: ")
      aux5 = False
    elif ingreso_edicion =="4":
      aux = True
      print("""
  Porfavor seleccione uno de los canales:\n
  1)oficinas     2)IVR \n
  3)ATM           4)POS \n
  5)Banca Por Internet \n

  (Si el servicio es Suiche7b o Tranred, solo presionar ENTER)\n
  """)
      while aux == True:
        seleccion_canales = input("-->")
        if seleccion_canales == "1":
          canvas.drawString(240,574, "X")
          aux = False
        elif seleccion_canales == "2":
          canvas.drawString(375,574, "X")
          aux = False
        elif seleccion_canales == "3":
          canvas.drawString(525,574, "X")
          aux = False
        elif seleccion_canales == "4":
          canvas.drawString(227,554, "X")
          aux = False
        elif seleccion_canales == "5":
          canvas.drawString(440,554, "X")
          aux = False
        elif nombre_servicio == "Suiche7b":
          canvas.drawString(525,574, "X")
          canvas.drawString(227,554, "X")
          canvas.drawString(440,554, "X")
          aux = False
        elif nombre_servicio == "Tranred":
          canvas.drawString(525,574, "X")
          canvas.drawString(227,554, "X")
          canvas.drawString(440,554, "X")
          aux = False
        else :
          print("Realizo una selección invalida! porfavor intente nuevamente")
          aux = True
      aux5 = False
    elif ingreso_edicion =="5":
      aux1 = True
      while aux1 == True:
            print("""
  Porfavor seleccione uno de los siguientes campos:\n
  1)Incidente Tecnológico\n
  2)Proveedor Externo \n
  3)Mantenimiento \n
  """)
            seleccion_canales1 = input("-->")
            if seleccion_canales1 == "1":
              canvas.drawString(150,472, "X")
              aux1 = False
            elif seleccion_canales1 == "2":
              canvas.drawString(335,472, "X")
              aux1 = False
            elif seleccion_canales1 == "3":
              canvas.drawString(517,472, "X")
              aux1 = False
            else :
              print("Realizo una selección invalida! porfavor intente nuevamente")
              aux1 = True
      aux5 = False
    elif ingreso_edicion =="6":        
      fecha_inicio = input("\nIngrese la NUEVA fecha de inicio del incidente(DD/MM/YYYY): ")
      aux5 = False
    elif ingreso_edicion =="7":
      hora_inicio = input("\nIngrese la NUEVA hora de inicio del incidente(00:00 am/pm): ")
      aux5 = False
    elif ingreso_edicion =="8":
          fecha_fin = input("\nIngrese la NUEVA fecha de fin del incidente(DD/MM/YYYY): ")
          aux5 = False
    elif ingreso_edicion =="9":
          hora_fin = input("\nIngrese la NUEVA hora de fin del incidente(00:00 am/pm): ")
          aux5 = False
    elif ingreso_edicion =="10":
          maxlength = 80
          descripcion=""
          click.echo('\nIngrese la NUEVA descripcion del incidente: ', nl=False)
          while len(descripcion) < maxlength:
            temp = click.getchar()
            click.echo(temp, nl=False)
            descripcion += temp
          descripcion1=""
          click.echo(':', nl=False)
          while len(descripcion1) < maxlength:
            temp = click.getchar()
            click.echo(temp, nl=False)
            descripcion1 += temp
          descripcion2="" 
          click.echo(':', nl=False)
          while len(descripcion2) < maxlength:
            temp = click.getchar()
            click.echo(temp, nl=False)
            descripcion2 += temp
          aux5 = False
    elif ingreso_edicion =="11":
          maxlength = 80
          motivo=""
          click.echo('\nIngrese el NUEVO motivo u origen del incidente o evento: ', nl=False)
          while len(motivo) < maxlength:
            temp = click.getchar()
            click.echo(temp, nl=False)
            motivo += temp
          motivo1=""
          click.echo('', nl=False)
          while len(motivo1) < maxlength:
            temp = click.getchar()
            click.echo(temp, nl=False)
            motivo1 += temp

          motivo2=""
          click.echo('', nl=False)
          while len(motivo2) < maxlength:
            temp = click.getchar()
            click.echo(temp, nl=False)
            motivo2 += temp
          aux5 = False
    elif ingreso_edicion =="12":
          maxlength = 80
          servicios_afectados=""
          click.echo('\nIngrese los NUEVOS servicios afectados por el incidente: ', nl=False)
          while len(servicios_afectados) < maxlength:
            temp = click.getchar()
            click.echo(temp, nl=False)
            servicios_afectados += temp
          aux5 = False
    elif ingreso_edicion =="13":
          maxlength = 75
          correctivos=""
          click.echo('\nIngrese los NUEVOS correctivos aplicados para solventar el incidente o evento : ', nl=False)
          while len(correctivos) < maxlength:
            temp = click.getchar()
            click.echo(temp, nl=False)
            correctivos += temp
          correctivos1=""
          click.echo('', nl=False)
          while len(correctivos1) < maxlength:
            temp = click.getchar()
            click.echo(temp, nl=False)
            correctivos1 += temp
          correctivos2=""
          click.echo('', nl=False)
          while len(correctivos2) < maxlength:
            temp = click.getchar()
            click.echo(temp, nl=False)
            correctivos2 += temp
          correctivos3=""
          click.echo('', nl=False)
          while len(correctivos3) < maxlength:
            temp = click.getchar()
            click.echo(temp, nl=False)
            correctivos3 += temp
          correctivos4=""
          click.echo('', nl=False)
          while len(correctivos4) < maxlength:
            temp = click.getchar()
            click.echo(temp, nl=False)
            correctivos4 += temp
          aux5 = False
    else :
          print("\n Ingreso una opcion invalida! Porfavor Intente nuevamente")
          aux5 == True
  generar()


def main():
  aux3 = True
  while aux3 == True: 
    print("\nPresione \n1)Para Generar El Documento\n2)Para Editar El Documento")
    a = input("-->")
    if a == "1":
      generar()
      canvas.save()
      print("\nSu reporte se ha creado correctamente")
      aux3= False
    elif a == "2":
      print("\n¿Cual de las opciones desea editar?\n")
      print("1) Nombre del documento: "+nombre+".pdf"+"\n")
      print("2) Nombre del area: "+nombre_area+"\n")
      print("3) Nombre del servicio: "+nombre_servicio+"\n")
      print("4) Selección: "+seleccion_canales+""""\n
                Porfavor seleccione uno de los canales:\n
                1)oficinas     2)IVR \n
                3)ATM           4)POS \n
                5)Banca Por Internet \n
                """)
      print("5) Selección: "+seleccion_canales1+"""\n
                Porfavor seleccione uno de los siguientes campos:\n
                1)Incidente Tecnológico\n
                2)Proveedor Externo \n
                3)Mantenimiento \n
            """)
      print("6) Fecha de Inicio del Incidente : "+fecha_inicio+"\n")
      print("7) Hora de Inico del Incidente: "+hora_inicio+"\n")
      print("8) Fecha de Fin del Incidente: "+fecha_fin+"\n")
      print("9) Hora de Fin del Incidente: "+hora_fin+"\n")
      print("10) Descripcion: "+descripcion+descripcion1+descripcion2+"\n")
      print("11) Motivo: "+motivo+motivo1+motivo2+"\n")
      print("12)nombre del documento: "+servicios_afectados+"\n")
      print("13)nombre del documento: "+correctivos+correctivos1+correctivos2+correctivos3+correctivos4+"\n")
      editar()
      canvas.save()
      print("\nSu reporte se ha creado correctamente")
      aux3 = False

    else: 
      print("\n Ingreso una opcion invalida! Porfavor Intente nuevamente")
      aux3== True

main()    
