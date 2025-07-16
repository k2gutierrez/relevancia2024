#import os
#from dotenv import load_dotenv
import json
import requests
import streamlit as st
#load_dotenv()

#api = os.environ.get("API")
api = st.secrets["API"]

apiUrl = "https://api.monday.com/v2"
headers = {"Authorization" : api}

st.set_page_config(
    page_title="Euncet-Cedem",
    page_icon="./triangulo.png",
)

#query = '{boards(limit:1) { name id description items_page { items { name column_values{id type text } } } } }'
#data = {'query' : query}

#r = requests.post(url=apiUrl, json=data, headers=headers) # make request

#st.write(r.json())


#query3 = 'mutation{ create_item (board_id:7601959436, item_name:"Test") { id } }'
#data = {'query' : query3}

#r = requests.post(url=apiUrl, json=data, headers=headers) # make request
#print(r.json())


#query5 = 'mutation ($boardid: ID!, $myItemName: String!, $columnVals: JSON!) { create_item (board_id:$boardid, item_name:$myItemName, column_values:$columnVals) { id } }'
#vars = {
#    'boardid' : '7601959436',
#    'myItemName' : 'Hello everyone!',
#    'columnVals' : json.dumps({
#    'texto__1' : '70',
#    'texto8__1' : 'coach'
# })
#}

#data = {'query' : query5, 'variables' : vars}
#r = requests.post(url=apiUrl, json=data, headers=headers) # make request
#print(r.json())

def sendRelevancia(consejo, encuestado, masR, menosR, email):
    try:
        if consejo == "Consejo 1. Dunia Guzman":
            verificador = consejo1.index(encuestado)
            if email.lower() != email1[verificador]:
                return st.error("El email no coincide con el que registraste para el Máster! Intenta nuevamente")

        if consejo == "Consejo 2. José Luis Rodríguez":
            verificador = consejo2.index(encuestado)
            if email.lower() != email2[verificador]:
                return st.error("El email no coincide con el que registraste para el Máster! Intenta nuevamente")

        if consejo == "Consejo 3. Juan Carlos Ruvalcaba":
            verificador = consejo3.index(encuestado)
            if email.lower() != email3[verificador]:
                return st.error("El email no coincide con el que registraste para el Máster! Intenta nuevamente")

        if consejo == "Consejo 4. Mario Humberto García":
            verificador = consejo4.index(encuestado)
            if email.lower() != email4[verificador]:
                return st.error("El email no coincide con el que registraste para el Máster! Intenta nuevamente")

        if consejo == "Consejo 5. Roberto Becerra":
            verificador = consejo5.index(encuestado)
            if email.lower() != email5[verificador]:
                return st.error("El email no coincide con el que registraste para el Máster! Intenta nuevamente")

        if consejo == "Consejo 6. Alfonso Pompa":
            verificador = consejo6.index(encuestado)
            if email.lower() != email6[verificador]:
                return st.error("El email no coincide con el que registraste para el Máster! Intenta nuevamente")

        id = consejos.index(consejo)
        bId = IDsConsejos[id]

        tipo = ""
        if encuestado in coaches:
            tipo = "coach"
        else:
            tipo = "alumno"
        
        if masR == "" or masR == None:
            status=st.error("No seleccionaste a nadie como el más relevante")
            return status
        elif menosR == None or menosR == "":
            status= st.error("No seleccionaste a nadie como el menos relevante")
            return status

        ## Verificación de registro en tablero
        q = '{boards(ids: '+ bId +') { name id description items_page { items { name column_values{id type text } } } } }'
        data = {'query' : q}
        res = requests.post(url=apiUrl, json=data, headers=headers) # make request
        res_json = res.json()
        res_list = res_json["data"]["boards"][0]["items_page"]["items"]
        
        if len(res_list) == 0:
            query5 = 'mutation ($boardid: ID!, $myItemName: String!, $columnVals: JSON!) { create_item (board_id:$boardid, item_name:$myItemName, column_values:$columnVals) { id } }'
            vars = {
                'boardid' : bId,
                'myItemName' : encuestado, # nombre
                'columnVals' : json.dumps({
                'texto__1' : masR, # más relevante
                'dup__of_m_s_relevante__1' : menosR, # menos relevante
                'texto8__1' : tipo # tipo
            })
            }

            data = {'query' : query5, 'variables' : vars}
            r = requests.post(url=apiUrl, json=data, headers=headers) # make request
            if r:
                status = st.success("Se ha registrado exitosamente!")
                return status
        
        else:
            for i in res_list:
                if i["name"] == encuestado:
                    return st.warning("Ya has realizado la encuesta!")
            
            query5 = 'mutation ($boardid: ID!, $myItemName: String!, $columnVals: JSON!) { create_item (board_id:$boardid, item_name:$myItemName, column_values:$columnVals) { id } }'
            vars = {
                'boardid' : bId,
                'myItemName' : encuestado, # nombre
                'columnVals' : json.dumps({
                'texto__1' : masR, # más relevante
                'dup__of_m_s_relevante__1' : menosR, # menos relevante
                'texto8__1' : tipo # tipo
            })
            }

            data = {'query' : query5, 'variables' : vars}
            r = requests.post(url=apiUrl, json=data, headers=headers) # make request
            if r:
                status = st.success("Se ha registrado exitosamente!")
                return status
    except:
        return

