import os
import firebase_admin
from firebase_admin import firestore

from google.cloud.firestore_v1 import Client
from google.cloud.firestore_v1.base_document import DocumentSnapshot
from google.cloud.firestore_v1.collection import CollectionReference


credential = firebase_admin.credentials.Certificate(os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"))
firebase_admin.initialize_app(credential, {'projectId': 'python-web-392316'})
db: Client = firestore.client()


def get_users():
    return db.collection('users').get()


def get_user(user_id) :
    return db.collection("users").document(user_id).get()


def get_user_by_username(username) :
    user = db.collection('users').where(
        "username", "==", username).limit(1).get()
    return user.pop() if len(user) == 1 else None


def get_todos(user_id) :
    return db.collection("users").document(user_id).collection("todos").get()

def create_user(user_data) :
    user_ref = db.collection("users").document(user_data.id)
    user_ref.set({
        "username": user_data.username,
        "password": user_data.password,
    })
    
def create_todo(user_id, todo_data) :
    todo_ref:CollectionReference =  db.collection("users").document(user_id).collection("todos")
    todo_ref.add({
        "title": todo_data["title"],
        "description": todo_data["description"],
        "done":todo_data["done"]
    })
    
def delete_todo(user_id, todo_id) :
    todo_ref =  _get_todo_ref(user_id, todo_id)
    todo_ref.delete()
    
def update_todo(user_id, todo_id, done) :
    todo_ref =  _get_todo_ref(user_id, todo_id)
    todo_ref.update({'done': not done})
    
def _get_todo_ref(user_id, todo_id):
    return db.document(f"users/{user_id}/todos/{todo_id}")
    
# Función para generar un nuevo ID autoincremental
def generate_auto_increment_id(collection_name):
    doc_ref = db.collection('counters').document(collection_name)
    doc = doc_ref.get()
    
    if doc.exists:
        counter = doc.to_dict()['counter']
    else:
        counter = 0
    
    # Incrementa el contador
    counter += 1
    
    # Actualiza el contador en la base de datos
    doc_ref.set({'counter': counter})
    
    # Retorna el nuevo ID autoincremental
    return str(counter)