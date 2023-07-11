// import { Dangerous, Done } from "@mui/icons-material";
// import { useEffect, useState } from "react";
// import makeGETRequest from "../../../http_requests/getRequest";
// import url from "../../../url";

// function Diagnostics(){
//     const [error,setError]=useState(false);
//     const [message,setMessage]=useState('Waiting....');
//     useEffect(()=>{
//         const interval=setInterval(async ()=>{
//             var response = await makeGETRequest(url + "status");
//             setError(response.data.error);
//             setMessage(response.data.message);
//             console.log("M"+message);
//             console.log("E"+error.toString());
//         },10000);
//         return ()=>clearInterval(interval);
//     },[]);
//     return (
//         <div style={{width:"100%",height:"30px",display:"flex",alignItems:"center",justifyContent:"center"}}>
//             {error===true?<Dangerous style={{color:"red"}}/>:<Done style={{color:"green"}}/>}
//             <b>{message}</b>
//         </div>
//     );
// }

// export default Diagnostics;