def sendCali(boardid, nombre, consejo, calificacion):
    try:

        query1 = 'mutation ($boardid: ID!, $myItemName: String!, $columnVals: JSON!) { create_item (board_id:$boardid, item_name:$myItemName, column_values:$columnVals) { id } }'
        vars = {
            'boardid' : boardid,
            'myItemName' : nombre, # nombre
            'columnVals' : json.dumps({
            'texto__1' : consejo, # más relevante
            'texto_1__1' : calificacion, # menos relevante
        })
        }

        data = {'query' : query1, 'variables' : vars}
        r = requests.post(url=apiUrl, json=data, headers=headers) # make request
        if r:
            status = st.success("Calificaciones registradas con éxito")
            return status
    except:
        return st.error("Ha ocurrido un error, intenta nuevamente")

def getconsejos(ids, consejo, consejoNum):
    consejo_actual = []
    for i in consejo:
        if i != consejo[0]:
            consejo_actual.append(i)
    query2 = '{boards(ids:'+ str(ids) +') { name id description items_page { items { name column_values{id type text } } } } }'

    data = {'query' : query2}

    r = requests.post(url=apiUrl, json=data, headers=headers) # make request

    rf = r.json()

    rf_list = rf["data"]["boards"][0]["items_page"]["items"]

    if len(rf_list) < len(consejo):
        return st.warning("Faltan personas por contestar la encuesta")
    elif len(rf_list) > len(consejo):
        return st.error("Hay más registros de calificaciones de lo esperado")

    alumni = []
    #st.write(rf_list)

    for i in consejo_actual:
        alumnis = {'nombre': i, 'calis': [], 'final': '0'}
        alumni.append(alumnis)

    if len(alumni) == 3:
        for i in rf_list:
            if i["column_values"][2]["text"] == "coach":
                for a in alumni:
                    if a['nombre'] == i["column_values"][0]["text"]:
                        a['calis'].insert(0, 100)
                    elif a['nombre'] == i["column_values"][1]["text"]:
                        a['calis'].insert(0, 60)
                    else:
                        a['calis'].insert(0, 80)
            
            elif i["column_values"][2]["text"] == "alumno":
                for a in alumni:
                    if a['nombre'] == i["column_values"][0]["text"]:
                        a['calis'].append(100)
                    elif a['nombre'] == i["column_values"][1]["text"]:
                        a['calis'].append(60)

    elif len(alumni) > 3:
        for i in rf_list:
            if i["column_values"][2]["text"] == "coach":
                for a in alumni:
                    if a['nombre'] == i["column_values"][0]["text"]:
                        a['calis'].insert(0, 100)
                    elif a['nombre'] == i["column_values"][1]["text"]:
                        a['calis'].insert(0, 60)
                    else:
                        a['calis'].insert(0, 80)
            
            elif i["column_values"][2]["text"] == "alumno":
                for a in alumni:
                    if a['nombre'] == i["column_values"][0]["text"]:
                        a['calis'].append(100)
                    elif a['nombre'] == i["column_values"][1]["text"]:
                        a['calis'].append(60)
                    else:
                        a['calis'].append(80)
    calificacion(alumni, consejoNum)

