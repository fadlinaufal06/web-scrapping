import firebase from 'firebase/compat/app';
import 'firebase/compat/auth';
import 'firebase/compat/firestore';

const firebaseConfig = {
  apiKey: "AIzaSyBp67VeHY6dq7aCes6HTHn81BFFGMnXTys",
  authDomain: "scrapping-411c8.firebaseapp.com",
  projectId: "scrapping-411c8",
  storageBucket: "scrapping-411c8.appspot.com",
  messagingSenderId: "787110069059",
  appId: "1:787110069059:web:91b1ee300d5694a993e5f6",
  measurementId: "G-S0QDGTSG12"
};

// Initialize Firebase
const firebaseApp = firebase.initializeApp(firebaseConfig);
const db = firebase.firestore();

export default db;
