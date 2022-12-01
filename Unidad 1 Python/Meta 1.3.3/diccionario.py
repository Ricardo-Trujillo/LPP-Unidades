
#Diccionarios
#Cuando requerimos LLave-dato|Key-Data

alumnos=["AVALOS GODOY LEONARDO",
         "BECERRA PERAZA ERICK ARTURO",
         "BRAMBILA MOLINA LUIS ADRIAN",
         "CASTRO ANTONIO BRANDON ALBERTO",
         "DE LA CRUZ CHAVEZ JOSE EDUARDO",
         "ESPINO NUÑEZ SHERLYN",
         "GUERRA CERVANTES OMAR EDUARDO",
         "GUERRA HABANA JOSE GUSTAVO",
         "GUTIERREZ SANCHEZ VALERIA KAREY",
          "GUTIÉRREZ RUIZ FRANCISCO GABRIEL",
         "MACHADO MERAZ ULISES JOEL",
         "MENDOZA NAVARRO BRANDON ABRAHAM",
         "PINEDA RAMIREZ JAFET JACOB",
         "RAMIREZ SANCHEZ ANGEL ALEJANDRO",
         "RODRIGUEZ CANDIA VICTOR MANUEL",
         "RODRIGUEZ ROSAS LUIS ENRIQUE",
         "SANCHEZ ZARAGOZA EDUARDO ARTURO",
         "SEGURA SOLIS VALENTINA",
         "VELARDE MORALES LUIS EMILIO"]

diccionario ={1282003:alumnos[0],
              1262844:alumnos[1],
              1264791:alumnos[2],
              1284997:alumnos[3],
              1282778:alumnos[4],
              1281160:alumnos[5],
              1281859:alumnos[6],
              1273586:alumnos[7],
              1282379:alumnos[8],
              1261897:alumnos[9],
              1261836:alumnos[10],
              1282292:alumnos[11],
              1273987:alumnos[12],
              1282041:alumnos[13],
              1259644:alumnos[14],
              1275919:alumnos[15],
              1280942:alumnos[16],
              1282007:alumnos[17],
              1273159:alumnos[18]}

print(diccionario)
print("\n")
# Demuestre que el estudiante BRAMBILA MOLINA LUIS ADRIAN está en el grupo
print("BRAMBILA MOLINA LUIS ADRIAN" in diccionario.values())
print("\n")

#Demuestre que el estudiante cuya matrícula 1272428 no está en el grupo
print(diccionario.get(1272428),"No esta en el grupo")
print("\n")

# Agregue al estudiante VELAZQUEZ SANCHEZ DIEGO ALEJANDRO 1282923 al diccionario.
alumnos.append("VELAZQUEZ SANCHEZ DIEGO ALEJANDRO ")
n = len(alumnos)
diccionario[1282923]=alumnos[n-1]
print(diccionario)