def calificacion(listfull, consejo):
    for i in listfull:
        nom = i["nombre"]
        caliC = (i["calis"][0])
        caliA = 0
        ind = len(i["calis"])-1
        for a in i["calis"]:
            caliA += a
        coach = caliC * .6
        alumnos = ((caliA - caliC)/ind) * .4
        total = coach + alumnos
        i['final'] = str(total)
        result = st.write(f"{nom}: {total}")
    #return result
    if st.button("Registrar en monday"):
        newquery = '{boards(ids: 7633182192) { name id description items_page { items { name column_values{id type text } } } } }'
        data = {'query' : newquery}
        r = requests.post(url=apiUrl, json=data, headers=headers) # make request
        rf = r.json()
        rf_list = rf["data"]["boards"][0]["items_page"]["items"]
        for i in listfull:
            if len(rf_list) == 0:
                sendCali(7633182192, i["nombre"], consejo, i["final"])
            
            for a in rf_list:
                if a["name"] == i["nombre"]:
                    return st.warning("Ya existen los registros en el tablero de monday!")

            sendCali(7633182192, i["nombre"], consejo, i["final"])
            #función para mandar a monday

    


IDsConsejos = ['7601959436', '7605844793', '7605845746', '7605846147', '7605846488', '7605846943']
consejos = ["Consejo 1. Dunia Guzman", "Consejo 2. José Luis Rodríguez", "Consejo 3. Juan Carlos Ruvalcaba", "Consejo 4. Mario Humberto García", "Consejo 5. Roberto Becerra", "Consejo 6. Alfonso Pompa"]
coaches = ["Dunia Guzman", "José Luis Rodríguez", "Juan Carlos Ruvalcaba", "Mario Humberto García", "Roberto Becerra", "Alfonso Pompa"]

consejo1 = ["Dunia Guzman", "Gabriela Sánchez", "Héctor Arias", "José Antonio Carballar"]
email1 = ["dguzman@akator.com", "gabriela.sanchez@dportenis.com.mx", "hector.arias.solorzano@gmail.com", "jose.antonio.carballar@accyflor.mx"]

consejo2 = ["José Luis Rodríguez", "Christian Flores", "Lucía Félix", "Nicolás Sañudo"]
email2 = ["jlrdzpro@gmail.com", "cristian.flores@accyflor.mx", "luciafelix24@hotmail.com", "nicolasanudo@gmail.com"]

consejo3 = ["Juan Carlos Ruvalcaba", "Armando Flores", "José Miguel Fernández", "Óscar Sánchez Reyes", "Rodolfo Becerra"]
email3 = ["jruvalcaba0114@gmail.com", "a.flores@accyflor.mx", "josemiguel_fdz@hotmail.com", "saos85@hotmail.com", "becerrarodolfo15@gmail.com"]

consejo4 = ["Mario Humberto García", "David Félix", "Emilio Sánchez", "Ildefonso Aviléz", "Marco Flores"]
email4 = ["mariogarcia@viveseguro.com", "davidfelixc7@gmail.com", "emilio.sanchez@dportenis.com.mx", "ilde.avilez@gmail.com", "mfloresgarcia207@gmail.com"]

consejo5 = ["Roberto Becerra", "Fernando Oropeza", "Germán Vázquez", "Julián Cajigas", "Ronald Ramírez"]
email5 = ["robertobecerrar@gmail.com", "fer@brandmandco.com", "german.vazquez@accyflor.mx", "julian.cajigas@gmail.com", "ramirezosorioronald@gmail.com"]

consejo6 = ["Alfonso Pompa", "Francisco Madero", "José Maldonado", "Marissa De la Rosa", "Óscar Sánchez Osuna"]
email6 = ["apompa@tec.mx", "francisco.madero17@gmail.com", "jmaldonado@gaservicio.com", "marissa@qvoz.com", "oscar.sanchez@dportenis.com.mx"]






