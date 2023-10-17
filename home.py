import streamlit as st
from firebase_admin import firestore

def app():
    if 'db' not in st.session_state:
        st.session_state.db = ''

    db = firestore.client()
    st.session_state.db = db
    
    
    if st.session_state.username == '':
        st.header(' :violet[Login to be able to CREATE!!] ')
    else:
        ph = 'TODO something'    

        todo = st.text_area(label = ' :orange[+ New TODO]', placeholder = ph, height = None, max_chars = 500)
    
        if st.button('Create', use_container_width = 20):
            if todo != '':
                info = db.collection('TODOs').document(st.session_state.username).get()
                if info.exists:
                    info = info.to_dict()
                    if 'Content' in info.keys():
                        t = db.collection('TODOs').document(st.session_state.username)
                        t.update({u'Content': firestore.ArrayUnion([u'{}'.format(todo)])})
                    else:
                        data = {"Content":[todo],'Username':st.session_state.username}
                        db.collection('TODOs').document(st.session_state.username).set(data)    
                else:
                    data = {"Content":[todo],'Username':st.session_state.username}
                    db.collection('TODOs').document(st.session_state.username).set(data)
                    
                st.success('TODO uploaded!!')
        
        st.header(' :violet[Latest TODOs] ')
        
   
    docs = db.collection('TODOs').document(st.session_state['username']).get()
    doc = docs.to_dict()
    content = doc['Content']
    try:
        for c in range(len(content)-1, -1, -1):
            st.text_area(label = ':green[TODOs by:] ' + ':orange[{}]'.format(st.session_state.username), value = content[c], height = 20,)
    except: pass
    
