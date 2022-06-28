import './App.css';
//Calling Bootstrap 4.5 css
import 'bootstrap/dist/css/bootstrap.min.css';
import "bootstrap/dist/js/bootstrap.bundle.min";
//Calling Firebase config setting to call the data
import React, { useState, useEffect } from "react";
import "./App.css";
import db from './firebase';

function App () {
  const [perkaraData, setPerkaraData] = useState([]);
  
  useEffect(() => {
    db.collection("sipp").onSnapshot((snapshot) => {
      setPerkaraData(
        snapshot.docs.map((doc) => ({
          id: doc.id,
          data: doc.data(),
        }))
      );
    });
    console.log({ perkaraData });
  }, []);

  return (
    <div className="MainDiv">
      <div className="jumbotron text-center bg-sky">
          <h1>Daftar Perkara</h1>
      </div>
      <div className="container">
          <table id="example" class="display table">
            <thead class="thead-dark">
                <tr>
                    <th>Nomor Perkara</th>
                    <th>Tanggal Register</th>
                    <th>Klasifikasi</th>
                    <th>Pihak</th>
                    <th>Status Perkara</th>
                    <th>Lama Proses</th>
                    <th>Detail</th>
                </tr>
            </thead>
            <tbody>
            {perkaraData?.map(({ id, data }) => (
              <tr key={id}>
                <td>{data.nomorPerkara}</td>
                <td>{data.tanggalRegister}</td>
                <td>{data.klasifikasi}</td>
                <td>{data.paraPihak}</td>
                <td>{data.statusPerkara}</td>
                <td>{data.lamaProses}</td>
                <a href={data.detail}>link</a>
              </tr>
            ))}
                  
            </tbody>
            
         </table>
          
     </div>
    </div>
  );
}
export default App;






// class App extends React.Component {
// constructor(props) {
    
//     super(props);
   
//     this.state = {studentslist : []}
//     }
    
//   componentDidMount() {
   
   
     
//       db.ref("sippt").on("value", snapshot => {
//         let studentlist = [];
//         snapshot.forEach(snap => {
//             // snap.val() is the dictionary with all your keys/values from the 'students-list' path
//             studentlist.push(snap.val());
//         });
//         this.setState({ studentslist: studentlist });
//       });
    
    
//  }
  
//   render(){
//   return (
//     <div className="MainDiv">
//       <div class="jumbotron text-center bg-sky">
//           <h3>How to show db data in reactjs?</h3>
//       </div>
    
//       <div className="container">
//           <table id="example" class="display table">
//             <thead class="thead-dark">
//                 <tr>
//                     <th>FirstName</th>
//                 </tr>
//             </thead>
//             <tbody>
//             {this.state.studentslist.map(data => {
                
//                 return (
//                     <tr>     
//                     <td>{data.nomorPerkara}</td>
//                     </tr>
                    
//                 );
               
//                 })}
        
               
//             </tbody>
            
//          </table>
          
//      </div>
//     </div>
//   );
// }
// }
// export default App;