st.title(":blue[Evaluación de Relevancia]")
st.subheader("Julio")
consejo = st.selectbox("Selecciona tu Consejo", ("Consejos", "Consejo 1. Dunia Guzman", "Consejo 3. Juan Carlos Ruvalcaba", 
                                                 "Consejo 4. Mario Humberto García", "Consejo 5. Roberto Becerra", "Consejo 6. Alfonso Pompa", "Selecciona tu Consejo"))

if consejo == "Consejo 1. Dunia Guzman":
    encuestado = st.selectbox("Selecciona tu nombre", ("-----", "Dunia Guzman", "Gabriela Sánchez", "Héctor Arias", "José Antonio Carballar"))
    relevante = None
    menos_relevante = None

    if encuestado == "Dunia Guzman":

        consejoR = consejo1[1:4]
        consejoNR = consejo1[1:4]
        st.divider()
        relevante = st.radio("Selecciona al más relevante", consejoR, index=None, horizontal=False)
        st.divider()
        if relevante == "Gabriela Sánchez":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)
        
        elif relevante == "Héctor Arias":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        elif relevante == "José Antonio Carballar":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        else:
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)
            
    
    elif encuestado == "Gabriela Sánchez":

        consejoR = consejo1[2:4]
        consejoNR = consejo1[2:4]
        st.divider()
        relevante = st.radio("Selecciona al más relevante", consejoR, index=None, horizontal=False)
        st.divider()
        
        if relevante == "Héctor Arias":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        elif relevante == "José Antonio Carballar":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        else:
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

    
    elif encuestado == "Héctor Arias":

        consejoR = ["Gabriela Sánchez", "José Antonio Carballar"]
        consejoNR = ["Gabriela Sánchez", "José Antonio Carballar"]
        st.divider()
        relevante = st.radio("Selecciona al más relevante", consejoR, index=None, horizontal=False)
        st.divider()
        if relevante == "Gabriela Sánchez":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)
        
        elif relevante == "José Antonio Carballar":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        else:
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)


    elif encuestado == "José Antonio Carballar":

        consejoR = ["Gabriela Sánchez", "Héctor Arias"]
        consejoNR = ["Gabriela Sánchez", "Héctor Arias"]
        st.divider()
        relevante = st.radio("Selecciona al más relevante", consejoR, index=None, horizontal=False)
        st.divider()
        if relevante == "Gabriela Sánchez":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)
        
        elif relevante == "Héctor Arias":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        else:
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)
    
    email = st.text_input("Ingresa el email con el que te registraste al Máster:")
    if st.button("Enviar encuesta", type='secondary'):
            send = sendRelevancia(consejo, encuestado, relevante, menos_relevante, email)





