from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

print(""" 
  000000    0    0    000000
  0    0    0    0    0
  00000     0    0    0
  0    0     0  0     0
  000000      00      000000
""")

nombre = input("Ingrese el nombre del documento:")
canvas = canvas.Canvas(nombre+".pdf", pagesize=letter)
canvas.setStrokeColorRGB(0, 0, 0)
canvas.setLineWidth(.3)
canvas.setFont('Helvetica', 9)
canvas.drawImage("logo.png", 30,650, width=200, height=150)
canvas.drawString(82,700,"RIF: J-000029709")
canvas.setFont('Helvetica', 15)
canvas.drawString(125,660,"Informe de Eventos, Fallas o Incidencias [ Inicio/Cierre ]")


"""Area1"""
canvas.setFont('Helvetica', 12)
canvas.rect(30,630,550, 15)
canvas.drawString(250,632,'IDENTIFICACIÓN')
canvas.setFont('Helvetica', 10)
"""Area2"""
canvas.rect(30,610,175, 20)
canvas.drawString(40,617,'Área donde se detectó el incidente:')
canvas.rect(205,610,375, 20)
nombre_area = input("Ingrese el nombre del área donde se detectó el incidente:")
canvas.drawString(230,617,nombre_area)
"""Area3"""
canvas.rect(30,590,100, 20)
canvas.drawString(40,595,'Servicio:')
canvas.rect(130,590,450, 20)
nombre_servicio = input("Ingrese el nombre del servicio donde se presento el incidente:")
canvas.drawString(150,595,nombre_servicio)
"""Area4"""
canvas.rect(30,550,150, 40)
canvas.drawString(40,565,'Canales:')
canvas.rect(180,550,400, 40)
canvas.drawString(200,575,'Oficinas')
canvas.rect(240,574,10, 10)
canvas.drawString(350,575,'IVR')
canvas.rect(375,574,10, 10)
canvas.drawString(500,575,'ATM')
canvas.rect(525,574,10, 10)
canvas.drawString(200,555,'POS')
canvas.rect(227,554,10, 10)
canvas.drawString(350,555,'Banca Por Internet')
canvas.rect(440,554,10, 10)
"""Area5"""
canvas.rect(30,490,150, 60)
canvas.drawString(40,520,'Fecha de inicio del incidente')
canvas.drawString(40,510,'o evento tecnológico:')
canvas.rect(180,490,125, 60)
fecha_inicio = input("Ingrese la fecha de inicio del incidente(DD/MM/YYYY):")
hora_inicio = input("Ingrese la hora de inicio del incidente(00:00 am/pm):")
canvas.drawString(190,510,fecha_inicio+" "+hora_inicio)
canvas.rect(305,490,150, 60)
canvas.drawString(315,520,'Fecha de fin del incidente')
canvas.drawString(315,510,'o evento tecnológico:')
canvas.rect(455,490,125, 60)
fecha_fin = input("Ingrese la fecha de fin del incidente(DD/MM/YYYY):")
hora_fin = input("Ingrese la hora de fin del incidente(00:00 am/pm):")
canvas.drawString(465,510,fecha_fin+" "+hora_fin)
"""Area6"""
canvas.rect(30,465,550, 25)
canvas.drawString(50,473,'Incidente Tecnológico')
canvas.rect(150,472,10, 10)
canvas.drawString(250,473,'Proveedor Externo')
canvas.rect(335,472,10, 10)
canvas.drawString(450,473,'Mantenimiento')
canvas.rect(517,472,10, 10)
"""Area7"""
canvas.setFont('Helvetica', 12)
canvas.rect(30,450,550, 15)
canvas.drawString(250,452,'DESCRIPCIONES')
"""Area8"""
canvas.setFont('Helvetica', 10)
print("DESCRIPCIONES")
canvas.rect(30,350,110, 100)
canvas.drawString(40,418,'Descripción del')
canvas.drawString(40,408,'incidente o evento')
canvas.drawString(40,398,'tecnológico')
canvas.rect(140,350,440, 100)
descripcion = input("Ingrese la descripcion del incidente: ")
canvas.drawString(150,418,descripcion)
"""Area8"""
canvas.setFont('Helvetica', 10)
canvas.rect(30,250,110, 100)
canvas.drawString(40,318,'Motivo u origen')
canvas.drawString(40,308,'del incidente o')
canvas.drawString(40,298,'evento tecnológico')
canvas.rect(140,250,440, 100)
motivo = input("Ingrese el motivo u origen del incidente: ")
canvas.drawString(150,318,descripcion)
"""Area9"""
canvas.setFont('Helvetica', 10)
canvas.rect(30,150,110, 100)
canvas.drawString(40,218,'Servicios afectados')
canvas.drawString(40,208,'por el incidente o ')
canvas.drawString(40,198,'evento tecnológico')
canvas.rect(140,150,440, 100)
servicios_afectados = input("Ingrese los servicios afectados por el incidente: ")
canvas.drawString(150,218,servicios_afectados)
"""Area10"""
canvas.setFont('Helvetica', 10)
canvas.rect(30,50,110, 100)
canvas.drawString(40,118,'Correctivos aplicados')
canvas.drawString(40,108,'para solventar')
canvas.drawString(40,98,'el incidente o ')
canvas.drawString(40,88,'evento tecnológico')
canvas.rect(140,50,440, 100)
correctivos = input("Ingrese los correctivos aplicados para solventar el incidente: ")
canvas.drawString(150,118,correctivos)


canvas.save()
