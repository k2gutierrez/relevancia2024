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

def sendRelevancia(consejo, encuestado, masR, menosR):
    try:
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

IDsConsejos = ['7601959436', '7605844793', '7605845746', '7605846147', '7605846488', '7605846943']
consejos = ["Consejo 1. Dunia Guzman", "Consejo 2. José Luis Rodríguez", "Consejo 3. Juan Carlos Ruvalcaba", "Consejo 4. Mario Humberto García", "Consejo 5. Roberto Becerra", "Consejo 6. Alfonso Pompa"]
coaches = ["Dunia Guzman", "José Luis Rodríguez", "Juan Carlos Ruvalcaba", "Mario Humberto García", "Roberto Becerra", "Alfonso Pompa"]

consejo1 = ["Dunia Guzman", "Gabriela Sánchez", "Héctor Arias", "José Antonio Carballar"]
consejo2 = ["José Luis Rodríguez", "Christian Flores", "Lucía Félix", "Nicolás Sañudo"]
consejo3 = ["Juan Carlos Ruvalcaba", "Armando Flores", "José Miguel Fernández", "Óscar Sánchez Reyes", "Rodolfo Becerra"]
consejo4 = ["Mario Humberto García", "David Félix", "Emilio Sánchez", "Ildefonso Aviléz", "Marco Flores"]
consejo5 = ["Roberto Becerra", "Fernando Oropeza", "Germán Vázquez", "Julián Cajigas", "Ronald Ramírez"]
consejo6 = ["Alfonso Pompa", "Francisco Madero", "José Maldonado", "Marissa De la Rosa", "Óscar Sánchez Osuna"]

st.title(":blue[Encuesta de Relevancia] :pencil:")
st.subheader("septiembre-octubre")
consejo = st.selectbox("Selecciona tu Consejo", ("Consejos", "Consejo 1. Dunia Guzman", "Consejo 2. José Luis Rodríguez", "Consejo 3. Juan Carlos Ruvalcaba", 
                                                 "Consejo 4. Mario Humberto García", "Consejo 5. Roberto Becerra", "Consejo 6. Alfonso Pompa"))

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
    
    if st.button("Enviar encuesta", type='secondary'):
            send = sendRelevancia(consejo, encuestado, relevante, menos_relevante)


elif consejo == "Consejo 2. José Luis Rodríguez":
    encuestado = st.selectbox("Selecciona tu nombre", ("-----", "José Luis Rodríguez", "Christian Flores", "Lucía Félix", "Nicolás Sañudo"))
    relevante = None
    menos_relevante = None
    if encuestado == "José Luis Rodríguez":
        consejoR = consejo2[1:4]
        consejoNR = consejo2[1:4]
        st.divider()
        relevante = st.radio("Selecciona al más relevante", consejoR, index=None, horizontal=False)
        st.divider()
        if relevante == "Christian Flores":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)
        
        elif relevante == "Lucía Félix":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        elif relevante == "Nicolás Sañudo":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        else:
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

    
    elif encuestado == "Christian Flores":
        consejoR = consejo2[2:4]
        consejoNR = consejo2[2:4]
        st.divider()
        relevante = st.radio("Selecciona al más relevante", consejoR, index=None, horizontal=False)
        st.divider()
        
        if relevante == "Lucía Félix":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        elif relevante == "Nicolás Sañudo":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        else:
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

    
    elif encuestado == "Lucía Félix":
        consejoR = ["Christian Flores", "Nicolás Sañudo"]
        consejoNR = ["Christian Flores", "Nicolás Sañudo"]
        st.divider()
        relevante = st.radio("Selecciona al más relevante", consejoR, index=None, horizontal=False)
        st.divider()
        if relevante == "Christian Flores":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)
        
        elif relevante == "Nicolás Sañudo":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)

        else:
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)


    elif encuestado == "Nicolás Sañudo":
        consejoR = consejo2[1:3]
        consejoNR = consejo2[1:3]
        st.divider()
        relevante = st.radio("Selecciona al más relevante", consejoR, index=None, horizontal=False)
        st.divider()
        if relevante == "Christian Flores":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)
        
        elif relevante == "Lucía Félix":
            consejoNR.remove(relevante)
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)


        else:
            menos_relevante = st.radio("Selecciona al menos relevante", consejoNR, index=None, horizontal=False)
    
    if st.button("Enviar encuesta", type='secondary'):
            send = sendRelevancia(consejo, encuestado, relevante, menos_relevante)


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
    
    if st.button("Enviar encuesta", type='secondary'):
            send = sendRelevancia(consejo, encuestado, relevante, menos_relevante)


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
    
    if st.button("Enviar encuesta", type='secondary'):
            send = sendRelevancia(consejo, encuestado, relevante, menos_relevante)


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
    
    if st.button("Enviar encuesta", type='secondary'):
            send = sendRelevancia(consejo, encuestado, relevante, menos_relevante)


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
    
    if st.button("Enviar encuesta", type='secondary'):
            send = sendRelevancia(consejo, encuestado, relevante, menos_relevante)






















else:
    st.write("No se ha seleccionado un Consejo aún")