elif consejo == "Consejo 3. Juan Carlos Ruvalcaba":
    encuestado = st.selectbox("Selecciona tu nombre", ("-----", "Juan Carlos Ruvalcaba", "Armando Flores", "José Miguel Fernández", "Óscar Sánchez Reyes", "Rodolfo Becerra"))
    relevante = None
    menos_relevante = None
    if encuestado == "Juan Carlos Ruvalcaba":
        consejoR = consejo3[1:5]
        consejoNR = consejo3[1:5]
        st.divider()
        relevante = st.radio("Selecciona al más relevante", consejoR, index=None, horizontal=False)
        st.divider()
        if relevante == "Armando Flores":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)
        
        elif relevante == "José Miguel Fernández":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        elif relevante == "Óscar Sánchez Reyes":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)
        
        elif relevante == "Rodolfo Becerra":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        else:
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

    
    elif encuestado == "Armando Flores":
        consejoR = consejo3[2:5]
        consejoNR = consejo3[2:5]
        st.divider()
        relevante = st.radio("Selecciona al más relevante", consejoR, index=None, horizontal=False)
        st.divider()
        
        if relevante == "José Miguel Fernández":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        elif relevante == "Óscar Sánchez Reyes":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        elif relevante == "Rodolfo Becerra":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        else:
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

    
    elif encuestado == "José Miguel Fernández":
        consejoR = ["Armando Flores", "Óscar Sánchez Reyes", "Rodolfo Becerra"]
        consejoNR = ["Armando Flores", "Óscar Sánchez Reyes", "Rodolfo Becerra"]
        st.divider()
        relevante = st.radio("Selecciona al más relevante", consejoR, index=None, horizontal=False)
        st.divider()
        if relevante == "Armando Flores":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)
        
        elif relevante == "Óscar Sánchez Reyes":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)
        
        elif relevante == "Rodolfo Becerra":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        else:
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)


    elif encuestado == "Óscar Sánchez Reyes":
        consejoR = ["Armando Flores", "José Miguel Fernández", "Rodolfo Becerra"]
        consejoNR = ["Armando Flores", "José Miguel Fernández", "Rodolfo Becerra"]
        st.divider()
        relevante = st.radio("Selecciona al más relevante", consejoR, index=None, horizontal=False)
        st.divider()
        if relevante == "Armando Flores":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)
        
        elif relevante == "José Miguel Fernández":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        elif relevante == "Rodolfo Becerra":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        else:
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

    elif encuestado == "Rodolfo Becerra":
        consejoR = consejo3[1:4]
        consejoNR = consejo3[1:4]
        st.divider()
        relevante = st.radio("Selecciona al más relevante", consejoR, index=None, horizontal=False)
        st.divider()
        if relevante == "Armando Flores":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)
        
        elif relevante == "José Miguel Fernández":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        elif relevante == "Óscar Sánchez Reyes":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        else:
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)
    
    email = st.text_input("Ingresa el email con el que te registraste al Máster:")
    if st.button("Enviar encuesta", type='secondary'):
            send = sendRelevancia(consejo, encuestado, relevante, menos_relevante, email)


elif consejo == "Consejo 4. Mario Humberto García":
    encuestado = st.selectbox("Selecciona tu nombre", ("-----", "Mario Humberto García", "David Félix", "Emilio Sánchez", "Ildefonso Aviléz", "Marco Flores"))
    relevante = None
    menos_relevante = None
    if encuestado == "Mario Humberto García":
        consejoR = consejo4[1:5]
        consejoNR = consejo4[1:5]
        st.divider()
        relevante = st.radio("Selecciona al más relevante", consejoR, index=None, horizontal=False)
        st.divider()
        if relevante == "David Félix":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)
        
        elif relevante == "Emilio Sánchez":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        elif relevante == "Ildefonso Aviléz":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)
        
        elif relevante == "Marco Flores":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        else:
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

    
    elif encuestado == "David Félix":
        consejoR = consejo4[2:5]
        consejoNR = consejo4[2:5]
        st.divider()
        relevante = st.radio("Selecciona al más relevante", consejoR, index=None, horizontal=False)
        st.divider()
        
        if relevante == "Emilio Sánchez":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        elif relevante == "Ildefonso Aviléz":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        elif relevante == "Marco Flores":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        else:
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

    
    elif encuestado == "Emilio Sánchez":
        consejoR = ["David Félix", "Ildefonso Aviléz", "Marco Flores"]
        consejoNR = ["David Félix", "Ildefonso Aviléz", "Marco Flores"]
        st.divider()
        relevante = st.radio("Selecciona al más relevante", consejoR, index=None, horizontal=False)
        st.divider()
        if relevante == "David Félix":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)
        
        elif relevante == "Ildefonso Aviléz":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)
        
        elif relevante == "Marco Flores":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        else:
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)


    elif encuestado == "Ildefonso Aviléz":
        consejoR = ["David Félix", "Emilio Sánchez", "Marco Flores"]
        consejoNR = ["David Félix", "Emilio Sánchez", "Marco Flores"]
        st.divider()
        relevante = st.radio("Selecciona al más relevante", consejoR, index=None, horizontal=False)
        st.divider()
        if relevante == "David Félix":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)
        
        elif relevante == "Emilio Sánchez":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        elif relevante == "Marco Flores":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        else:
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

    elif encuestado == "Marco Flores":
        consejoR = consejo4[1:4]
        consejoNR = consejo4[1:4]
        st.divider()
        relevante = st.radio("Selecciona al más relevante", consejoR, index=None, horizontal=False)
        st.divider()
        if relevante == "David Félix":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)
        
        elif relevante == "Emilio Sánchez":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        elif relevante == "Ildefonso Aviléz":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        else:
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)
    
    email = st.text_input("Ingresa el email con el que te registraste al Máster:")
    if st.button("Enviar encuesta", type='secondary'):
            send = sendRelevancia(consejo, encuestado, relevante, menos_relevante, email)


