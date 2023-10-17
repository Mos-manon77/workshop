import streamlit as st
from firebase_admin import firestore

def app():
    db = firestore.client()

    try:
        st.title('TODOs by: ' + st.session_state['username'] )
            
        result = db.collection('TODOs').document(st.session_state['username']).get()
        r = result.to_dict()
        content = r['Content']
            
        def delete_todo(k):
            c = int(k)
            h = content[c]
            try:
                db.collection('TODOs').document(st.session_state['username']).update({"Content": firestore.ArrayRemove([h])})
                st.warning('TODO deleted')
            except:
                st.write('Something went wrong..')
                
        for c in range(len(content)-1, -1, -1):
            st.text_area(label = ':green[TODO]', value = content[c])
            st.button('Delete TODO', on_click = delete_todo, args = ([c] ), key = c)        

    except:
        if st.session_state.username == '':
            st.text('Please Login first')        