elif consejo == "Consejo 5. Roberto Becerra":
    encuestado = st.selectbox("Selecciona tu nombre", ("-----", "Roberto Becerra", "Fernando Oropeza", "Germán Vázquez", "Julián Cajigas", "Ronald Ramírez"))
    relevante = None
    menos_relevante = None
    if encuestado == "Roberto Becerra":
        consejoR = consejo5[1:5]
        consejoNR = consejo5[1:5]
        st.divider()
        relevante = st.radio("Selecciona al más relevante", consejoR, index=None, horizontal=False)
        st.divider()
        if relevante == "Fernando Oropeza":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)
        
        elif relevante == "Germán Vázquez":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        elif relevante == "Julián Cajigas":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)
        
        elif relevante == "Ronald Ramírez":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        else:
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

    
    elif encuestado == "Fernando Oropeza":
        consejoR = consejo5[2:5]
        consejoNR = consejo5[2:5]
        st.divider()
        relevante = st.radio("Selecciona al más relevante", consejoR, index=None, horizontal=False)
        st.divider()
        
        if relevante == "Germán Vázquez":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        elif relevante == "Julián Cajigas":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        elif relevante == "Ronald Ramírez":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        else:
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

    
    elif encuestado == "Germán Vázquez":
        consejoR = ["Fernando Oropeza", "Julián Cajigas", "Ronald Ramírez"]
        consejoNR = ["Fernando Oropeza", "Julián Cajigas", "Ronald Ramírez"]
        st.divider()
        relevante = st.radio("Selecciona al más relevante", consejoR, index=None, horizontal=False)
        st.divider()
        if relevante == "Fernando Oropeza":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)
        
        elif relevante == "Julián Cajigas":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)
        
        elif relevante == "Ronald Ramírez":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        else:
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)


    elif encuestado == "Julián Cajigas":
        consejoR = ["Fernando Oropeza", "Germán Vázquez", "Ronald Ramírez"]
        consejoNR = ["Fernando Oropeza", "Germán Vázquez", "Ronald Ramírez"]
        st.divider()
        relevante = st.radio("Selecciona al más relevante", consejoR, index=None, horizontal=False)
        st.divider()
        if relevante == "Fernando Oropeza":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)
        
        elif relevante == "Germán Vázquez":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        elif relevante == "Ronald Ramírez":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        else:
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

    elif encuestado == "Ronald Ramírez":
        consejoR = consejo5[1:4]
        consejoNR = consejo5[1:4]
        st.divider()
        relevante = st.radio("Selecciona al más relevante", consejoR, index=None, horizontal=False)
        st.divider()
        if relevante == "Fernando Oropeza":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)
        
        elif relevante == "Germán Vázquez":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        elif relevante == "Julián Cajigas":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        else:
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)
    
    email = st.text_input("Ingresa el email con el que te registraste al Máster:")
    if st.button("Enviar encuesta", type='secondary'):
            send = sendRelevancia(consejo, encuestado, relevante, menos_relevante, email)


elif consejo == "Consejo 6. Alfonso Pompa":
    encuestado = st.selectbox("Selecciona tu nombre", ("-----", "Alfonso Pompa", "Francisco Madero", "José Maldonado", "Marissa De la Rosa", "Óscar Sánchez Osuna"))
    relevante = None
    menos_relevante = None
    if encuestado == "Alfonso Pompa":
        consejoR = consejo6[1:5]
        consejoNR = consejo6[1:5]
        st.divider()
        relevante = st.radio("Selecciona al más relevante", consejoR, index=None, horizontal=False)
        st.divider()
        if relevante == "Francisco Madero":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)
        
        elif relevante == "José Maldonado":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        elif relevante == "Marissa De la Rosa":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)
        
        elif relevante == "Óscar Sánchez Osuna":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        else:
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

    
    elif encuestado == "Francisco Madero":
        consejoR = consejo6[2:5]
        consejoNR = consejo6[2:5]
        st.divider()
        relevante = st.radio("Selecciona al más relevante", consejoR, index=None, horizontal=False)
        st.divider()
        
        if relevante == "José Maldonado":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        elif relevante == "Marissa De la Rosa":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        elif relevante == "Óscar Sánchez Osuna":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        else:
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

    
    elif encuestado == "José Maldonado":
        consejoR = ["Francisco Madero", "Marissa De la Rosa", "Óscar Sánchez Osuna"]
        consejoNR = ["Francisco Madero", "Marissa De la Rosa", "Óscar Sánchez Osuna"]
        st.divider()
        relevante = st.radio("Selecciona al más relevante", consejoR, index=None, horizontal=False)
        st.divider()
        if relevante == "Francisco Madero":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)
        
        elif relevante == "Marissa De la Rosa":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)
        
        elif relevante == "Óscar Sánchez Osuna":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        else:
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)


    elif encuestado == "Marissa De la Rosa":
        consejoR = ["Francisco Madero", "José Maldonado", "Óscar Sánchez Osuna"]
        consejoNR = ["Francisco Madero", "José Maldonado", "Óscar Sánchez Osuna"]
        st.divider()
        relevante = st.radio("Selecciona al más relevante", consejoR, index=None, horizontal=False)
        st.divider()
        if relevante == "Francisco Madero":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)
        
        elif relevante == "José Maldonado":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        elif relevante == "Óscar Sánchez Osuna":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        else:
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

    elif encuestado == "Óscar Sánchez Osuna":
        consejoR = consejo6[1:4]
        consejoNR = consejo6[1:4]
        st.divider()
        relevante = st.radio("Selecciona al más relevante", consejoR, index=None, horizontal=False)
        st.divider()
        if relevante == "Francisco Madero":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)
        
        elif relevante == "José Maldonado":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        elif relevante == "Marissa De la Rosa":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        else:
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)
    
    email = st.text_input("Ingresa el email con el que te registraste al Máster:")
    if st.button("Enviar encuestas", type='secondary'):
            send = sendRelevancia(consejo, encuestado, relevante, menos_relevante, email)

elif consejo == "Selecciona tu Consejo":
    coord = st.text_input("Introduce la contraseña:", value="")
    if coord == "loreCedem2024":
        coord_consejos = st.selectbox("Selecciona un Consejo", ("Consejos", "Consejo 1. Dunia Guzman", "Consejo 2. José Luis Rodríguez", "Consejo 3. Juan Carlos Ruvalcaba", 
                                                "Consejo 4. Mario Humberto García", "Consejo 5. Roberto Becerra", "Consejo 6. Alfonso Pompa"))

        if coord_consejos == "Consejo 1. Dunia Guzman":
            getconsejos(IDsConsejos[0], consejo1, str(1))
        
        elif coord_consejos == "Consejo 2. José Luis Rodríguez":
            getconsejos(IDsConsejos[1], consejo2, str(2))

        elif coord_consejos == "Consejo 3. Juan Carlos Ruvalcaba":
            getconsejos(IDsConsejos[2], consejo3, str(3))

        elif coord_consejos == "Consejo 4. Mario Humberto García":
            getconsejos(IDsConsejos[3], consejo4, str(4))

        elif coord_consejos == "Consejo 5. Roberto Becerra":
            getconsejos(IDsConsejos[4], consejo5, str(5))

        elif coord_consejos == "Consejo 6. Alfonso Pompa":
            getconsejos(IDsConsejos[5], consejo6, str(6))
    
    elif coord == "":
        st.write("Aún no ingresas la clave")
    else:
        st.error("Contraseña incorrecta!")

else:
    st.write("No se ha seleccionado un Consejo aún")

### test de grupos
#que = '{boards(ids: 7605845746) { groups { title id } name id description items_page { items { name column_values{id type text } } } } }'  # name id description items_page { items { name column_values{id type text } } }
#data = {'query' : que}
#r = requests.post(url=apiUrl, json=data, headers=headers) # make request
#rf = r.json()
#st.write(rf)
